from Life import Life
from time import sleep

if __name__ == "__main__":
    life = Life(200, 80)
    life.random_gen(20)

    while True:
        print("\033c")
        life.print_state()
        life.add_noise()
        life.next_state()
