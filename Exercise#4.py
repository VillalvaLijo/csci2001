#Exercise#4.py

#Samuel Villalva Lijo

#1/21/22

#this program takes the radius of a circle as a command line argument


from math import pi

radius = None
while radius is None:
    try:
        radius = float(input('Enter the radius of a circle: '))
    except ValueError as err:
        print('Error parsing that as a number: %s' % err)


def compute_diameter(radius):
    diameter = radius*2
    return diameter

def compute_circumference(radius):
    circumference = 2*pi*radius
    return circumference

def compute_area(radius):
    area = pi*radius*radius
    return area

print("Radius: ", radius)
print("Diameter: ", compute_diameter(radius))
print("Circumferenc: ", compute_circumference(radius))
print("Area: ", compute_area(radius))



