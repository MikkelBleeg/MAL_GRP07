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

def getSet00():
    img = []
    path = "C:\\Users\\Trung\\Documents\\ITMAL\\MAL_GRP07\\Exercise05\\Dataset\\CAT_00\\*.jpg"
    for file in glob.glob(path):
#          print(file)
        a=cv2.imread(file, cv2.IMREAD_GRAYSCALE)
        img.append(a)
    return img

def getSet01():
    img = []
    path = "C:\\Users\\Trung\\Documents\\ITMAL\\MAL_GRP07\\Exercise05\\Dataset\\CAT_01\\*.jpg"
    for file in glob.glob(path):
#         print(file)
        a=cv2.imread(file, cv2.IMREAD_GRAYSCALE)
        img.append(a)
    return img

def getSet02():
    img = []
    path = "C:\\Users\\Trung\\Documents\\ITMAL\\MAL_GRP07\\Exercise05\\Dataset\\CAT_02\\*.jpg"
    for file in glob.glob(path):
#         print(file)
        a=cv2.imread(file, cv2.IMREAD_GRAYSCALE)
        img.append(a)
    return img

def getSet03():
    img = []
    path = "C:\\Users\\Trung\\Documents\\ITMAL\\MAL_GRP07\\Exercise05\\Dataset\\CAT_03\\*.jpg"
    for file in glob.glob(path):
#       print(file)
        a=cv2.imread(file, cv2.IMREAD_GRAYSCALE)
        img.append(a)
    return img

def getSet04():
    img = []
    path = "C:\\Users\\Trung\\Documents\\ITMAL\\MAL_GRP07\\Exercise05\\Dataset\\CAT_04\\*.jpg"
    for file in glob.glob(path):
#       print(file)
        a=cv2.imread(file, cv2.IMREAD_GRAYSCALE)
        img.append(a)
    return img



def getSet05():
    img = []
    path = "C:\\Users\\Trung\\Documents\\ITMAL\\MAL_GRP07\\Exercise05\\Dataset\\CAT_05\\*.jpg"
    for file in glob.glob(path):
#       print(file)
        a=cv2.imread(file, cv2.IMREAD_GRAYSCALE)
        img.append(a)
    return img



def getSet06():
    img = []
    path = "C:\\Users\\Trung\\Documents\\ITMAL\\MAL_GRP07\\Exercise05\\Dataset\\CAT_06\\*.jpg"
    for file in glob.glob(path):
#       print(file)
        a=cv2.imread(file, cv2.IMREAD_GRAYSCALE)
        img.append(a)
    return img



def reshape(data):
    image = data.reshape(200, 200)
    return image