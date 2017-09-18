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
    rng        = len(l1)
    img        = np.zeros((512,512,rng))
    img_T1     =[]
    img_T1_255 =[]
    cnt        = 0
    for i in range(len(l1)):
        item = int(i)
        try:
            [x,y,z] = org_image(item,l1)
            img_T1.append(x)                #  Read image
            img[:,:,item] = y               #  image array
            img_T1_255.append(z)
            cnt+= 1
            sleep(0.01)
        except:
            pass
        
    imgInt = np.zeros((512,512,rng)).astype(np.int64)
    for i in range(cnt):
        imgInt[:,:,i] = img[:,:,i].astype(np.int64)
        
    return (imgInt,cnt)
