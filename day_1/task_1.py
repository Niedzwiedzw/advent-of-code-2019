def fuel(mass: int) -> int:
    return max(mass // 3 - 2, 0)


def fuelnacci(mass: int) -> int:
    if mass <= 0:
        return mass
    return fuel(mass) + fuelnacci(fuel(mass))


def main():
    with open('day_1/input_1.txt') as f:
        data = list(map(int, [l.strip() for l in f.readlines()]))

    module_fuel = sum(map(fuel, data))
    print(f'module fuel: {module_fuel}')

    # task 2
    overall = sum(map(fuelnacci, data))
    print('overall: ', overall)


if __name__ == '__main__':
    main()
