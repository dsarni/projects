# Daniel Sarni
# dsarni@ucsc.edu
# Programming Assignment 3
# This program takes 3 inputs from the user and returns those inputs in the radius and area of a sphere and cylinder.

import math
def sphere_volume(r):
    v = 4/3*math.pi*r**3
    return v
def sphere_area(r):
    a = 4*math.pi*r**2
    return a
def cylinder_volume (r,h):
    cv = math.pi*r**2*h
    return cv
def cylinder_area (r,h):
    ca = (2*math.pi*r**2)+2*math.pi*r*h
    return ca
def print_sphere(r):
    a = sphere_volume(r)
    b = sphere_area(r)
    print("The volume of the sphere with radius",r,"is:",a)
    print("The surface area of the sphere with radius",r,"is:",b)
def print_cylinder(r,h):
    c = cylinder_volume(r,h)
    d = cylinder_area(r,h)
    print("The volume of the cylinder with radius",r,"and height",h,"is:",c)
    print("The surface area of the cylinder with radius",r,"and height",h,"is:",d)
print("Enter three numbers:")
input1 = input("first number: ")
input2 = input("second number: ")
input3 = input("third number: ")
print()
r = float(input1)
print_sphere(r)
print()
r = float(input2)
print_sphere(r)
print()
r = float(input3)
print_sphere(r)
print()
r = float(input1)
h = float(input2)
print_cylinder(r,h)
print()
r = float(input2)
h = float(input3)
print_cylinder(r,h)
print()
r = float(input3)
h = float(input1)
print_cylinder(r,h)
print()





