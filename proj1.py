'''
Dante Lacey-Thompson
CST205-MultiMedia Programming
Project1
This project will allow the user to filter out a certain thing that they wouldn't like in a series of pics.
It will do this by loading the images, applying a median filter, and then using that to create the new image.
It takes the images from the Proj1images folder and apply the filterinto a new images that will be stored within the images folder
'''

#github link: https://github.com/dantelt24/CST205

from PIL import Image
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


#list to store images
img_list=[]
for filename in glob.glob('/home/ubuntu/workspace/cst205proj1/Proj1images/*.png'): #regex looking for images that end in .png format, needed to use absolute path not relative
        #error checking for getting pictures
        try:
            img=Image.open(filename)
            img_width, img_height = img.size
            img_list.append(img)
            #print(img.format, img.size, img.mode)#tesing image info
        except IOError: 
            print('An error occured opening the file.')

#print len(img_list)#check if all images were loaded.
i_size = img_list[0].size
#print i_size #testing if size was grabbed correctly

#create new image
new_img = Image.new('RGB', i_size)
new_img_width, new_img_height = new_img.size

#loop through the pixels
for x in range(new_img_width):
    for y in range(new_img_height):
        #list to store pixels
        red_pix_list = []
        green_pix_list = []
        blue_pix_list = []
        for img_num in range(0, len(img_list)):#loop through each image at (x,y) to get most common pixel value
            r,g,b = img_list[img_num].getpixel((x,y))
            red_pix_list.append(r)
            green_pix_list.append(g)
            blue_pix_list.append(b)
        r_median = getMedian(red_pix_list)
        g_median = getMedian(green_pix_list)
        b_median = getMedian(blue_pix_list)
        #print r_median, g_median, b_median # checking that i am getting median values
        new_img.putpixel((x,y), (r_median, g_median, b_median)) #place the median values into the new image

new_img.save('/home/ubuntu/workspace/cst205proj1/Proj1images/combined.png') #save the new image to be able to open and view it
new_img.show()#show the image



