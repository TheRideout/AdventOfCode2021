from collections import Counter


def load_input(path):
    with open(path) as f:
        return [[int(y) for y in x if y != '\n'] for x in f.readlines()]


def calc_gamma(data, length):
    gamma = []
    for x in range(length):
        gamma.append(get_most_common(get_column(data, x)))
    return int_array_to_binary(gamma)


def calc_epsilon(data, length):
    epsilon = []
    for x in range(length):
        epsilon.append(get_least_common(get_column(data, x)))
    return int_array_to_binary(epsilon)


def calc_oxygen(data, length):
    filtered = data
    for x in range(length):
        v = get_most_common(get_column(filtered, x))
        filtered = [d for d in filtered if d[x] == v]
    return int_array_to_binary(filtered[0])


def calc_co2(data, length):
    filtered = data
    for x in range(length):
        v = get_least_common(get_column(filtered, x))
        filtered = [d for d in filtered if d[x] == v]
    return int_array_to_binary(filtered[0])


def get_column(matrix, i):
    return [x[i] for x in matrix]


def get_most_common(data):
    c = Counter(data).most_common()
    return c[0][0] if c[0][1] > c[-1][1] else 1


def get_least_common(data):
    c = Counter(data).most_common()
    return c[-1][0] if c[-1][1] < c[0][1] else 0


def int_array_to_binary(array):
    str_array = [str(x) for x in array]
    return bin(int(''.join(str_array), 2))


def main():
    input = load_input('Input')
    print('Part 1: {v}'.format(v=int(calc_gamma(input, 12), 2) * int(calc_epsilon(input, 12), 2)))
    print('Part 2: {v}'.format(v=int(calc_oxygen(input, 12), 2) * int(calc_co2(input, 12), 2)))


if __name__ == '__main__':
    main()
