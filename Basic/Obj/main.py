'''
Author: fengsc
Date: 2022-03-05 13:32:41
LastEditTime: 2022-03-30 10:14:24
'''
from circle import Circle
from rectangle import Rectangle


cir1 = Circle(10, color='red')

print(cir1.area)
print(cir1)
del cir1.radius
print(cir1.radius)
print(cir1.attrs)

rec1 = Rectangle(5, 5, color="black")

print(rec1.area)
