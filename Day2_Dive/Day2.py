def load_input(path):
    f = open(path)
    directions = [line_parse(x) for x in f.readlines()]
    f.close()
    return directions


def line_parse(line):
    x, y = line.split(' ')
    return [x[0], int(y)]


def basic_navigation(data):
    x = 0
    y = 0
    for k, v in data:
        if k == 'f':
            x += v
        if k == 'd':
            y += v
        if k == 'u':
            y -= v
    return x, y


def aim_navigation(data):
    aim = 0
    x = 0
    y = 0
    for k, v in data:
        if k == 'f':
            x += v
            y += (aim * v)
        if k == 'd':
            aim += v
        if k == 'u':
            aim -= v
    return x, y


data = load_input('Input')

# Part 1
x, y = basic_navigation(data)
print(x * y)

# Part 2
xa, ya = aim_navigation(data)
print(xa * ya)
