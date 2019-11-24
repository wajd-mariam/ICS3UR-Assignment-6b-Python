#!/usr/bin/env python3

# Created by: Wajd Mariam
# Created on: November 2019
# This program calculates the volume of the Tetrahedron

import math


def calculate_volume(side):
    # this function calculates volume
    # process
    volume = (side ** 3) / (6 * math.sqrt(2))

    # output
    print("The volume of the Tetrahedron is {} cm³".format(round(volume, 2)))


def main():
    # this function calls functions
    # welcome statement
    print("This program calculates the Tetrahedron volume")
    print("")

    # try statement
    # input
    try:
        side_from_user = int(input("Enter length of Tetrahedron side(cm): "))
    except Exception:
        print("Invalid entry, please try again")
    else:
        # calling function if side_from_user is valid
        calculate_volume(side_from_user)
    finally:
        print("")
        print("Thank you for using my program")


if __name__ == "__main__":
    main()
