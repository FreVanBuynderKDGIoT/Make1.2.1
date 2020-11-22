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
    programmed_list  = ["een", "twee", "drie", "vier', 'vijf"]
    print(programmed_list)

    random_list = list(map(str, input("Enter multiple words: ").split()))
    print(random_list)

if __name__ == '__main__':
    main()
