#!/usr/bin/env python
"""
info about our project
"""

# import


__author__ = "Fre Van Buynder"
__email__ = "fre.vanbuynder@student.kdg.be"
__status__ = "Development"


def main():
    list_of_words = ["hi", "I", "am", "Fre", "how", "are", "You"]

    searching_word = input("Which word do  you want to find?: ")

    i = 0

    while i < len(list_of_words):
        if list_of_words[i] == searching_word:
            print("Found it!!!")
            break
        else:
            print("Your word is not in this list right now.")

        i += 1


if __name__ == '__main__':
    main()
