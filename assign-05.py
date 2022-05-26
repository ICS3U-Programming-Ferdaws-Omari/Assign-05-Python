# !/usr/bin/env python3
# Created By: Ferdaws
# Date: May 2022
# This program asks the user for a side
# of the cube in mm. It then
# calculates and displays the area and
# vloume.
import math


def calc_area(user_side):
    # Calculate area.
    r_area = 6 * user_side ** 2

    return r_area


def calc_volume(user_side):
    # Calculate volume.
    r_volume = user_side ** 3

    return r_volume


def main():
    # Ask the user for one of the sides of the cube and the unit
    user_side = input("Enter the side:")
    user_units = input("Enter the units:")

    try:
        side_from_user = float(user_side)
    # display the results to the user and round it to two decimal places
        area = calc_area(side_from_user)
        print("")
        print("Area = {:.2f} {}". format(area, user_units))
        volume = calc_volume(side_from_user)
        print("")
        print("Volume = {:.2f} {}". format(volume, user_units))

    except ValueError:
        print("Invalid input")


if __name__ == "__main__":
    main()
