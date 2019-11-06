#%%
#This cell is practice for Chapter 10 in prepping my mindset for how python works in Ch.10
#Please jump down to line 40 to see Free Project 10-1! Thank you!
from PIL import image


# %%
#Also a practice cell
#Practicing the python code for creating an image. 
#Problem I'm having with running the code in Python Interactive - the cells are taking a long time to run and I don't understand what's going on
#Why is it taking so long for VS Code to connect to Jupyter server?

ourimage = Image.new('RGBA', (100, 100), 'black')

mode = 'RGBA'
size = (100, 100)
color = 'black'
ourimage = Image.new(mode, size, color)
ourimage.save('practiceImage.png')
# %%
#Also a practice cell
#creating image & putting in 1 while pixel in the middle
allblack = Image.new('RGB', (100, 100))
allblack.putpixel((50, 50), (255, 255, 255, 255))
allblack.save('almostall.png')

#code for going through entire image:
from PIL import Image
rectangle = Image.new('RGB', (150, 100))
for x in range(150):
    for y in range(100):
        rectangle.putpixel((x, y), (127, 127, 127, 255))

#creating a gradient image

for x in range(150):
    for y in range(100):
        rectangle.putpixel((x, y), (x, x, x))
rectange.save('gradient.png')
#%%
#Project 2 Starts Here!!!!
#Image Generator
#I am choosing to create an image generator for this exercise, I do not yet see how it could be converted to a text generator or vice versa...we'll see what happens

from PIL import Image
GenerateImage = Image.new('RGBA', (300, 300), (52, 67, 235, 255))
mode = 'RGB' #I'm not sure if I need this since I want to make it so users can define their image in number values
size = (300, 300)
color = (52, 67, 235, 255)

#Users would see the parameters laid out and this example of creating a blue colored box, and would then use the function 'GenerateImage' to define the parameters of the image they want to create (the mode, size, and color)

GenerateImage = Image.new(mode, size, color))

#An example of how to user could utilize this function to create an image:
mode = 'RGB'
size = (550, 325)
color = (100, 100, 100, 255)
GenerateImage

#My logic in creating this code is that it defines the parameters of the image so that users can use this function to create the image they want

#Converting to a text generator?
#Can I use the same type of function and swap out the names of functions? Similar to the Mad Libs exercise?
