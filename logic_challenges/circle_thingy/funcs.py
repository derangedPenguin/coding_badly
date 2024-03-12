import numpy as np
import math
import random
import pygame

def fast_distance(points):
    '''
    Returns square of the distance between two points
    Squared to avoid using sqrt because slow
    Meant for use in comparison with other fast_distances
    '''
    return (points[0][0]-points[1][0])**2 + (points[0][1]-points[1][1])**2
def distance(points):
    '''
    Returns the distance between two points
    '''
    return math.sqrt((points[0][0]-points[1][0])**2 + (points[0][1]-points[1][1])**2)

def rand_point_on_line(line):
    percent_along = random.random()
    return ((line[0][0] - line[1][0])*percent_along)+line[0][0], ((line[0][1] - line[1][1])*percent_along)+line[0][0]

def far_points_on_poly(polygon, min_dist, max_attempts=20):
    '''
    randomly generate two points on the edges of a polygon
    points will never be on the same edge
    creates points until distance between them is greater than min_dist,
    or until max_attempts is reached, then returns best result
    '''
    i = 0
    attempts = {}
    while True:
        i += 1
        #pick random points
        lines = [[polygon[i], polygon[(i+1)%len(polygon)]] for i in range(len(polygon))]
        line1 = lines.pop(random.randint(0,len(polygon)-1))
        line2 = random.choice(lines)
        points = rand_point_on_line(line1), rand_point_on_line(line2)
        #is points are far enough apart, return, else log and try again
        if dist := fast_distance(points) > min_dist:
            return points
        else:
            attempts[dist] = points
        #if tried too many times, return best
        if i >= max_attempts:
            return attempts[max(attempts.keys())]