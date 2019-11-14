# Even though there are multiple objects, we still only need one class. 
# No matter how many cookies we make, only one cookie cutter is needed.
class Car(object):
# The Constructor is defined with arguments.
    def __init__(self, c, xpos, ypos, xspeed):
        self.c = c
        self.xpos = xpos
        self.ypos = ypos
        self.xspeed = xspeed
        
    def display(self):
        stroke(0)
        fill(self.c)
        rectMode(CENTER)
        rect(self.xpos, self.ypos, 20, 10);
    
    def drive(self):
        self.xpos = self.xpos + self.xspeed;
        if self.xpos > width:
            self.xpos = 0

class Light(object):
    def __init__(self, xpos, ypos, longer):
        self.xpos = xpos
        self.ypos = ypos
        self.longer = longer
    
    def display(self):
        stroke(0)
        fill(color(197,66,245)) #purple
        ellipse(self.xpos, self.ypos, 20, self.longer)

class grass(object):
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
    
    def display(self):
        stroke(0)
        fill(color(66,245,87))
        rectMode(CENTER)
        rect(self.xpos, self.ypos, 30, 30)
        
class stopsign(object):
    def __init__(self, xpos, ypos):
         self.xpos = xpos
         self.ypos = ypos
    def display(self):
        stroke(0)
        fill(color(252,28,3))
        triangle(self.xpos, self.ypos)
        
               
import random 
myCar1 = Car(color(255, 0, 0), 0, 100, 2)
myCar2 = Car(color(0, 255, 255), 0, 10, 1)
    
def setup():
    size(500,500)



#Lights array
lights = []
for i in range(3):
    lights.append(Light((15*i)+50, 60, random.randint(5,25)))

grasses = []

grasstype = 0

#Creating a function so it will create a new speed of car
def newspeed():
    xspeed = random.randint(1,10)
    println("works")
    return xspeed


#create the new speed when the key is pressed
def keyPressed():
    if (key == 'a'):
        myCar1.xspeed = newspeed()
    if (key == 'b'):
        myCar2.xspeed = newspeed()
    if (key == 'g'):
        grasstype = 0
    if (key == 'h'):
        println("pressed")
        grasstype = 1

#create grass when mouse is pressed
def mousePressed():
    if (grasstype == 0):
        grasses.append(grass(mouseX, mouseY))
        println("grass")
    if (grasstype == 1):
        grasses.append(stopsign(mouseX, mouseY))
        println("stop sign")
#create stop sign when key is pressed

def draw(): 
  background(255)
  myCar1.drive()
  myCar1.display()
  myCar2.drive()
  myCar2.display()
  for i in lights:
    i.display()
  for i in grasses:
      i.display()
  if (grasstype == 0):
      instruction = "click anywhere to plant some grass. press h to place stop signs"
  if (grasstype == 1):
      instruction = "click to place stop sign. press g to return to planting grass"
  text(instruction, 100, 160, 180, 30)
