from gopigo import *
import sys

    print("press enter to start")

    raw_input()

    stop_distance = 20

    fwd()

    while True:

        dist = us_dist(15)

        print("dist ", dist, "cm")

        if dist < stop_distance:

            print("stopping")

            stop()

            break

        time.sleep(.1)