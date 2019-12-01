#Goal is to create a function so that when the mouse is clicked a rectangle is placed at the mouse's position
class holidayLight(object):
    def __init__(self, c, xpos, ypos, xspeed):
        self.c = c
        self.xpos = xpos
        self.ypos = ypos
        self.xspeed = xspeed
        
    def display(self):
        stroke(2)
        fill(self.c)
        # rectMode(CENTER)
        ellipse(self.xpos, self.ypos, 80, 80);
    
    def drive(self):
        self.xpos = self.xpos + self.xspeed;
        if self.xpos > width:
            self.xpos = 0

myHolidayLight1 = holidayLight(color(62, 194, 201), 0, 100, 2)
myHolidayLight2 = holidayLight(color(235, 21, 128), 0, 10, 1)
myHolidayLight3 = holidayLight(color(252, 50, 5), 0, 50, 4)
myHolidayLight4 = holidayLight(color(252, 255, 89), 0, 200, 3)
myHolidayLight5 = holidayLight(color(247, 130, 20), 0, 300, 6)
myHolidayLight6 = holidayLight(color(149, 20, 247), 0, 400, 5)

class wreath(object):
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
    
    def display(self):
        stroke(0)
        fill(color(32, 212, 32))
        rectMode(CENTER)
        rect(self.xpos, self.ypos, 60, 60)
        #I made the squares larger so that they wouldn't be drowned in the lights/circles
        #Originally I wanted to have this be triangles, and I found the syntax for defining a triangle but I got too confused at how to define each point and decided to use rectangles because I understand how to define them
wreaths = []        
wreathType = 0

def setup():
    size(500,500)
    
    
def mousePressed():
    if (wreathType == 0):
        wreaths.append(wreath(mouseX, mouseY))
        println("Holidays!")
    if (wreathType == 1):
        wreaths.append(wreath(mouseX, mouseY))
        println("More Holiday Fun!")
#Should allow user to draw a wreath
        
def draw(): 
  background(255)
  myHolidayLight1.drive()
  myHolidayLight1.display()
  myHolidayLight2.drive()
  myHolidayLight2.display()
  myHolidayLight3.drive()
  myHolidayLight3.display()
  myHolidayLight4.drive()
  myHolidayLight4.display()
  myHolidayLight5.drive()
  myHolidayLight5.display()
  myHolidayLight6.drive()
  myHolidayLight6.display()
  for i in wreaths:
      i.display()
  if (wreathType == 0):
      instruction = "Happy Holidays, it's time to decorate! Click your mouse wherever you'd like to create some greenery - try creating a Christmas wreath!"
  text(instruction, 100, 400, 180, 500)
#A problem I had is positioning the text where I want it. I don't understand why it moves after the first time the user clicks the mouse. I did look up the syntax for text() at https://processing.org/reference/text_.html
    
    
