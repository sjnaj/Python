'''
Author: fengsc
Date: 2022-03-05 12:23:33
LastEditTime: 2022-03-05 14:32:24
'''
import math
from geometricobject import Geometricobject


class Circle(Geometricobject):
    def __init__(self, radius=0, color="white", filled=False) -> None:
        super().__init__(color, filled)
        self.radius = radius  # *调用radius.setter进行范围检查

    @property
    def radius(self) -> float:
        return self.__radius

    @radius.setter
    def radius(self, radius) -> None:
        if radius >= 0:
            self.__radius = radius
        else:
            raise ValueError("radius must be positive")

    @radius.deleter
    def radius(self) -> None:
        self.__radius = 0

    @property
    def area(self) -> float:
        return self.__radius*self.__radius*math.pi

    @property
    def perimeter(self) -> float:
        return self.__radius*math.pi*2

    def __repr__(self) -> str:
        return super().__repr__()+" and radius is "+str(self.__radius)
