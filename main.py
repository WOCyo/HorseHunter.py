import pyperclip
import random
import time

if __name__ == "__main__":

    with open("resources.txt", "r", encoding="utf-8") as resources:
        lines = resources.readlines()

    print(f"Random selecting from total {len(lines)} lines, every 0.1s.")

    while True:
        pyperclip.copy(random.choice(lines))
        time.sleep(0.1)
