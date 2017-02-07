'''
Dante Lacey-Thompson
CST205-MultiMedia Programming
Project1
This project will allow the user to filter out a certain thing that they wouldn't like in a series of pics.
It will do this by loading the images, applying a median filter, and then using that to create the new image.
'''

from PIL import Image
import sys
import os
import glob #glob allows for unix-style filename pattern matching, allowing you to use regex to find the files you would like in python

img_list=[]
for filename in glob.glob('/home/ubuntu/workspace/cst205proj1/Proj1images/*.png'): #regex looking for images that end in .png format, needed to use absolute path not relative
        #error checking
        try:
            img=Image.open(filename)
            img_list.append(img)
            print(img.format, img.size, img.mode)#tesing image info
        except IOError: 
            print('An error occured opening the file.')
print len(img_list)#check if all images were loaded.
#/cst205proj1/images  -relative path
#print "Hello, World"

#git pracfile

def getMedian(lst_obj): #find median values 
    srtlist = sorted(lst_obj)
    lst_len = len(lst_obj)
    index = (lst_len-1) / 2
    if(lst_len%2):
        return srtlist[index]
    else:
        return (srtlist[index] + srtlist[index+1])/2

        