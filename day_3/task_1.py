from typing import List, Iterable

with open('./day_3/input_1.txt') as f:
    INPUT = list(filter(bool, f.readlines()))
    WIRE_1, WIRE_2 = INPUT
    WIRE_1 = list(map(lambda e: e.strip(), WIRE_1.split(',')))
    WIRE_2 = list(map(lambda e: e.strip(), WIRE_2.split(',')))

DIRECTION_MAPPING = {
    'U': (0, 1),
    'D': (0, -1),
    'L': (-1, 0),
    'R': (1, 0),
}


class Position:
    DIRECTION_MAPPING = {
        'U': (0, 1),
        'D': (0, -1),
        'L': (-1, 0),
        'R': (1, 0),
    }

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def moved_by(self, direction: str, distance: int) -> Iterable['Position']:
        x, y = self.DIRECTION_MAPPING[direction]
        if x:
            for i in range(self.x+x, distance+x, x):
                yield Position(i, self.y)

        elif y:
            for i in range(self.y+y, distance+y, y):
                yield Position(self.x, i)

    def __str__(self):
        return f'[x:{self.x},y:{self.y}]'

    def __repr__(self):
        return str(self)

    def __hash__(self):
        return hash(f'{self.x},{self.y}')

    def __eq__(self, other: 'Position'):
        return hash(self) == hash(other)


class Wire:
    def __init__(self, path):
        self.positions: List[Position] = [Position(0, 0)]
        self.path: List[str] = path

        for direction, distance in map(lambda p: (str(p[0]), int(p[1:])), self.path):
            self.add_moved_by(direction, distance)

    def add_moved_by(self, direction: str, distance: int):
        x, y = DIRECTION_MAPPING[direction]
        if x:
            for i in range(distance):
                last = self.positions[-1]
                self.positions.append(Position(last.x + x, last.y))

        if y:
            for i in range(distance):
                last = self.positions[-1]
                self.positions.append(Position(last.x, last.y+y))

    def __str__(self):
        return str(self.positions)


def main():
    wire_1 = Wire(WIRE_1)
    wire_2 = Wire(WIRE_2)

    common = (set(wire_1.positions) & set(wire_2.positions)) - {Position(0, 0)}
    minimal = min(map(lambda d: abs(d.x) + abs(d.y), common))
    print('closest intesection:', minimal)

    effort_intersections = [sum((wire_1.positions.index(i), wire_2.positions.index(i))) for i in common]

    print('least effort intersection:', min(effort_intersections))


if __name__ == '__main__':
    main()
