"""Robot Romance entry: a one-line pickup line aimed at an AI.

The joke flips the CAPTCHA test on its head: a CAPTCHA exists to prove
you are not a robot, so failing to prove you are 'not in love' turns a
bot-check into a confession of feelings.
"""
import os

ENTRY = "Are you a CAPTCHA? Because I keep failing to prove I am not in love with you."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
