from dataclasses import dataclass

from .color import Color
from .point import Point


@dataclass
class Rectangle:
    '''
    Хранит информацию о прямоугольнике
    '''

    color: Color
    left_top: Point
    right_bottom: Point

    @staticmethod
    def read(buffer) -> 'Rectangle':
        color = Color.read(buffer)
        buffer.skip_whitespaces()
        left_top = Point.read(buffer)
        buffer.skip_whitespaces()
        right_bottom = Point.read(buffer)
        return Rectangle(color, left_top, right_bottom)

    def perimiter(self):
        height = self.right_bottom.y - self.left_top.y
        width = self.right_bottom.x - self.left_top.x
        return 2*(height + width)

    def __str__(self) -> str:
        return (f'Rectangle: color={self.color}, '
                f'top-left={self.left_top}, '
                f'bottom-right={self.right_bottom}')
