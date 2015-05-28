
import numpy as np

class Color:
    # HSV Values
    BLUE = (np.array([100, 50, 50]),
            np.array([120, 255, 255]),
            'blue')

    YELLOW = (np.array([20,100,100]),
              np.array([30,255,255]),
              'yellow')

    # RED is a bitch. It sits at the edge of the HSV cyliner - it has two ranges.
    RED = (np.array([0,100,100]),
           np.array([3,255,255]),
           'red',
           np.array([160,100,100]),
           np.array([179,255,255]))

class Shape:
    TRIANGLE = 1
    RECTANGLE = 2
    HEXAGON = 3
    CIRCLE = 4
    PENTAGON = 5
