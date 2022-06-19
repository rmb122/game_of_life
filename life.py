import typing
import enum
from random import randint


class LifeStatus(enum.Enum):
    ALIVE = 1
    DEAD = 0


class Life:
    _last_state: typing.List[typing.List[LifeStatus]]
    _state: typing.List[typing.List[LifeStatus]]
    _size_y: int
    _size_x: int

    def __init__(self, size_y=50, size_x=50):
        self._size_y = size_y
        self._size_x = size_x
        self._last_state = [[LifeStatus.DEAD for _ in range(self._size_x)] for __ in range(self._size_y)]
        self._state = [[LifeStatus.DEAD for _ in range(self._size_x)] for __ in range(self._size_y)]

    def random_gen(self, probability: float = 0.2) -> None:
        assert 1 > probability > 0
        precision = 100
        probability = int(probability * precision)

        self._state = [
            [
                LifeStatus.ALIVE if randint(0, precision) <= probability else LifeStatus.DEAD
                for _ in range(self._size_x)
            ] for __ in range(self._size_y)
        ]

    def _judge_one_cell(self, x, y) -> LifeStatus:
        count = 0

        for offset_y in [-1, 0, 1]:
            for offset_x in [-1, 0, 1]:
                if offset_x == 0 and offset_y == 0:
                    continue
                else:
                    if self._state[(y + offset_y) % self._size_y][(x + offset_x) % self._size_x] is LifeStatus.ALIVE:
                        count += 1

        match count:
            case 3:
                return LifeStatus.ALIVE
            case 2:
                return self._state[y][x]
            case _:
                return LifeStatus.DEAD

    def next_state(self) -> None:
        self._last_state = self._state
        self._state = [
            [
                self._judge_one_cell(x, y)
                for x in range(self._size_x)
            ] for y in range(self._size_y)
        ]

    def add_noise(self, probability: float = 0.001) -> None:
        assert 1 > probability > 0
        precision = 10000
        probability = int(probability * precision)

        self._state = [
            [
                LifeStatus.ALIVE
                if self._state[y][x] is LifeStatus.DEAD and randint(0, precision) <= probability
                else self._state[y][x]
                for x in range(self._size_x)
            ] for y in range(self._size_y)
        ]

    def get_current_state(self) -> typing.List[typing.List[LifeStatus]]:
        return self._state

    def get_state_diff(self) -> typing.List[typing.Tuple[int, int, LifeStatus]]:
        diffs = []
        for y in range(self._size_y):
            for x in range(self._size_x):
                if self._state[y][x] is not self._last_state[y][x]:
                    diffs.append((y, x, self._state[y][x]))
        return diffs
