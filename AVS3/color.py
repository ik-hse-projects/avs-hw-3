from enum import IntEnum
from typing import TextIO

class Color(IntEnum):
    '''
    Перечисление, хранит информацию об цвете фигур
    '''

    RED = 0,
    ORANGE = 1,
    YELLOW = 2,
    GREEN = 3,
    LIGHT_BLUE = 4,
    BLUE = 5,
    PURPLE = 6,

    @staticmethod
    def read(buffer) -> 'Color':
        num = buffer.read_uint(0, 6)
        return Color(num)

    def __str__(self) -> str:
        return self.name.lower()
