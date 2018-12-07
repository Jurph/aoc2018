#!usr/bin/python
# Solves Day 3, Part 1 of Advent of Code 2018
# Details at https://adventofcode.com/2018/day/3
# Input looks like:     #1 @ 258,327: 19x22


def getinputarray(userfile=None):
    if userfile == None:
        filename = 'input.txt'
    else:
        filename = userfile
    inputs = []
    with open(filename, "r") as inputfile:
        for lines in inputfile:
            inputs.append(lines.rstrip())
    inputfile.close()
    return inputs


class Claim:
    """An object for storing a single line of the input"""
    def __init__(self, ordinal, xcoordinate, ycoordinate, width, height):
        self.name = "Claim" + str(ordinal)
        self.number = int(ordinal)
        self.x = int(xcoordinate)
        self.y = int(ycoordinate)
        self.width = int(width)
        self.height = int(height)
        self.area = width * height


class SquareInch:
    """A square inch of the fabric the elves want to claim"""
    def __init__(self, xcoordinate, ycoordinate, isclaimed=None):
        self.x = int(xcoordinate)
        self.y = int(ycoordinate)
        if isclaimed is None or isclaimed is False:
            self.isclaimed = int(0)
        else:
            self.isclaimed = bool(isclaimed)
        if isclaimed > 1:
            self.isdisputed = True
        elif isclaimed == 1 | isclaimed == 0:
            self.isdisputed = False
        else:
            print("WARN: Tenuous claim on square at {},{}".format(self.x, self.y))
            self.isdisputed = None

    def claim(self):
        self.isclaimed += 1
        if self.isclaimed > 1:
            self.isdisputed = True
        elif self.isclaimed == 1 | self.isclaimed == 0:
            self.isdisputed = False
        else:
            self.isclaimed = 0
            self.isdisputed = False

    def relinquish(self):
        self.isclaimed -= 1
        if self.isclaimed > 1:
            self.isdisputed = True
        elif self.isclaimed == 1 | self.isclaimed == 0:
            self.isdisputed = False
        elif self.isclaimed < 0:
            self.isclaimed = 0
            self.isdisputed = False
        else:
            print("WARN: relinquishing this claim has created problems at {}, {}".format(self.x, self.y))

