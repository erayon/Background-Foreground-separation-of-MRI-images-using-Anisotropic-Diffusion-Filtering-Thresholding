# # import Dependencies

import sys
import os
from os import path
sys.path.append(path.abspath('./util'))

import matplotlib.pyplot as plt
import numpy as np
import warnings
from AnDiffusion import *
from MaskGenAlgo import *
from tqdm import tqdm
from hysteresisThresholding import apply_hysteresis_threshold
from time import sleep
from skimage.morphology import erosion, dilation, opening, closing, white_tophat
from skimage.morphology import disk
from ImageFinder import *
import os
from scipy.stats import norm
from scipy.ndimage.morphology import binary_fill_holes
import argparse

def loadimage(Ipath):
    l = filelocation(Ipath)
    [orgImge,nofimage] =  LoadOrginalImage(l)
    print("Total no of image = ",nofimage)
    return (orgImge,nofimage,l)

def converter(Ipath):
    [orgImge,nofimage,l] = loadimage(Ipath)
    mask   = np.zeros((512,512,nofimage))
    fgnd   = np.zeros((512,512,nofimage))
    actImg = np.zeros((512,512,nofimage))
    selem  = disk(4)
    print("Start Genarate Mask--- ")
    for i in tqdm(range(nofimage)):
        img             = orgImge[:,:,i]
        diff            = anisodiff(img,20,50,0.1)
        mu,sigma        = norm.fit(diff)
        htr             = apply_hysteresis_threshold(diff,mu,sigma).astype(int)
        pmask           = binary_fill_holes(htr)
        eroded          = erosion(pmask, selem)
        [fg,bg]         = foregroundBackground(eroded,img)
        mask[:,:,i]     = eroded
        fgnd[:,:,i]     = fg
        actImg[:,:,i]   = img
        sleep(0.1)
    return (mask,fgnd,actImg,nofimage,l)


def saveimage(Spath):
    [mask,fgnd,actImg,nofimage,l] = converter(Ipath)
    dictr = Spath
    print("Save output images.......")
    for i in tqdm(range(nofimage)):
        x=l[i].split("/")
        loc1=dictr+x[-1]+'.png'
        loc2=dictr+x[-1]+'fg'+'.png'
        loc3=dictr+x[-1]+'actImg'+'.png'
        plt.imsave(loc1,mask[:,:,i],cmap = plt.cm.gray) # save psudo mask
        plt.imsave(loc2,fgnd[:,:,i],cmap = plt.cm.gray)
        plt.imsave(loc3,actImg[:,:,i],cmap = plt.cm.gray)



if __name__ =="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("Input_Folder",help=": Location of folder Dicom files")
    parser.add_argument("Output_Folder",help=": Location of folder where to save")

    args  = parser.parse_args()
    Ipath = args.Input_Folder
    Spath = args.Output_Folder
    saveimage(Spath)
