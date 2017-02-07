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

#getMedian function:purpose is to get median of lists
def getMedian(lst_obj): #find median values 
    srtlist = sorted(lst_obj)
    lst_len = len(lst_obj)
    index = (lst_len-1) / 2
    if(lst_len%2):
        return srtlist[index]
    else:
        return (srtlist[index] + srtlist[index+1])/2


#list to store pixels
red_pix_list = []
green_pix_list = []
blue_pix_list = []

#list to store images
img_list=[]
for filename in glob.glob('/home/ubuntu/workspace/cst205proj1/Proj1images/*.png'): #regex looking for images that end in .png format, needed to use absolute path not relative
        #error checking for getting pictures and their pixels rgb values
        try:
            img=Image.open(filename)
            img_width, img_height = img.size
            for x in range(img_width):
                for y in range(img_height):
                    r,g,b = img.getpixel((x,y))
                    red_pix_list.append(r)
                    green_pix_list.append(g)
                    blue_pix_list.append(b)
            img_list.append(img)
            print(img.format, img.size, img.mode)#tesing image info
        except IOError: 
            print('An error occured opening the file.')

print len(img_list)#check if all images were loaded.
i_width , i_height = img_list[0].size
print i_width, i_height # testing if width and height were grabbed successfully

print len(red_pix_list), len(green_pix_list), len(blue_pix_list) #testing if values were added successfully

#calculate median of the lists 
r_median = getMedian(red_pix_list)
g_median = getMedian(green_pix_list)
b_median = getMedian(blue_pix_list)

print r_median, g_median, b_median #test the median values of said list

#/cst205proj1/images  -relative path
#print "Hello, World"

#git pracfile
        