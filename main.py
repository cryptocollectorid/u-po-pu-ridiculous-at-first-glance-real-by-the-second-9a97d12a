#!/usr/bin/env python3
"""Ridiculous at First Glance, Real by the Second — make.fun entry.

Writes one sentence (at most 200 characters) pitching a bizarre startup
idea that sounds absurd until you realise it would actually sell.
"""

import os

ENTRY = "We sell alien-abduction insurance for pets, because anxious owners pay $9 a month for a policy that has never paid out a single claim."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
