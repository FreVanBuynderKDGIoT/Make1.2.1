#!/usr/bin/env python
"""
info about project
"""

# imports


__author__ = "Fre Van Buynder"
__email__ = "fre.vanbuynder@student.kdg.be"
__status__ = "Development"


# functions
def main():
    word = input("Give me a random word (the more random the better): ")
    print("the word exist of", len(word), "letters")


if __name__ == '__main__':
    main()
