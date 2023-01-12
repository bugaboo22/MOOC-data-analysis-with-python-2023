# Enter you module contents here
import math
__doc__ = "This module provides basic operations for triangles."
__author__ = "Lauri Vastela"
__version__ = "1.0.1"

def hypothenuse(a, b):

    ''' Hypothenuse of a triangle'''
    return math.hypot(a, b)

def area(a,b): 

    ''' Area of two sided triangle '''
    area = ( a * b ) / 2  
    return area
