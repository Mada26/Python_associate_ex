import math


class Point:
    def __init__(self, x=0.0, y=0.0):
        #
        # Write code here
        #
        self.x=x
        self.y=y

    def getx(self):
        #
        # Write code here
        #
        return self.x
        

    def gety(self):
        #
        # Write code here
        #
        return self.y
        
    def distance_from_xy(self, x, y):
        #
        # Write code here
        #
        return math.hypot(self.x,self.y)
        
    def distance_from_point(self, point):
        #
        # Write code here
        #
        self.point=point
        x=self.point.x
        y=self.point.y
        return math.hypot(x,y)

point1 = Point(0, 1)
point2 = Point(1, 0)
print(point1.distance_from_point(point1))
print(point2.getx())
