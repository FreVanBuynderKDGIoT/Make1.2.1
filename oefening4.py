#!/usr/bin/env python
"""
Een python script dat de functie van een stopwatch heeft.
Gebruik hiervoor de functie 'time' (Koppelingen naar een externe site.).
"""

# imports
import time

__author__ = "Fre Van Buynder"
__email__ = "fre.vanbuynder@student.kdg.be"
__status__ = "Development"


# global vars


# functions


def main():
    input("Press enter to start the timer:")
    timer_start = time.time()
    input("Press enter to stop the timer")
    timer_stop = time.time()

    seconds = timer_stop - timer_start

    time_convert(seconds)


def time_convert(seconds):
    minutes = seconds // 60
    seconds = seconds % 60
    hours = minutes // 60
    minutes = minutes % 60
    print("Time elapsed = {0}:{1}:{2}".format(int(hours), int(minutes), seconds))


if __name__ == '__main__':
    main()
