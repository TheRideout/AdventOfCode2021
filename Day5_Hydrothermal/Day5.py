from collections import Counter


class Vent:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.diagonal = False
        self.points = self.calc_points()

    def calc_points(self):
        x1 = self.start[0]
        x2 = self.end[0]
        y1 = self.start[1]
        y2 = self.end[1]
        xrange = range(x1, x2 + 1) if x1 < x2 else range(x1, x2 - 1, -1)
        yrange = range(y1, y2 + 1) if y1 < y2 else range(y1, y2 - 1, -1)
        if x1 == x2:
            return [(x1, y) for y in yrange]
        if y1 == y2:
            return [(x, y1) for x in xrange]
        m = (y1 - y2) / (x1 - x2)
        b = (x1 * y2 - x2 * y1) / (x1 - x2)
        self.diagonal = True
        return [(x, int((m*x)+b)) for x in xrange]


def load_input(path):
    with open(path) as f:
        return [vent_from_string(x) for x in f.readlines()]


def vent_from_string(input):
    points = [tuple(map(int, point.split(','))) for point in input.strip().split(' -> ')]
    return Vent(points[0], points[1])


def main():
    vents = load_input('Input')

    hv_points = []
    for vent in vents:
        if not vent.diagonal:
            hv_points.extend(vent.points)
    print('Part 1: {v}'.format(v=len([v for k, v in Counter(hv_points).items() if v > 1])))

    all_points = []
    for vent in vents:
        all_points.extend(vent.points)
    print('Part 2: {v}'.format(v=len([v for k, v in Counter(all_points).items() if v > 1])))


if __name__ == '__main__':
    main()
