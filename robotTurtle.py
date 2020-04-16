# import turtle
# from turtle import Screen

# WIDTH, HEIGHT = 28, 28  # coordinate system size
# # points to draw, will draw a line from 5,5 to 0,0 then a new line at next pairs

# turt = turtle.Turtle()

# def main():
#     screen = Screen()
#     screen.setworldcoordinates(-WIDTH/2, -HEIGHT/2, WIDTH//2, HEIGHT/2)

#     #turt.speed('fastest')
#     turt.penup()

#     # X AXIS
#     axis(turt, WIDTH, 1)
    
#     turt.penup()
#     turt.home()
#     turt.setheading(90)


#     # Y AXIS
#     axis(turt, HEIGHT, 1)

#    # drawPath(turt, points)
#     #drawObstacle(turt, obstacle)
#     pathPoints = ((0,0), (4,4), (-4,4), (9,9))
#     obstacle = ((2, 2), (-2, 2), (-2, -2), (2, -2), (5, 5), (-5, 5), (-5, -5), (5, -5), (6, 6), (6, -6), (9, -6), (9, 6))
#     point = ((-3, -3), (-1, -1))
#     drawPath(pathPoints)
#     drawObstacle(obstacle)
#     drawPoints(point)
#     screen.exitonclick()

#     turtle.done

# # for path (green)
# def drawPath(coordinates, color="green"):
    
#     # goes to x1,y2 to x2,y2
#     # then resets go home 
    
#     myTurtle = turtle.Turtle()
#     myTurtle.color(color)
#     myTurtle.penup
#     counter = 0
#     for coordinate in coordinates:
#         counter = counter + 1
#         myTurtle.goto(coordinate)
#         if (counter % 2 == 0):
#             myTurtle.penup()
             
#         myTurtle.pendown()

# # draw obstacles black
# def drawObstacle(coordinates, color="black"):
#     myTurtle = turtle.Turtle()
#     myTurtle.color(color)
#     myTurtle.penup()

#     counter = 0

#     for coordinate in coordinates:
        
#         counter = counter + 1
        
#         myTurtle.goto(coordinate)

        
#         if(counter % 4 == 0):
            
#             myTurtle.goto(coordinates[(counter - 4)])
#             myTurtle.penup()
#         else:
#             myTurtle.pendown()

# # draw red points
# def drawPoints(coordinates, color="red"):
#     myTurtle = turtle.Turtle()
#     myTurtle.color(color)

#     for coordinate in coordinates:
#         myTurtle.penup()
#         myTurtle.goto(coordinate)
#         myTurtle.pendown()
#         myTurtle.dot()

# #draw Axis
# def axis(turtle, distance, tick):
#     position = turtle.position()
#     turtle.pendown()

#     for _ in range(0, distance // 2, tick):
#         turtle.forward(tick)
#         turtle.dot()

#     turtle.setposition(position)

#     for _ in range(0, distance // 2, tick):
#         turtle.backward(tick)
#         turtle.dot()


# main()



