#!/usr/bin/env python
"""
info about our project
"""

# import


__author__ = "Fre Van Buynder"
__email__ = "fre.vanbuynder@student.kdg.be"
__status__ = "Development"

import random

c = 0


def main():
    global c
    random_number = random.randint(1, 10)

    print("het random gegeneerde getal is:", random_number)

    for number in range(random_number):
        c += 1
        print("de teller staat op:", c)


if __name__ == '__main__':
    main()
