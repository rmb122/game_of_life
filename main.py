from Life import Life
from time import sleep

if __name__ == "__main__":
    life = Life(100, 40)
    life.random_gen(20)

    while True:
        print("\033c")
        life.next_state()
        life.print()
        sleep(0.1)