from copy import copy
from typing import List

with open('./day_2/input_1.txt') as f:
    INPUT = list(map(int, f.read().split(',')))


def exit_(*args):
    raise SystemExit("")


def mult(x: int, y: int) -> int:
    return x * y


def add(x: int, y: int) -> int:
    return x + y


class IntCodeComputer:
    INSTRUCTIONS = {
        1: add,
        2: lambda x, y: x * y,
        99: exit_,
    }

    def __init__(self, memory):
        self.cursor = 0
        self.memory: List[int] = copy(memory)

    def next_instruction(self) -> [int, int, int, int]:
        instruction = []
        for i in range(4):
            instruction.append(self.memory[self.cursor])
            self.cursor += 1

        return instruction

    def execute(self, instruction: [int, int, int, int]):
        command, in_1, in_2, out = instruction
        val = self.INSTRUCTIONS[command](
            self.memory[in_1],
            self.memory[in_2]
        )
        self.memory[out] = val

    def run(self) -> List[int]:
        while True:
            try:
                self.execute(self.next_instruction())
            except SystemExit:
                return self.memory


def mock_input(noun: int, verb: int) -> List[str]:
    data = copy(INPUT)
    data[1] = noun
    data[2] = verb
    return data


def main():
    # part 1
    computer = IntCodeComputer(INPUT)
    print(computer.run())

    # part 2
    for noun in range(99):
        for verb in range(99):
            out = IntCodeComputer(mock_input(noun, verb)).run()
            if out[0] == 19690720:
                print(f'{noun}{verb}')
                return


if __name__ == '__main__':
    main()
