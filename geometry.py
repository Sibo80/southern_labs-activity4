# Author: Sibonile

"""Calculate the area of a circle using a random radius."""

import math
import random


def calculate_circle_area(radius):
    """
    Calculate the area of a circle.

    :param radius: The radius of the circle.
    :return: The area of the circle.
    """
    return math.pi * radius ** 2


def generate_random_radius(min_val, max_val):
    """Generate and return a random integer radius."""
    return random.randint(min_val, max_val)


def main():
    """Run the main program."""
    radius = generate_random_radius(1, 10)
    area = calculate_circle_area(radius)

    print(f"Radius: (radius)")
    print(f"Circle area: (area:.2f)")


if __name__ == "__main__":
    main()

