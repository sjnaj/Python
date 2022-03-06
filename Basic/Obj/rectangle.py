'''
Author: fengsc
Date: 2022-03-05 13:20:04
LastEditTime: 2022-03-05 14:13:56
'''
from geometricobject import Geometricobject


class Rectangle(Geometricobject):

    def __init__(self, width=0, height=0, color="white", filled=False) -> None:
        super().__init__(color, filled)
        self.width = width
        self.height = height

    @property
    def width(self) -> float:
        return self.__width

    @width.setter
    def width(self, width) -> None:
        if width >= 0:
            self.__width = width
        else:
            raise ValueError("width must be positive")

    @property
    def height(self) -> float:
        return self.__height

    @height.setter
    def height(self, height) -> None:
        if height >= 0:
            self.__height = height
        else:
            raise ValueError("height must be positive")
    @property
    def area(self) -> float:
        return self.__width*self.__height
    @property
    def perimeter(self) -> float:
        return 2*(self.__width+self.__height)

    def __repr__(self) -> str:
        return super().__repr__()+ " width is "+str(self.__width)+" height is "+str(self.__height)
