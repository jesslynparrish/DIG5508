#%%
# [2-4] ON YOUR OWN: 
# Using code, create a new function that accepts three arguments: (1) an image created by Image.new, and (2) a x value, and (3) a color specified as a 4-tuple. 
# The function should return the image that has a vertical line drawn across it in the color provided.

# For instance, if it were named vert_line:
# image = Image.new(100,100)
# vert_line(image, 50, (10,30,50,255))

# You must create the vertical line on an image of any size.
 
# WRITE YOUR CODE HERE
image = Image.tiny(50,50)
vertical_line(image, 25, (10,30,50,255))

#%%
# [2-5] ON YOUR OWN:
# Write a function that generates a radial gradient in an image given a particular coordinate. Your function should take in an image of any size and create a radial gradient from the coordinate provided in the form of a tuple.

# For instance, if the function were called "gradient", and "image" contained a 100 x 100 image, you could call the function like so:

# gradient(image, (25,25))

# This would return the same image with the gradient starting at 25, 25. You may either specify the color in the function or accept two quadtuples as arguments:
# gradient(image, (25,25), (100,100,100,255),(200,200,200,255)
# or, with each argument given its own variable:
# location = (25,25)
# color_1 = (100,100,100,255)
# color_2 = (200,200,200,255)
# gradient(image,location,color_1,color_2)

#My code:
gradient(image, (15,15))

gradient(image, (15,15), (143,50,168,255),(166,50,168,255)

#or if trying the other code option listed above:

location = (15,15)
color_1 = (143,50,168,255)
color_2 = (166,50,168,255)
gradient(image,location,color_1,color_2)
#%%
# [2-6] ON YOUR OWN:
# Write a function that takes as an input an image. 
# Create a "Thumbnail" image of the provided image that is 1/3 of the size of the original image, and return it. The new image should have the same color space as the original, and work with either RGB or RGBA color schemes.

from PIL import Image
image = Image.open("Lab2/laika.jpg")
MAX_SIZE = (100, 100)

image.thumbnail(MAX_SIZE)

image.save("laikathumb.jpg")
image.show()
 
 #In working on the code for creating a thumbnail, I used code from this website: https://www.geeksforgeeks.org/python-pil-image-thumbnail-method/
#%%
# [2-7] ON YOUR OWN:
# Given a formula to calculate the "luminance" of a pixel as:
#  L  =  0.2126 × R   +   0.7152 × G   +   0.0722 × B 
# Write a function that accepts an image and returns a new image that is in grayscale that is the same dimensions.

def modify(image):
    for x: original_image(50, 50, (3,40,252,255))
    for y: greyscale_image(50, 50, (0.2126*3, 0.7152*40, 0.0722*252,255))
    print(image)  

#I did not try the code described in chapter 11, I was trying to create a function that would modify the image with x being the original value and y being the modified image, or the image with a "luminance" 
#As we discuss this in class, I realize I was more off base than I thought. Chapter 11 is making a bit more sense as we are discussing these problems in class - to an extent. I hope i remember this stuff after I leave class
#%%
# [2-8] ON YOUR OWN:
# Write a function that applies the grayscale method to all of the image files in a directory.
# Use the Glob library. Make sure the new images have "_gray" appended to their name. This means "img1.png" would be written as "img1_gray.png". Guidance for doing this can be found in Montfort's Chapter 11. 

import glob
glob.glob('*.jpg')

import glob
file_list = glob.glob('*.jpg')
for filename in file_list:
    current - Image.open(filename)
    old_skool(current)
    current.save(filename)
    
def modify(image):
    for 

current.save("laika_gray.jpg")
print(image)