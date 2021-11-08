from dataclasses import dataclass
import sys

from .color import Color
from .shape import read_shape
from . import buffer, selection_sort_by_perimiter


def print_usage():
    '''
    Выводит справку об использовании программы
    '''

    print("Usage:")
    print("  default: read from Stream, write to stdout.")
    print("  -r <seed> to use random values")
    print("  -f <filename> to read from file")
    print("  -o <filename> to set output file")
    print("Input format:")
    print("  First line contains number of shapes.")
    print("  In the following lines shapes are entered.")
    print("  All values are separated using whitespace")
    print("Shapes:")
    print("  Circle:    `1 <color> <x> <y> <radius>`")
    print("  Rectangle: `2 <color> <x1> <y1> <x2> <y2>`")
    print("             where (x1, y1) is the left-upper corner")
    print("             and (x2, y2) is the bottom-left.")
    print("  Triangle:  `3 <color> <x1> <y1> <x2> <y2> <x3> <y3>")
    print("Colors:")
    for i, color in enumerate(Color):
        print(f'  {i}. {color}')


@dataclass
class Options:
    '''
    Хранит разобранные параметры программы
    '''
    mirror = None
    input = buffer.Stream(sys.stdin)
    output = sys.stdout


def parse_args() -> Options:
    '''
    Разбирает параметры программы
    '''

    result = Options()

    i = 1
    while i < len(sys.argv):
        option = sys.argv[i]
        i += 1

        if (option[0] != '-' or len(option) != 2):
            print("Invalid option: ", option, file=sys.stderr)
            exit(1)

        if option[1] == 'h':
            print_usage()
            exit(0)

        if i >= len(sys.argv):
            print(f"Expected argument after {option}")
            exit(1)
        argument = sys.argv[i]
        i += 1

        if option[1] == 'r':
            seed = int(argument)
            result.input = buffer.Randomized(seed)
        elif option[1] == 'm':
            result.mirror = open(argument, 'w')
        elif option[1] == 'f':
            in_file = open(argument, 'r')
            result.input = buffer.Stream(in_file)
        elif option[1] == 'o':
            result.output = open(argument, 'w')
    return result


def main():
    '''
    Точка входа
    '''

    options = parse_args()
    options.input.mirror = options.mirror

    n = options.input.read_uint(1, 30)
    options.input.skip_whitespaces()

    shapes = []
    for i in range(n):
        shape = read_shape(options.input)
        shapes.append(shape)
        options.input.skip_whitespaces()

    options.output.write(f'Count: {len(shapes)}\n')

    options.output.write(f'Data:\n')
    for i, shape in enumerate(shapes, 1):
        options.output.write(f'{i}. {shape}\n')

    selection_sort_by_perimiter(shapes)

    options.output.write(f'Sorted:\n')
    for i, shape in enumerate(shapes, 1):
        options.output.write(f'{i}. {shape}\n')


if __name__ == "__main__":
    main()
