#!/usr/bin/env python3

# Created by: Ahmad El-khawaldeh
# Created on: Dec 2020
# this program is the "number guess game"


import random

random_number = random.randint(1, 10)


def main():
    # this function sees if the user iputed the random number

    print("enter a number from 1 to 10")

    User_number_string = input("Enter an integer: ")

    try:
        User_number = int(User_number_string)

        if User_number == random_number:
            print(" you got the right answer !!")
        elif User_number < 0:
            print("it is not a possitive integer")
        elif User_number != random_number:
            while User_number != random_number:
                User_number = int(User_number_string)
                if User_number > random_number:
                    print("HINT: the is too big, try again ")
                    print("enter a number from 1 to 10")
                    User_number_string = input("Enter an integer: ")
                elif 0 <= User_number < random_number:
                    print("HINT: the number is too small, guess again")
                    print("enter a number from 1 to 10")
                    User_number_string = input("Enter an integer: ")
                elif User_number < 0:
                    print("it is not a possitive integer")
                elif User_number == random_number:
                    print("you are right, Good job ")
                    break
    except Exception:
        print("This was not an integer")


if __name__ == "__main__":
    main()
