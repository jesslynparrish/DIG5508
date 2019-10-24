# Think about what you want to do for the final project - it's due the last week of classes
# Look up how python can work with AR (& unity)
# We're covering chapter 10 in class tonight.
# Next week, read through chapter 11
# today we're talking about pixels (images)
# LAB 2 DUE NEXT WEEK! - plan for 6-8 hours max
# Free project 2 is due the week after Lab 2 is due (Murray suggests doing something more image oriented than text oriented for free project 2)

#%%
Main Topics for today:
Regular Expressions
Classes
Image Manipulation & Analysis with PIL (Ch. 10 & 11)
Lab 2 & Individual meetings

#%%
Regular Expressions (JS, Visual Studio, & Python)
-Used for text Analysis
-translate what humans understand as time into something the computer understands

Syntax:
-literals (the character itself)
character calsses (One of ...[abc])
special characters: \w for word character
repetition:
    ? Optional
    * repeat or more times
    + repeat 1 or more times
    {2} exactly 2

you can match a string against a regular expression. this returns all matches within a string, including capture groups 
    re.match

you can search a string, finding the first occurrence of a pattern

Groups:
regular expression groups are used to separate defferent strings
E.g.  detecting a username, a domain name, and a top-level domain from an email address:
    (\w)+@(\w)+\.(\w)+
They are also called Capture Groups

#%%
#%%
# A class is a function with valuables associated with it
#Classes do not use parameter list
#using a period calls a method in a class

class MyClass:
    """A simple example class"""
    i = 12345
    def __init__(self, name):
        self.name = name
    def f(self):
        return 'hello world from ' + self.name

#%%
aClass = MyClass("John")
print(aClass.f())
bClass = MyClass("Lucy")
print(bClass.f())

#%%
import json
data = {
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian"
    }
}
#%% 
with open('out.json','w') as fh:
    json.dump(data, fh)

#%%
# Importing data from a json file:
with open('out.json', 'r') as nfh:
    obj = json.load(nfh)
    print(obj)
    print(obj["president"]["name"])

#%%
import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
print(x)
#(xoeu)*
# x*

#%%
# US zip code (either 5 or 5+4)
# \d = [0-9]
zipcode1 = "33555"
zipcode2 = "12345-1234"
x = re.search("\d{5}(-\d{4})?", zipcode1)
print(x)
#%%
zipcode2 = "54321-4321"
x = re.search("\d{5}(-\d{4})?", zipcode2)
print(x)
#%%
 zip = "334440099"
 x = re.search("^\d{5}(-\d{4})?$", zip)
 print(x)
# Principle of programming: don't repeat yourself. One option is creating a function that you can use multiple times
# Remember you can have a cheat sheet handy! One used in class: https://www.debuggex.com/cheatsheet/regex/python
#%%

# Time of day (with groups for each part)

time = "5pm"
time2 = "1400"
time3 = "11:00"
time4 = "13:00am"
time5 = "9:02pm"

regexpression = "^([1-9]|1[0-2])(:\d\d)?[ap]m?$"
print(re.search(regexpression, time))
print(re.search(regexpression, time2))
print(re.search(regexpression, time3))
print(re.search(regexpression, time4))
print(re.search(regexpression, time5))


# phone number (either with or without area code)

#%%
txt = "aaaaaaaaa"
x = re.search("a+", txt)
print(x)

#%%
#Pixels:
# do i need to install PIL ?
from PIL import Image
#%%
mode = 'RGBA'
size = (100, 100)
color = (0, 255, 0, 255)
ourimage = Image.new(mode, size, color)
ourimage

#%%
