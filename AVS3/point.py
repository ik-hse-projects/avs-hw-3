from dataclasses import dataclass
from math import sqrt

@dataclass
class Point:
    '''
    Хранит информацию о точке на плоскости
    '''

    x: int
    y: int

    @staticmethod
    def read(buffer) -> 'Point':
        x = buffer.read_uint()
        buffer.skip_whitespaces()
        y = buffer.read_uint()
        return Point(x, y)

    def distance(self, other):
        dx = other.x - self.x
        dy = other.y - self.y
        return sqrt(dx*dx + dy*dy)

    def __str__(self) -> str:
        return f'({self.x}, {self.y})'
