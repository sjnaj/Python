'''
Author: fengsc
Date: 2022-03-05 11:52:56
LastEditTime: 2022-03-05 14:08:47
'''
import datetime


class Geometricobject:

    def __init__(self, color="white", filled=False) -> None:# 不支持重载，使用默认参数
        self.__color = color
        self.__filled = filled
        self.__date_created = datetime.datetime.now()

    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, color) -> None:
        self.__color = color

    @property
    def filled(self) -> bool:
        return self.__filled

    @filled.setter
    def filled(self, filled) -> None:
        self.__filled = filled

    @property
    def date_created(self) -> datetime.datetime:
        return self.__date_created

    def __repr__(self) -> str:
        return "created on "+str(self.__date_created)+"\ncolor: "+str(self.__color)+" and filled: "+str(self.__filled)