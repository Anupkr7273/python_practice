import math
def circle_stats(rad):
    area= math.pi * rad**2
    circum=2*math.pi*rad
    return area,circum
a,c=circle_stats(4)
print("Area=",a,"circumference",c)