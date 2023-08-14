from tetris_game import Tetris
from arduino import Controller
import threading
import time


def initialize_package1():
    mytetris = Tetris()
    mytetris.run()


def initialize_package2():
    mycontroller = Controller()
    mycontroller.setup()
    mycontroller.loop()


if __name__ == "__main__":
    thread1 = threading.Thread(target=initialize_package1)
    thread2 = threading.Thread(target=initialize_package2)

    thread2.start()
    time.sleep(1.5)
    thread1.start()

    thread2.join()
    thread1.join()

    print("Both packages initialized.")
