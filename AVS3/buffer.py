from typing import TextIO
from random import Random

from . import INT_MAX, INT_MIN, UINT_MAX, UINT_MIN


class Peakable:
    '''
    Класс, позволяющий делать операцию peek() над файлоподобным объектом
    '''

    def __init__(self, backing: TextIO) -> None:
        self.backing = backing  # Файлоподобный объект
        self._peek = None       # Значение, которое было считано из backing,
                                # но ещё не считано в read()

    def read(self) -> str:
        '''
        Считывает один символ из файла
        '''

        if self._peek:
            result = self._peek
            self._peek = None
            return result
        return self.backing.read(1)

    def peek(self):
        '''
        Возвращает символ, который вернёт следюущий вызов read()
        '''

        if not self._peek:
            self._peek = self.backing.read(1)
        return self._peek


class Stream:
    '''
    Реализует разбор данных из файлоподобного объекта
    '''

    def __init__(self, backing: TextIO) -> None:
        self.backing = Peakable(backing)
        self.mirror = None

    def read_uint(self, _min=UINT_MIN, _max=UINT_MAX) -> int:
        '''
        Считывает число без знака
        '''

        number = 0
        while True:
            char = self.backing.peek()
            if char.isdigit():
                number *= 10
                number += int(char)
                self.backing.read()
            else:
                if self.mirror:
                    self.mirror.write(str(number))
                return number

    def read_int(self, _min=INT_MIN, _max=INT_MAX) -> int:
        '''
        Считывает число со знаком
        '''

        sign = 1
        if self.backing.peek() == '-':
            self.backing.read()
            sign = -1
            if self.mirror:
                self.mirror.write('-')
        result = sign * self.read_uint()
        return result

    def skip_whitespaces(self):
        '''
        Пропускает все подряд идущие пробелы
        '''

        is_any = False
        while True:
            char = self.backing.peek()
            if char.isspace():
                self.backing.read()
                if self.mirror and char == '\n':
                    self.mirror.write('\n')
                is_any = True
            else:
                break
        if not is_any:
            raise Exception("Expected whitespace")
        if self.mirror:
            self.mirror.write(' ')


class Randomized:
    '''
    Генератор случайных данных
    '''

    def __init__(self, seed: int, mirror: TextIO = None) -> None:
        self.generator = Random(seed)
        self.mirror = mirror

    def read_uint(self, a=UINT_MIN, b=UINT_MAX) -> int:
        '''
        Генерирует и возвращает случайное число
        '''

        return self.read_int(a, b)

    def read_int(self, a=INT_MIN, b=INT_MAX) -> int:
        '''
        Генерирует и возвращает случайное число
        '''

        result = self.generator.randint(a, b)
        if self.mirror:
            self.mirror.write(str(result))
        return result

    def skip_whitespaces(self):
        if self.mirror:
            self.mirror.write(' ')
