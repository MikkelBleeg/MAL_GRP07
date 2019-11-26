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
    return np.array(["Star" for s in getStar()])
    
    
def get_yCircle():
    return np.array(["Circle" for s in getCircle()])

    
def get_ySquare():
    return np.array(["Square" for s in getSquare()])
    
    
def get_yTriangle():
    return np.array(["Triangle" for s in getTriangle()])
    


def resizeAllShapesArrays():
    size = getCircle().shape[0]
    
    star = getStar()[:size]
    circle = getCircle()[:size]
    square = getSquare()[:size]
    triangle = getTriangle()[:size]
    
    return star, circle, square, triangle

def getShapes():
    xAppend = []
    yAppend = []
    star = getStar()
    circle = getCircle()
    square = getSquare()
    triangle = getTriangle()
    
    ystar = get_yStar()
    ycircle = get_yCircle()
    ysquare = get_ySquare()
    ytriangle = get_yTriangle()
    
    
    for i in range(len(star)):
        xAppend.append(star[i])
        
    for i in range(len(ystar)):
        yAppend.append(ystar[i])
        
    for o in range(len(circle)):
        xAppend.append(circle[o])
    for o in range(len(ycircle)):
        yAppend.append(ycircle[o])
      
    for n in range(len(square)):
        xAppend.append(square[n])
    for n in range(len(ysquare)):
        yAppend.append(ysquare[n])
    
    
    for s in range(len(triangle)):
        xAppend.append(triangle[s])
    for s in range(len(ytriangle)):
        yAppend.append(ytriangle[s])

    
    return xAppend, yAppend

def getNewShapes():
    imageList = glob.glob('NewTestData/*.png')
    x  = np.array([np.array(Image.open(fname)) for fname in imageList])
    return x
    
def oneHotcleanup(data):
    for i in range(data.shape[0]):
        for n in range(data[i].shape[0]):

            if data[i, n] < 0.9:
                data[i, n] = 0
            else:
                data[i, n] = 1
            
    return data


def oneHotDecode(data):
    retData = []
    for i in range(data.shape[0]):
        decoded = label_encoder.inverse_transform([argmax(data[i,:])])
        retData.append(decoded)
        
    return retData
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    