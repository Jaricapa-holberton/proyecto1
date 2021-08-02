#!/bin/python3

import math
import os
import random
import re
import sys


class Car:
    '''A class to represent a Car.'''
    def __init__(self, max_speed=0, unit_speed=""):
        '''
        Construct all the necessary attributes for the Car object.
        '''
        # Check for the correct input
        if type(max_speed) is not int:
            raise TypeError("size must be an integer")
        elif type(unit_speed) is not str:
            raise TypeError("unit must be an string")
        else:
            self.max_speed = max_speed
            self.unit_speed = unit_speed

        def __str__(self):
            """
            Print an string of a Car object.
            """

            rep_car = "Car with the maximum speed of" + " " + str(max_speed) + " " + str(unit_speed)
            return(rep_car)

class Boat:
    '''A class to represent a Boat.'''
    def __init__(self, max_speed=0, unit_speed="knots"):
        '''
        Construct all the necessary attributes for the Boat object.
        '''
        # Check if size is a correct input
        if type(max_speed) is not int:
            raise TypeError("size must be an integer")
        elif type(unit_speed) is not str:
            raise TypeError("unit must be an string")
        else:
            self.max_speed = max_speed
            self.unit_speed = unit_speed

        def __str__(self):
            """
            Print an string of a Boat object.
            """

            rep_boat = "Car with the maximum speed of" + " " + str(max_speed) + " " + str(unit_speed)
            return(rep_boat)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input())
    queries = []
    for _ in range(q):
        args = input().split()
        vehicle_type, params = args[0], args[1:]
        if vehicle_type == "car":
            max_speed, speed_unit = int(params[0]), params[1]
            vehicle = Car(max_speed, speed_unit)
        elif vehicle_type == "boat":
            max_speed = int(params[0])
            vehicle = Boat(max_speed)
        else:
            raise ValueError("invalid vehicle type")
        fptr.write("%s\n" % vehicle)
    fptr.close()