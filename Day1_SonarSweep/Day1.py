def load_input(path):
    f = open(path)
    numbers = [int(x) for x in f.readlines()]
    f.close()
    return numbers


def find_increases(numbers):
    return [determine_change(x, numbers[i-1]) if i > 0 else None for i, x in enumerate(numbers)]


def determine_change(x, y):
    # Returns 1 for increase, 0 for same value and -1 for decrease
    return 1 if x > y else 0 if x == y else -1


def get_windowed_sums(numbers, window):
    sums = []
    for x in range(len(numbers)-window+1):
        sums.append(sum(numbers[x:x+window]))
    return sums


puzzle_input = load_input('Input')

#Part 1
increases = find_increases(puzzle_input)
print(increases.count(1))

#Part 2
sums = get_windowed_sums(puzzle_input, 3)
sum_increases = find_increases(sums)
print(sum_increases.count(1))
