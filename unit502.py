#!/usr/bin/env python3

# Created by: Amir Mersad
# Created on: November 2019
# This program calculates the area of a triangle


def area(base_user, height_user):
    # Process
    area = (base_user * height_user) / 2
    if base_user <= 0 or height_user <= 0:
        print("\nThe value must be more than 0!")
        return

    # Output
    print("\nThe area of the triangle is {} cm^2".format(area))


def main():
    # This function gets input and call other functions

    # Input
    base_str = input("Please enter the base (cm): ")
    height_str = input("\nPlease enter the height (cm): ")

    # Process
    try:
        base = int(base_str)
        height = int(height_str)
    except(Exception):
        print("\nWrong input!!!")
        return

    # Calling another function
    area(base, height)


if __name__ == "__main__":
    main()
