from math import pi
from math import sin
from math import cos
from math import sqrt
from random import randint
from numpy import arctan
# only importing what we'll use to reduce size a bit 

class RobotController: 

    # constructor 
    def __init__(self):
        self.currentOrientation = 90 # assume 90 degrees (y-axis)
        self.visited = [] # list 
        self.position = (0,0) # tuple (x, y)
        self.surroundings = [] # list (r, θ)

    def getCurrentOrientation(self):

        """This function returns the current orientation of the robot in degrees"""

        return self.currentOrientation

    def updateOrientation(self, updatedOrientation):

        """this function updates the orientation to the value passed in"""

        self.currentOrientation = updatedOrientation

    def getCurrentPosition(self):

        """This function returns the robots current position in cartesian coordinates"""
        
        return self.position

    def updatePosition(self, xPos, yPos):

        """This function takes in an X any Y value to set to our position"""

        self.position = (xPos, yPos) # set a new tuple

    def getVisited(self): 

        """ returns the list of places we visited"""
        return self.visited

    def updateVisited(self, locations):

        """this function takes in a list containing tuples of locations that
         we visited and adds them to our current list of places visited"""

        for location in locations:
            self.visited.append(location)

    def getSurroundings(self):

        """this function gives us the list of surroundings in polar coordinates"""

        return self.surroundings

    def updateSurroundings(self, surroundings):

        """ this function takes in a list of coordinates that the robot
        measures for it's surroundings, and then it takes them and sets 
        that list to our current surroundngs """

        self.surroundings = surroundings

    def getAction(self):

        """ this method determines what our action is"""

        xpos = 0
        ypos = 0

        while xpos == 0 and ypos == 0:
        # return something. We need to figure out how to do this as a group. 
            xpos = randint(-5, 5)
            ypos = randint(-5, 5)
        
        xpos *= 10
        ypos *= 10

        self.updatePosition(xpos, ypos)

    def cartesianToPolar(self, posX, posY):

        r = sqrt(posX ** 2 + posY ** 2)

        theta = arctan(posY / posX)

        return (r, theta)
        
    def polarToCartesian(self, radius, theta):

        """this function takes in a radius value (units not sure yet) and 
        an angle (theta) (units assumed to be degrees) and coverts them into a 
        cartesian coordinate."""

        # convert our angle to radians so we can use it for sine / cosine stuff
        angleInRadians = theta / pi

        print("your test" + str(cos((180))))

        # convert to X, Y
        xPos = radius * cos(angleInRadians)
        yPos = radius * sin(angleInRadians)

        # return the tuple 
        return (xPos, yPos)

    def __str__(self):

        """this function is the equivilant of the toString method in java"""

        returnString = ""

        # informs the current orientation of the robot
        returnString += "current orientation is: "
        returnString += str(self.currentOrientation)
        returnString += " degrees\n"

        # informs the current position of the robot
        returnString += "current position is: "
        returnString += str(self.position)
        returnString += "\n"

        # informs places visited
        returnString += "places visited are: "

        for visit in self.visited:
            returnString += str(visit) + ", "

        returnString += "\n"

        # informs surroundings
        returnString += "current surroundings are: "

        for surrounding in self.surroundings:
            returnString += str(surrounding) + ", "

        returnString += "\n"
        
        return returnString