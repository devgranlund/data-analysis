#!/usr/bin/env python3

import math


def main():
    while True:
        selection = input("Choose a shape (triangle, rectangle, circle):")
        if selection == "triangle":
            print_area(triangle())
        elif selection == "rectangle":
            print_area(rectangle())
        elif selection == "circle":
            print_area(circle())
        elif selection == "":
            break
        else:
            print("Unknown shape!")


def triangle():
    base = float(input("Give base of the triangle:"))
    height = float(input("Give height of the triangle:"))
    return (base * height) // 2

def print_area(f):
    print(f"The area is {f:6f}")

def rectangle():
    width = float(input("Give width of the rectangle:"))
    height = float(input("Give height of the rectangle:"))
    return width * height

def circle():
    radius = float(input("Give radius of the circle:"))
    return math.pi * radius ** 2

if __name__ == "__main__":
    main()
