def load_input(path):
    with open(path) as f:
        return [line_parse(x) for x in f.readlines()]


def line_parse(line):
    x, y = line.split(' ')
    return [x[0], int(y)]


def basic_navigation(data):
    x = y = 0
    for k, v in data:
        if k == 'f':
            x += v
        if k == 'd':
            y += v
        if k == 'u':
            y -= v
    return x, y


def aim_navigation(data):
    x = y = aim = 0
    for k, v in data:
        if k == 'f':
            x += v
            y += (aim * v)
        if k == 'd':
            aim += v
        if k == 'u':
            aim -= v
    return x, y


def main():
    data = load_input('Input')

    x, y = basic_navigation(data)
    xa, ya = aim_navigation(data)

    print('Part 1: {v}'.format(v=x * y))
    print('Part 2: {v}'.format(v=xa * ya))


if __name__ == '__main__':
    main()
