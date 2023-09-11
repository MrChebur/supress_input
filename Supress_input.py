import time
import pynput  # https://github.com/moses-palmer/pynput
from tqdm import tqdm


class SupressInput:
    def __init__(self):
        self.mouse_listener = pynput.mouse.Listener(suppress=True)
        self.keyboard_listener = pynput.keyboard.Listener(suppress=True)

    def disable(self):
        """Disable mouse and keyboard events"""
        self.mouse_listener.start()
        self.keyboard_listener.start()

    def enable(self):
        """Enable mouse and keyboard events"""
        self.mouse_listener.stop()
        self.keyboard_listener.stop()

    def for_seconds(self, seconds_to_sleep=10):
        """Suppress input for X seconds and print a message every second"""

        self.disable()
        print('Input disabled!')
        print(f'Sleeping {seconds_to_sleep} seconds...')

        bar_format = '{desc:<5.5}{percentage:3.0f}%|{bar:10}{r_bar}'

        for x in tqdm(
                range(1, seconds_to_sleep + 1),
                bar_format=bar_format):
            # print(f'Sleeping {x} of {seconds_to_sleep} seconds...')
            time.sleep(1)

        self.enable()
        print('Input enabled!')


if __name__ == '__main__':
    supress = SupressInput()
    supress.for_seconds(3)
