def load_input(path):
    with open(path) as f:
        return [int(x) for x in f.readlines()]


def find_slopes(numbers):
    return [determine_change(x, numbers[i-1]) if i > 0 else None for i, x in enumerate(numbers)]


def determine_change(x, y):
    # Returns 1 for increase, 0 for same value and -1 for decrease
    return 1 if x > y else 0 if x == y else -1


def get_windowed_sums(numbers, window):
    sums = []
    for x in range(len(numbers)-window+1):
        sums.append(sum(numbers[x:x+window]))
    return sums


def main():
    puzzle_input = load_input('Input')

    slopes = find_slopes(puzzle_input)
    windowed_slopes = find_slopes(get_windowed_sums(puzzle_input, 3))

    print('Part 1: {v}'.format(v=slopes.count(1)))
    print('Part 2: {v}'.format(v=windowed_slopes.count(1)))


if __name__ == '__main__':
    main()
