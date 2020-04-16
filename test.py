
from controller import RobotController
from math import pi
def main():
    
    controller = RobotController();

    controller.updateSurroundings([(10, 180)])
    controller.updatePosition(5, 0)
    controller.updateVisited([(5, 0)])

    print(str(controller.polarToCartesian(1, pi / 2)))

    print(controller)
  



if __name__ == "__main__":
    main()





