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

def getSquare():
    img = []
    path = "C:\\Users\\Trung\\Documents\\ITMAL\\MAL_GRP07\\Exercise05\\Shapes\\shapes\\square\\*.png"
    for file in glob.glob(path):
#          print(file)
        a=cv2.imread(file, cv2.IMREAD_GRAYSCALE)
        img.append(a)
    return img

def getCircle():
    img = []
    path = "C:\\Users\\Trung\\Documents\\ITMAL\\MAL_GRP07\\Exercise05\\Shapes\\shapes\\circle\\*.png"
    for file in glob.glob(path):
#         print(file)
        a=cv2.imread(file, cv2.IMREAD_GRAYSCALE)
        img.append(a)
    return img

def getStar():
    img = []
    path = "C:\\Users\\Trung\\Documents\\ITMAL\\MAL_GRP07\\Exercise05\\Shapes\\shapes\\star\\*.png"
    for file in glob.glob(path):
#         print(file)
        a=cv2.imread(file, cv2.IMREAD_GRAYSCALE)
        img.append(a)
    return img

def getTriangle():
    img = []
    path = "C:\\Users\\Trung\\Documents\\ITMAL\\MAL_GRP07\\Exercise05\\Shapes\\shapes\\triangle\\*.png"
    for file in glob.glob(path):
#       print(file)
        a=cv2.imread(file, cv2.IMREAD_GRAYSCALE)
        img.append(a)
    return img

def reshape(data):
    image = data.reshape(200, 200)
    return image