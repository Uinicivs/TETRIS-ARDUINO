import os
import time
import pygame
import pyfirmata
from dotenv import load_dotenv

load_dotenv()


class Controller:
    def __init__(self):
        self.board = pyfirmata.Arduino(os.environ.get("ARDUINO_SERIALPORT"))
        self.input_pins = [int(os.environ.get("LEFT_KEY_PIN")),
                           int(os.environ.get("RIGHT_KEY_PIN")),
                           int(os.environ.get("DOWN_KEY_PIN")),
                           int(os.environ.get("ROTATE_KEY_PIN"))]

        self.input_states = {pin: False for pin in self.input_pins}
        self.last_event_times = {pin: 0 for pin in self.input_pins}

        self.it = pyfirmata.util.Iterator(self.board)
        self.it.start()

    def setup(self):
        for pin in self.input_pins:
            self.board.digital[pin].mode = pyfirmata.INPUT

    def loop(self):
        while True:
            if pygame.get_init():
                for pin in self.input_pins:
                    state = self.board.digital[pin].read()

                    if state != self.input_states[pin] and time.time() - self.last_event_times[pin] > 0.2:
                        self.input_states[pin] = state

                        if state == 1:
                            self.move(pin)
                            self.last_event_times[pin] = time.time()
            else:
                self.board.exit()

            time.sleep(0.05)

    def move(self, pin):
        if pin == 8:
            self.pygameEvent(pygame.K_LEFT)
        elif pin == 9:
            self.pygameEvent(pygame.K_RIGHT)
        elif pin == 10:
            self.pygameEvent(pygame.K_DOWN)
        elif pin == 11:
            self.pygameEvent(pygame.K_UP)

    def pygameEvent(self, key):
        event = pygame.event.Event(pygame.KEYDOWN, key=key)
        pygame.event.post(event)
