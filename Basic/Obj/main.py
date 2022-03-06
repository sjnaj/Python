'''
Author: fengsc
Date: 2022-03-05 13:32:41
LastEditTime: 2022-03-05 14:28:40
'''
from circle import Circle
from rectangle import Rectangle


cir1 = Circle(10, color='red')

print(cir1.area)
print(cir1)
del cir1.radius
print(cir1.radius)

rec1 = Rectangle(5, 5, color="black")

print(rec1.area)
