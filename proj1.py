from PIL import Image
import sys
import os
import glob

img_list=[]
for filename in glob.glob('/home/ubuntu/workspace/cst205proj1/Proj1images/*.png'): #regex looking for images that end in .png format, needed to use absolute path not relative
        img=Image.open(filename)
        img_list.append(img)
        print(img.format, img.size, img.mode)#tesing image info
print len(img_list)#check if all images were loaded.
#/cst205proj1/images  -relative path
#print "Hello, World"

#git pracfile

