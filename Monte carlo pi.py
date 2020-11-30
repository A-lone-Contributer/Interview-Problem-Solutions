# The area of a circle is defined as πr^2. Estimate π using a Monte Carlo method.

# This problem was asked by Google
# Difficulty -> Medium


# The idea is to simulate random (x, y) points in a 2-D plane with domain as a square of side 1 unit.
# Imagine a circle inside the same domain with same diameter and inscribed into the square.
# We then calculate the ratio of number of  points that lied inside the circle and total number of generated points.

# Algorithm for Monte carlo pie estimation:

# 1.Initialize circle_points, square_points to 0
# 2.Generate random x and y points
# 3.loop for a certain interval
# 4.calculate distance from origin as d = sqrt(x*x + y*y)
# 5.If d <= 1, increment circle_points else Increment square_points.
# 6.Terminate the loop
# 7.Calculate pi = 4*(circle_points/square_points).
# 8.Return answer


# import random and math library
import random
from math import sqrt


def piEstimation(iterations):

    # Initialize circle_points, square_points to 0
    circle_points, square_points = 0, 0

    # setting a random seed and giving parameter as None so that it uses system time
    # for generating random values
    random.seed(None)

    # run loop till the number of iterations (more iterations = better estimation)
    for _ in range(0, iterations):

        # generating random values for x and y
        rand_x, rand_y = random.random(), random.random()

        # calculating the distance from origin (sqrt isn't mandatory as we have 1 on other side
        # but for better understanding i used it
        origin_dist = sqrt(rand_x ** 2 + rand_y ** 2)

        # if origin distance is 1 i.e we are inside the circle else inside square so increment the
        # respective point counts
        if origin_dist <= 1:
            circle_points += 1
        square_points += 1

    # calculating value of pi
    pi = (4 * circle_points) / square_points

    return pi


# Driver code
print(piEstimation(10000))

# Time Complexity : O(n)
# Space Complexity : O(1)
