#!/usr/bin/env python3

# Created by: RJ Fromm
# Created on: Dec 2019
# This is a program that finds the largest number in a list

import random


def largest_number(numbers):
    # This is finds largest number in a list

    last_number = 0

    for number in numbers:
        if number > last_number:
            largest = number
            last_number = number

    return largest


def main():
    # This is generate 10 random numbers

    largest = 0

    numbers = []

    # process
    for repeater in range(0, 10):
        number = random.randint(0, 100)
        numbers.append(number)
        # output
        print(numbers[repeater])

    largest = largest_number(numbers)

    # output
    print("The largest is " + str(largest))


if __name__ == "__main__":
    main()
