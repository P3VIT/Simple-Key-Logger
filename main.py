from pynput import keyboard

from threading import Thread
from time import sleep
import sys

f = open("text_file.txt", "x")

# Define global variables
text = ""

def timer():
    sleep_duration = 5
    while sleep_duration > 0:
        sleep(1)
        sleep_duration -= 1
    sys.exit()

def main():
    timer_thread = Thread(target=timer)
    timer_thread.start()

    def on_press(key):
        global text, start_time
        try:
            key_char = '{0}'.format(key.char)
            if not timer_thread.is_alive():
                f.write(text)
                f.close()
                sys.exit()
            text += key_char

        except AttributeError:
            if not timer_thread.is_alive():
                f.write(text)
                f.close()
                sys.exit()

            special_key = '{0}'.format(key)

            if special_key == "Key.space":
                text += " "
            elif special_key == "Key.backspace":
                text = text[:-1]

    # Collect events until released
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

    # ...or, in a non-blocking fashion:
    listener = keyboard.Listener(on_press=on_press)
    listener.start()

if __name__ == "__main__":
    main()