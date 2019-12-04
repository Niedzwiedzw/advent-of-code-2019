from typing import List, Tuple

with open('./day_4/input_1.txt') as f:
    INPUT = map(int, f.read().split('-'))


def pairs(number: str) -> List[Tuple[str, str]]:
    return list(zip(number, number[1:]))


def test(number: int) -> bool:
    pairs_ = pairs(str(number))
    return any([a == b for (a, b) in pairs_]) and not any(a > b for (a, b) in pairs_)


def test_2(number: int) -> bool:
    number = str(number)
    for a, b in pairs(str(number)):
        if a == b and number.count(a) == 2:
            return True
    return False


def main():
    low, high = INPUT
    combinations = list(filter(test, range(low, high)))
    print('combinations:', len(combinations))
    after_hint = list(filter(test_2, combinations))
    print('after hint:', len(after_hint))


if __name__ == '__main__':
    main()
