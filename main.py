import atexit
import curses
import enum
import sys
import time
from os import get_terminal_size

from life import Life, LifeStatus

COLOR_PAIR_WHILE = 1
COLOR_PAIR_BLACK = 2
BLANK = '  '
SLEEP_TIME = 0
MUTATION = True


class ControlKeys(enum.Enum):
    QUIT_KEY = ord('q')
    FASTER_KEY = ord('x')
    SLOWER_KEY = ord('z')
    MUTATION_SWITCH = ord('m')


def exit_handler():
    curses.endwin()


atexit.register(exit_handler)


def init_window(window):
    size = get_terminal_size()
    width = size.columns
    height = size.lines

    life = Life(height, (width // len(BLANK)) - 1)
    life.random_gen(0.2)
    window.resize(height, width)
    return life


if __name__ == "__main__":
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    curses.start_color()

    stdscr.keypad(True)
    stdscr.nodelay(True)
    curses.curs_set(False)

    curses.init_pair(COLOR_PAIR_WHILE, curses.COLOR_WHITE, curses.COLOR_WHITE)
    curses.init_pair(COLOR_PAIR_BLACK, curses.COLOR_BLACK, curses.COLOR_BLACK)

    window = curses.newwin(0, 0, 0, 0)
    life = init_window(window)

    while True:
        if MUTATION:
            life.add_noise(0.0001)
        life.next_state()

        for diff in life.get_state_diff():
            window.addstr(
                diff[0],
                diff[1] * len(BLANK),
                BLANK,
                curses.color_pair(COLOR_PAIR_WHILE if diff[2] is LifeStatus.ALIVE else COLOR_PAIR_BLACK)
            )

        window.refresh()
        time.sleep(SLEEP_TIME)

        key = stdscr.getch()
        match key:
            case curses.KEY_RESIZE:
                life = init_window(window)
                window.clear()
            case ControlKeys.FASTER_KEY.value:
                if SLEEP_TIME - 0.1 >= 0:
                    SLEEP_TIME -= 0.1
            case ControlKeys.SLOWER_KEY.value:
                SLEEP_TIME += 0.1
            case ControlKeys.QUIT_KEY.value:
                sys.exit(0)
            case ControlKeys.MUTATION_SWITCH.value:
                MUTATION = not MUTATION
