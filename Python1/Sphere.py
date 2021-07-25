# Daniel Sarni
# dsarni@ucsc.edu
# Programming Assignment 1
# This program will compute the volume and surface area of a sphere by taking in the radius entered by the user

import math
radius = float(input("Enter the radius of the sphere: "))
volume = 4/3*math.pi*radius**3
sa = 4*math.pi*radius**2
print("The volume is:", volume)
print("The surface area is:", sa)