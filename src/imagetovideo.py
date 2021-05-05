import cv2
import numpy as np
import glob

def image_to_video():

    img_array = []
    #Import images and get relevant informations for building the video and saveing it into an array
    for filename in glob.glob('./Images/*.jpg'):
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width,height)
        img_array.append(img)
    #Create Video Writer
    out = cv2.VideoWriter('Video.avi',cv2.VideoWriter_fourcc(*'DIVX'), 1, size)

    #Build and write video
    for i in range(len(img_array)):
        out.write(img_array[i])
    out.release()

image_to_video()