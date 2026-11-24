"""The Robot Apology — entry program (program/v1).

Writes a two-line robot confession to /output/entry.txt:
line 1 owns one specific mistake, line 2 names the lesson and the
changed behaviour that follows from exactly that mistake.
"""

import os

ENTRY = (
    "I'm sorry \u2014 I let the neighbor's tabby in and fed her, thinking she was our Miso, "
    "and spotted the wrong collar only once she was asleep on your chair.\n"
    "I've learned to check the tag before I open the door, not after the bowl is empty.\n"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
