{
 "cells": [],
 "metadata": {},
 "nbformat": 4,
 "nbformat_minor": 2
}

import cv2
import numpy as np
import glob
import os
import matplotlib
import matplotlib.pyplot as plt

#path name needs change everytime we run from a different computer

def getStar():
    img = []
    #Set Path
    path = "C:\\Users\\Trung\\Documents\\ITMAL\\MAL_GRP07\\DataSet\\star\\*.png"
    for file in glob.glob(path):
#          print(file)
        a=cv2.imread(file, cv2.COLOR_BGR2RGB)
        #Change to right colour order
#         b,g,r = cv2.split(a)           # get b, g, r
#         NewIm = cv2.merge([r,g,b])     # switch it to r, g, b
        img.append(a)
    return img

def getCircle():
    img = []
    path = "C:\\Users\\Trung\\Documents\\ITMAL\\MAL_GRP07\\Dataset\\circle\\*.png"
    for file in glob.glob(path):
#         print(file)
        a=cv2.imread(file, cv2.COLOR_BGR2RGB)
#         b,g,r = cv2.split(a)           # get b, g, r
#         NewIm = cv2.merge([r,g,b])     # switch it to r, g, b
        img.append(a)
    return img

def getSquare():
    img = []
    path = "C:\\Users\\Trung\\Documents\\ITMAL\\MAL_GRP07\\Dataset\\square\\*.png"
    for file in glob.glob(path):
#         print(file)
        a=cv2.imread(file, cv2.COLOR_BGR2RGB)
#         b,g,r = cv2.split(a)           # get b, g, r
#         NewIm = cv2.merge([r,g,b])     # switch it to r, g, b
        img.append(a)
    return img

def getTriangle():
    img = []
    path = "C:\\Users\\Trung\\Documents\\ITMAL\\MAL_GRP07\\Dataset\\triangle\\*.png"
    for file in glob.glob(path):
#       print(file)
        a=cv2.imread(file, cv2.COLOR_BGR2RGB)
#         b,g,r = cv2.split(a)           # get b, g, r
#         NewIm = cv2.merge([r,g,b])     # switch it to r, g, b
        img.append(a)
    return img




def reshape(data):
    image = data.reshape(200, 200)
    return image