from dataclasses import dataclass

from .color import Color
from .point import Point


@dataclass
class Triangle:
    '''
    Хранит информацию о трегуольнике.
    '''

    color: Color
    a: Point
    b: Point
    c: Point

    @staticmethod
    def read(buffer) -> 'Triangle':
        color = Color.read(buffer)
        buffer.skip_whitespaces()
        a = Point.read(buffer)
        buffer.skip_whitespaces()
        b = Point.read(buffer)
        buffer.skip_whitespaces()
        c = Point.read(buffer)
        return Triangle(color, a, b, c)

    def perimiter(self):
        return (self.a.distance(self.b)
                + self.b.distance(self.c)
                + self.c.distance(self.a))

    def __str__(self) -> str:
        return (f'Triangle: color={self.color}, '
                f'points={self.a} - {self.b} - {self.c}')
