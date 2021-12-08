def load_input(path):
    with open(path) as f:
        all_digits = []
        all_segments = []
        for line in f.readlines():
            segments, digits = line.split(' | ')
            all_digits.append([digit.strip() for digit in digits.split(' ')])
            all_segments.append([seg.strip() for seg in segments.split(' ')])
        return all_segments, all_digits


def decode_segments(segments):
    decoded = {}
    decoded[1] = [x for x in segments if len(x) == 2][0]  # Unique segment length numbers are known
    decoded[7] = [x for x in segments if len(x) == 3][0]
    decoded[4] = [x for x in segments if len(x) == 4][0]
    decoded[8] = [x for x in segments if len(x) == 7][0]
    len5 = [x for x in segments if len(x) == 5]  # Can be 2,3,5
    len6 = [x for x in segments if len(x) == 6]  # Can be 0,6,9

    decoded[3] = [x for x in len5 if len(remove_chars(x, decoded[1])) == 3][0]  # 3 has exactly 3 segments when removing the segments of 1
    len5.remove(decoded[3])

    decoded[9] = [x for x in len6 if len(remove_chars(x, decoded[3])) == 1][0]  # 9 has exactly 1 segment when removing the segments of 3
    len6.remove(decoded[9])

    decoded[2] = [x for x in len5 if remove_chars(decoded[8], decoded[9]) in x][0]  # 2 contains segment 'e' which is the difference between 8 and 9
    len5.remove(decoded[2])

    decoded[5] = len5[0]  # 5 is the last remaining choice for len5

    decoded[0] = [x for x in len6 if contains_all(x, decoded[1])][0]  # 0 is the only remaining option that contains all segments from 1
    len6.remove(decoded[0])

    decoded[6] = len6[0]  # 6 is the last remaining choice for len6

    return {sort_string(v): k for k, v in decoded.items()}  # Reverse key, value from dict and sort new string key for easier use


def remove_chars(string, chars):
    return ''.join(c for c in string if c not in chars)


def sort_string(string):
    return str(''.join(sorted(string)))


def contains_all(string, chars):
    return all([c in string for c in chars])


def decode_digits(decoded, digits):
    return int(''.join([str(decoded[sort_string(d)]) for d in digits]))


def find_unique_count(digits):
    unique_segments = [2, 3, 4, 7]
    lengths = [len(x) for y in digits for x in y]
    return sum([lengths.count(x) for x in unique_segments])


def decode_data(segments, digits):
    return [decode_digits(decode_segments(segment), digit) for segment, digit in zip(segments, digits)]


def main():
    segments, digits = load_input('Input')
    print(F'Part1 : {find_unique_count(digits)}')
    print(F'Part2 : {sum(decode_data(segments, digits))}')


if __name__ == '__main__':
    main()
