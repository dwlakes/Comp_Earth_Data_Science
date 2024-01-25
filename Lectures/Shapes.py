import numpy as np
class Circle:

    pi = np.pi

    def __init__(self, r):
        self.r = r

    def area(self):
        return (1.0/2.0) * self.pi * self.r**2
    
    def circumference(self):
        return 2.0 * self.pi * self.r
    
    def __str__(self):
        info = 'radius: value ' + ('%1.4e' % float(self.r))
        return info

class Rectange:

    def __init__(self, width, length):
        self.width = width
        self.length = length

    def area(self):
        return self.width * self.length

    def area(self):
        return self.width * self.length
    
    def perimeter(self):
        return ((self.width * 2) + (self.length *2))
