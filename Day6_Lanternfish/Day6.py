from collections import Counter


def load_input(path):
    with open(path) as f:
        return [int(x) for x in f.readlines()[0].split(',')]


def simulate(fish_pool, days):
    fish_dict = Counter(fish_pool)
    for x in range(days):
        updated_fish = {}
        if 0 in fish_dict:
            updated_fish[6] = updated_fish[8] = fish_dict[0]
        for age in range(1, 9):
            if age in fish_dict:
                if age == 7 and 6 in updated_fish:
                    updated_fish[6] += fish_dict[age]
                else:
                    updated_fish[age-1] = fish_dict[age]
        fish_dict = updated_fish
    return sum(fish_dict.values())


def main():
    fish_pool = load_input('Input')
    print('Part 1: {v}'.format(v=simulate(fish_pool, 80)))
    print('Part 2: {v}'.format(v=simulate(fish_pool, 256)))


if __name__ == '__main__':
    main()
