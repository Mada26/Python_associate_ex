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

class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        #
        # Write code here
        #
        
        self.__lista__=[vertice1,vertice2,vertice3]

    def perimeter(self):
        #
        # Write code here
        #
        sum=0.0
        for i in self.__lista__:
            self.distanta=i.distance_from_point(i)
            sum+=self.distanta
        return sum

triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())
