from Life import Life
from time import sleep
from os import get_terminal_size


if __name__ == "__main__":
    size = get_terminal_size()
    width = size.columns
    hight = size.lines

    life = Life((width // 2), hight)
    life.random_gen(20)

    while True:
        print("\033c")
        life.print_state()
        life.add_noise()
        life.next_state()
        sleep(0.01)
