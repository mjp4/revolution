import random as random
import math as math

class Point():
    def __init__(self):
        self.latitude = 0
        self.longitude = 0


def generate_random_points(lowerLatitude, upperLatitude, lowerLongitude, upperLongitude, numberOfPoints):

    listOfPoints = []

    i  = 0

    while i < numberOfPoints:

        latitude = lowerLatitude + (upperLatitude - lowerLatitude) * random.random()
        longitude = lowerLongitude + (upperLongitude - lowerLongitude) * random.random()
        point = Point()
        point.latitude = latitude
        point.longitude = longitude
        print(point.latitude, point.longitude)
        listOfPoints.append(point)
        i = i + 1

    return listOfPoints


def generate_random_trajectory(start, end, numberOfPoints):
    
    distance = distance_between_points(start, end)
    
    if distance < 0.01:
        return []
    unitVector = [(end.latitude - start.latitude) / distance, (end.longitude - start.longitude) / distance]

    trayectory = []
    trayectory.append(start)
    step = distance / numberOfPoints

    i = 0
    while (i < numberOfPoints):
        point = Point()
        point.latitude = trayectory[-1].latitude + step * unitVector[0]
        point.longitude = trayectory[-1].longitude + step * unitVector[1]

        trayectory.append(point)
        i = i + 1

    
    return trayectory


def distance_between_points(a, b):

    return math.sqrt(math.pow(b.latitude - a.latitude, 2) + math.pow(b.longitude - a.longitude, 2))


#print(generate_random_points(49.764911, 59.714322, -6.577090, 0.140923, 1000))