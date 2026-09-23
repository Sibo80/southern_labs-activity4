# Author: Sibonile

"""
This calculates the area of a circle using a random radius.
"""

import math
import random


def calculate_circle_area(radius):
    """
    Calculate the radius of a circle.

    :param radius: The radius of the circle.
    :return: calculated area of the circle.
    """
    return math.pi * radius ** 2


def generate_random_radius(min_val, max_val):
    """Generate and return a random integer radius."""
    return random.randint(min_val, max_val)


def main():
    """Run the main program."""
    radius = generate_random_radius(1, 10)
    area = calculate_circle_area(radius)

    print("Radius: (radius)")
    print("Circle area: (area: 2)")

 
if __name__ == "__main__":
    main()

