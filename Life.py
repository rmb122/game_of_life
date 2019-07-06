from random import randint


class Life:
    def __init__(self, size_x=50, size_y=50):
        self.state = [[0 for _ in range(size_x)] for __ in range(size_y)]
        self.size_y = size_y
        self.size_x = size_x

    def random_gen(self, probability=20):
        assert 100 > probability > 0

        for y in range(len(self.state)):
            for x in range(len(self.state[y])):
                self.state[y][x] = (lambda: 1 if randint(0, 100) <= probability else 0)()

    def judge_one_cell(self, x, y):
        count = 0

        for offset_y in [-1, 0, 1]:
            for offset_x in [-1, 0, 1]:
                if offset_x == 0 and offset_y == 0:
                    continue
                else:
                    if self.state[(y + offset_y) % self.size_y][(x + offset_x) % self.size_x]:
                        count += 1

        if count == 3:
            return 1
        elif count == 2:
            return self.state[y][x]
        else:
            return 0

    def next_state(self):
        tmp = [[0 for _ in range(self.size_x)] for __ in range(self.size_y)]
        for y in range(len(self.state)):
            for x in range(len(self.state[y])):
                tmp[y][x] = self.judge_one_cell(x, y)
        self.state = tmp

    def print(self, alive='█', died=' '):
        for y in range(len(self.state)):
            for x in range(len(self.state[y])):
                if self.state[y][x]:
                    print(alive, end='')
                else:
                    print(died, end='')
            print('')
