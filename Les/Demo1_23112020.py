#!/usr/bin/env python
"""
info about our project
"""

# import


__author__ = "Fre Van Buynder"
__email__ = "fre.vanbuynder@student.kdg.be"
__status__ = "Development"


def main():
    name = input("What's your name?: ")
    if name == "Phineas":
        print("... and Ferb")
    else:
        print("Good morning", name, '!')


if __name__ == '__main__':
    main()
