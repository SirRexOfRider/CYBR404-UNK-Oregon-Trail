'''
Author: Anna Gettinger
Project: A Nifty, Dungeons and Dragons-esque, Oregon Trail-esque, Survive the Day at UNK Game™
Purpose: To create a Weapons class to hold weapon data.
Last Edit: 3/4/25
'''

# Imports.
from Weapons import Weapons

def main():

    # Call functions to read in file data, create objects, and print out new objects.
    weapons_list = read_file("weapons.txt", Weapons)
    print_objects(weapons_list)

# Create function to read in data from file to create objects.
def read_file(file, class_name):
    object_list = []
    with open(file, "r") as f:
        for line in f:
            c1 = class_name(line.split(",")[0].strip(), line.split(",")[1].strip(), line.split(",")[2].strip())
            object_list.append(c1)
    return object_list

# Create function to print out objects from object list.
def print_objects(object_list):
    for object in object_list:
        print(object)

if __name__ == '__main__':
    main()
