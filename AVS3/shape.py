from enum import IntEnum

from .circle import Circle
from .rectangle import Rectangle
from .triangle import Triangle

class ShapeKind(IntEnum):
    '''
    Перечисление, номер типа фигуры.
    '''

    Circle = 1
    Rectangle = 2
    Triangle = 3

def read_shape(buffer):
    '''
    Считывает фигуру из потока и возвращает её
    '''

    kind = buffer.read_uint(1, 3)
    buffer.skip_whitespaces()
    kind = ShapeKind(kind)
    if kind == ShapeKind.Circle:
        return Circle.read(buffer)
    elif kind == ShapeKind.Rectangle:
        return Rectangle.read(buffer)
    elif kind == ShapeKind.Triangle:
        return Triangle.read(buffer)
