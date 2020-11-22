#!/usr/bin/env python
"""
Een python script dat het volgende doet:
vraagt achter je leeftijd
berekent in welk jaar je geboren bent en dat ook als output meegeeft
berekent in welk jaar je 50 jaar zal zijn en dat ook als output meegeeft
"""

# imports
from _datetime import datetime

__author__ = "Fre Van Buynder"
__email__ = "fre.vanbuynder@student.kdg.be"
__status__ = "Development"


# functions
def main():
    age = int(input("What's your age? (I know it's a rude question): "))
    today = datetime.now()
    year = int(today.year)

    birth_year = year - age
    if age <= 50:
        fifty_year = year + (50 - age)
        print("You are born in: ", birth_year, " and you will be 50 in the year: ", fifty_year)
    elif age > 50:
        fifty_year = year - (50 + age)
        print("You are born in: ", birth_year, " and you were 50 in the year: ", fifty_year)

if __name__ == '__main__':
    main()