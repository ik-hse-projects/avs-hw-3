from dataclasses import dataclass
from math import pi

from .color import Color
from .point import Point

@dataclass
class Circle:
    '''
    Хранит информацию об окружности
    '''

    color: Color
    center: Point
    radius: int

    @staticmethod
    def read(buffer) -> 'Circle':
        color = Color.read(buffer)
        buffer.skip_whitespaces()
        center = Point.read(buffer)
        buffer.skip_whitespaces()
        radius = buffer.read_int()
        return Circle(color, center, radius)

    def perimiter(self):
        return 2 * pi * self.radius

    def __str__(self) -> str:
        return (f'Circle: color={self.color}, '
                f'center={self.center}, '
                f'radius={self.radius}')
