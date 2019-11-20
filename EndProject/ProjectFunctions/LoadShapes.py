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
from PIL import Image

# Path name needs change everytime we run from a different computer
# Ref: https://stackoverflow.com/questions/39195113/how-to-load-multiple-images-in-a-numpy-array

def getStar():
    imageList = glob.glob('DataSet/star/*.png')
    x  = np.array([np.array(Image.open(fname)) for fname in imageList])
    return x

def getCircle():
    imageList = glob.glob('DataSet/circle/*.png')
    x  = np.array([np.array(Image.open(fname)) for fname in imageList])
    return x

def getSquare():
    imageList = glob.glob('DataSet/square/*.png')
    x  = np.array([np.array(Image.open(fname)) for fname in imageList])
    return x

def getTriangle():
    imageList = glob.glob('DataSet/triangle/*.png')
    x  = np.array([np.array(Image.open(fname)) for fname in imageList])
    return x


def reshape(data):
    image = data.reshape(200, 200)
    return image

def get_yStar():
    return np.array(["Star" for s in getCircle()])
    
    
def get_yCircle():
    return np.array(["Circle" for s in getCircle()])

    
def get_ySquare():
    return np.array(["Square" for s in getCircle()])
    
    
def get_yTriangle():
    return np.array(["Triangle" for s in getCircle()])
    


def resizeAllShapesArrays():
    size = getCircle().shape[0]
    
    star = getStar()[:size]
    circle = getCircle()[:size]
    square = getSquare()[:size]
    triangle = getTriangle()[:size]
    
    return star, circle, square, triangle

def getShapes():    
    X  = np.array([getStar()[:3700]])
    X.extend(getCircle()[:3700])
    X.extend(getSquare()[:3700])
    X.extend(getTriangle()[:3700])
    
    y = np.array([get_yStar()[:3700]])
    y.extend(get_yCircle()[:3700])
    y.extend(get_ySquare()[:3700])
    y.extend(get_yTriangle()[:3700])
    
    return X, y
    


