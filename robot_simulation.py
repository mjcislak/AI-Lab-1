from controller import RobotController
from math import pi
from math import cos
from math import sin
from math import sqrt
import turtle
from turtle import Screen
from mathFunctions import *

def main():
    
    #--------------------------------------OBSTACLE-SETUP---------------------------------#

    obstacles = [(-100,0),(-90,0),(-90,150),(-100,150),(100,0),(90,0),(90,150),(100,150), 
    (40,50),(-40,50),(-40,80),(40,80)]

    newObstacles = formatObstacles(obstacles)
    #---------------------------------------GET-POSITION----------------------------------#

    robotPos = (0,0)

    #---------------------------------------HISTORY STUFF---------------------------------#
    # Just for printing out at the end
    sensedPointsHist = []
    
    path = []
    
    controller = RobotController()
    #---------------------------------------ACTION LOOP---------------------------------#
    for i in range(1):

        # Get action
        action = controller.getAction()
        path.append(controller.getCurrentPosition())
      
        # Get scan of surroundings every 15 degrees
        detectedPoints = getDetectedPoints(controller.getCurrentPosition(), newObstacles, 15)
        controller.updateSurroundings(detectedPoints)
        sensedPointsHist += detectedPoints
    
    drawSimulation(obstacles, path, sensedPointsHist)
        
"""
Get points around current position every d degrees
"""
def getDetectedPoints(pos, obstacles, d):

    d = ((d * pi) / 180)

    degree = 0

    radius = 300

    angleList = []

    while degree <= (pi):

        xpos = radius * cos(degree) + pos[0]
        ypos = radius * sin(degree) + pos[1]

        x = getIntersectionFromClosestEdge(obstacles, ([pos[0],pos[1]], [xpos, ypos]))

        angleList.append(x)

        degree += d

    return angleList
    
"""
Move simulated robot in specified direction
"""
def moveRobot(move):

    robotPos[0] += move[0]
    robotPos[1] += move[1]
    # Return collision points (if n collision, return none)
    return None

"""
Draw simulation
"""
def drawSimulation(coordinates, path, detectedPoints, color = "red"):

    # screen = Screen()
    # screen.setworldcoordinates(-WIDTH/2, -HEIGHT/2, WIDTH//2, HEIGHT/2)

    myTurtle = turtle.Turtle()
    myTurtle.color(color)
    myTurtle.penup()

    #-------------------------------OBSTACLE--------------------------------------#
    counter = 0

    for coordinate in coordinates:
        
        counter = counter + 1
        
        myTurtle.goto(coordinate)

        
        if(counter % 4 == 0):
            
            myTurtle.goto(coordinates[(counter - 4)])
            myTurtle.penup()
        else:
            myTurtle.pendown()
    #----------------------------------PATH-----------------------------------#
    counter2 = 0
    
    for p in path:
        # counter2 = counter2 + 1
        myTurtle.goto(p)
        #if (counter2 % 2 == 0):
           # myTurtle.penup()
        myTurtle.pendown()
        myTurtle.circle(3)
        myTurtle.penup()
    #---------------------------------SURROUNDING-------------------------------#

    myTurtle.color("blue")

    print(str(detectedPoints))

    for coordinate in detectedPoints:

        if coordinate:
            myTurtle.penup()
            myTurtle.goto(coordinate)
            myTurtle.pendown()
            myTurtle.circle(1)


    turtle.done()

def formatObstacles(obstacles):

    formatted = []

    shift = 0

    counter = 0

    for i in range(len(obstacles)):

        if (counter % 4 == 0 and counter != 0):
            shift += 4

        # add to a small list 
        smallList = []
        
        smallList.append(obstacles[(i % 4) + shift])
        smallList.append(obstacles[((i + 1) % 4) + shift])

        # add small list to giant list 
        formatted.append(smallList) 

        counter += 1

    return formatted

if __name__ == "__main__":
    main()