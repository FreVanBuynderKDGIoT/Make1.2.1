#!/usr/bin/env python
"""
info about our project
"""

# import


__author__ = "Fre Van Buynder"
__email__ = "fre.vanbuynder@student.kdg.be"
__status__ = "Development"


def main():
    counter = 1
    result = 0

    while counter <= 100:
        result += counter
        counter += 1

    print("the numbers 1 to 100 added by each other is:", result)


if __name__ == '__main__':
    main()
