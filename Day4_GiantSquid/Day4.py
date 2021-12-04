class Board:
    def __init__(self, board_data=None):
        self.board_data = [[int(x) for x in y.strip().split(' ') if x != ''] for y in board_data if y != '\n']
        self.board_numbers = [num for row in self.board_data for num in row]
        self.played_numbers = []
        self.win = False
        self.winning_number = None
        self.score = None

    def play_number(self, number):
        if number in self.board_numbers:
            self.played_numbers.append(number)
            if not self.win:
                self.win = self.calc_win()
                if self.win:
                    self.score = self.calc_score()
                    self.winning_number = number

    def calc_win(self):
        for row in self.board_data:
            if all([x in self.played_numbers for x in row]):
                return True
        for i in range(5):
            if all([x in self.played_numbers for x in [row[i] for row in self.board_data]]):
                return True
        return False

    def calc_score(self):
        return sum([x for x in self.board_numbers if x not in self.played_numbers])


def load_input(path):
    with open(path) as f:
        lines = f.readlines()
        called_numbers = [int(x) for x in lines[0].strip().split(',')]
        board_splits = [i for i, v in enumerate(lines) if v == '\n']
        boards = [Board(lines[s:board_splits[i + 1]]) for i, s in enumerate(board_splits[:-1])]
        return called_numbers, boards


def play_full_game(numbers, boards):
    winning_boards = []
    for num in numbers:
        for board in boards:
            if not board.win:
                board.play_number(num)
                if board.win:
                    winning_boards.append(board)
    return winning_boards


def main():
    numbers, boards = load_input('Input')
    win_boards = play_full_game(numbers, boards)
    print('Part 1: {v}'.format(v=win_boards[0].winning_number * win_boards[0].score))
    print('Part 2: {v}'.format(v=win_boards[-1].winning_number * win_boards[-1].score))


if __name__ == '__main__':
    main()
