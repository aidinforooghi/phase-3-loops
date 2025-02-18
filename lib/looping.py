#!/usr/bin/env python3


def happy_new_year():
    countdown = 10
    while countdown >= 1:
        print(countdown)
        countdown -= 1
    print("Happy New Year!")

happy_new_year()

def square_integers(numbers):
    squared_list = [num ** 2 for num in numbers]
    return squared_list

numbers = [1, 2, 3, 4, 5]
print(square_integers(numbers))

def fizzbuzz():
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

fizzbuzz()
