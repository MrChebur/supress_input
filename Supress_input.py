import time
import pynput  # https://github.com/moses-palmer/pynput
from tqdm import tqdm


class SupressInput:
    def __init__(self):
        self.mouse_listener = pynput.mouse.Listener(suppress=True)
        self.keyboard_listener = pynput.keyboard.Listener(suppress=True)

    def disable_all(self):
        """Disable mouse and keyboard events"""
        self.mouse_listener.start()
        self.keyboard_listener.start()

    def enable_all(self):
        """Enable mouse and keyboard events"""
        self.mouse_listener.stop()
        self.keyboard_listener.stop()

    def wait(self, seconds_to_sleep=10):
        """Suppress input for X seconds"""

        self.disable_all()
        print('Input disabled!')
        print(f'Sleeping {seconds_to_sleep} seconds...')

        for x in tqdm(range(1, seconds_to_sleep + 1)):
            time.sleep(1)

        self.enable_all()
        print('Input enabled!')


if __name__ == '__main__':
    supress_input = SupressInput()
    supress_input.wait(3)
