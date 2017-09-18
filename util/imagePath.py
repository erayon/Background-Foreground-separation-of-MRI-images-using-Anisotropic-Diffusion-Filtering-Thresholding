from skimage import data
import SimpleITK as sitk
import numpy as np
from time import sleep
from scipy import ndimage
from skimage import io
import os
from skimage.io import imread


# import each and every file
def filelocation(directory):
    DEBUG =False
    l = []
    for file in os.listdir(directory):
        img = directory + file
        if DEBUG : print (img)
        l.append(img)
    # the os.listdir function do not give the files in the right order 
    #so we need to sort them
    l=sorted(l)
    return l


def org_image(n,l1):
    img_T1 = sitk.ReadImage(l1[n])
    img_T1_255 = sitk.Cast(sitk.RescaleIntensity(img_T1), sitk.sitkUInt8)
    org_nda = sitk.GetArrayFromImage(img_T1_255)
    org_nda=org_nda[0,:,:]
    return (img_T1,org_nda,img_T1_255)

def LoadOrginalImage(l1):
    img        = np.zeros((512,512,25))
    img_T1     =[]
    img_T1_255 =[]
    pic = np.linspace(0,20,21)
    for i in pic:
        item = int(i)
        [x,y,z] = org_image(item,l1)
        img_T1.append(x)                #  Read image
        img[:,:,item] = y               #  image array
        img_T1_255.append(z)
        sleep(0.01)
        
    imgInt = np.zeros((512,512,25)).astype(np.int64)
    for i in range(24):
        imgInt[:,:,i] = img[:,:,i].astype(np.int64)
        
    return imgInt


# In[4]:


def mask_image(n,l2):
    img = imread(l2[n])
    return img[:,:,1]
    
def LoadGndMask(l2):
    mask = np.zeros((512,512,25))
    pic = np.linspace(1,21,21)
    for i in pic:
        item = int(i)
        mask[:,:,item-1] = mask_image(item,l2)
        sleep(0.01)
    return mask


# In[5]:


# source: http://www.pyimagesearch.com/2014/09/15/python-compare-two-images/
def mse(imageA, imageB):
    # the 'Mean Squared Error' between the two images is the
    # sum of the squared difference between the two images;
    # NOTE: the two images must have the same dimension
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])
    
    # return the MSE, the lower the error, the more "similar"
    # the two images are
    return err

