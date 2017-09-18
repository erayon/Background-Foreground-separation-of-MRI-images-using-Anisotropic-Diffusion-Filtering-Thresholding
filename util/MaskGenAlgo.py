import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage.filters import median_filter
from AnDiffusion import *

def partialSum(y,j):
    x = 0;
    for i in range(j):
        x+=y[i]
    return x;

def Percentile(data,ptile):
    ptile = ptile
    avec = np.zeros(256)
    total = partialSum(data,256)
    temp = 1.0
    threshold=-1
    for i in range(256):
        avec[i] = np.abs((partialSum(data,i)/total)-ptile)
        if avec[i]<temp:
            temp = avec[i]
            threshold = i
    return threshold


def Thresholding_op(x,th):
    t=np.copy(x)
    low_values_indices = x < th
    high_values_indices= x>=th
    t[low_values_indices] = 0 
    t[high_values_indices]= 1
    return t


def algorithm(img,ptile,medfiltsize,niter,kappa,gamma):
    
    """
      Usage:
        mask = anisodiff(im,ptile,niter,kappa,gamma)
 
        Arguments:
                img         - input image
                ptile       - percentile range between 0 and 1
                medfiltsize - Median filter size greater than int val 1
                niter       - number of iterations
                kappa       - conduction coefficient 20-100 ?
                gamma       - max value of .25 for stability
        Returns:
                out   - Mask image.
    """
    
    diff            = anisodiff(img,niter=niter,kappa=kappa,gamma=gamma)
    hist, bin_edges = np.histogram(diff,bins=256)
    thresholdValue  = Percentile(hist,ptile)
    segmentation    = Thresholding_op(diff,thresholdValue)
    medianFilter    = median_filter(segmentation,medfiltsize)
    mask            = medianFilter
    return (mask,diff)


def foregroundBackground(mask,originalImage):

    """
      Usage:
        [fg,bg] = foregroundBackground(mask,originalImage)
 
        Arguments:
               mask                 - Mask image
               originalImage        - original image
   
        Returns:
                (Forground, background)  - nd image.
    """
  
    [row,col] = np.shape(mask)
    fg = np.abs(mask*originalImage)
    fg = np.copy(fg)
    bg = originalImage
    bg = np.copy(bg)
    for i in range(row):
        for j in range(col):
                if(mask[i,j]==1):
                    bg[i,j]=255
                if(mask[i,j]==0):
                    fg[i,j]=255
    return (fg,bg)


def plot_comparison(original, filtered, filter_name):
    fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(8, 4), sharex=True,sharey=True)
    ax1.imshow(original, cmap=plt.cm.gray)
    ax1.set_title('histogram_equalized_image')
    ax1.axis('off')
    ax1.set_adjustable('box-forced')
    ax2.imshow(filtered, cmap=plt.cm.gray)
    ax2.set_title(filter_name)
    ax2.axis('off')
    ax2.set_adjustable('box-forced')


