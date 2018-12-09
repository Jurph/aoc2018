#!usr/bin/python
# Solves Day 3, Part 1 of Advent of Code 2018
# Details at https://adventofcode.com/2018/day/3
# Input looks like:     #1 @ 258,327: 19x22
import unittest


class Claim:
    """An object for storing a single line of the input"""
    def __init__(self, ordinal, xcoordinate, ycoordinate, width, height):
        self.name = "Claim" + str(ordinal)
        self.number = int(ordinal)
        self.x = int(xcoordinate)
        self.y = int(ycoordinate)
        self.width = int(width)
        self.height = int(height)
        self.area = int(width) * int(height)
        self.isdisputed = False

    @classmethod
    def create_claim_from_string(cls, inputstring):
        # Could I just refactor Claim() to take an inputstring and self-initialize?
        hashnum, at, coords, size = inputstring.split(" ")
        number = int(hashnum[1:])
        x, y = coords.split(",")
        y = int(y[:-1])
        width, height = size.split("x")
        new_claim = cls(number, x, y, width, height)
        return new_claim


class SquareInch:
    """A square inch of the fabric the elves want to claim"""
    def __init__(self, xcoordinate: int, ycoordinate: int, starting_claim=None):
        self.x = int(xcoordinate)
        self.y = int(ycoordinate)
        if not starting_claim:
            self.isclaimed = int(0)
            self.isdisputed = False
        else:
            self.isclaimed = int(starting_claim)
        if self.isclaimed > 1:
            self.isdisputed = True
        elif (self.isclaimed == 1) | (self.isclaimed == 0):
            self.isdisputed = False
        else:
            print("WARN: Tenuous claim on square at {},{} - claim value purports to be {}".format(self.x, self.y, self.isclaimed))
            self.isdisputed = None
        #  print("Created a SquareInch at ({},{}) with a claim of {} and dispute of {}".format(
        #  self.x, self.y, self.isclaimed, self.isdisputed))

    def claim(self):
        self.isclaimed += 1
        if self.isclaimed > 1:
            self.isdisputed = True
        elif (self.isclaimed == 1) | (self.isclaimed == 0):
            self.isdisputed = False
        else:
            self.isclaimed = 0
            self.isdisputed = False

    def relinquish(self):
        self.isclaimed -= 1
        if self.isclaimed > 1:
            self.isdisputed = True
        elif (self.isclaimed == 1) | (self.isclaimed == 0):
            self.isdisputed = False
        elif self.isclaimed < 0:
            self.isclaimed = 0
            self.isdisputed = False
        else:
            print("WARN: relinquishing this claim has created problems at {}, {}".format(self.x, self.y))


class TestCustomFunctions(unittest.TestCase):

    def test_initialize_a_claim(self):
        init_string = "#1 @ 258,327: 19x22"
        clem = Claim.create_claim_from_string(init_string)
        self.assertEqual(clem.x, 258)
        self.assertEqual(clem.y, 327)
        self.assertEqual(clem.area, 418)  # equals 19 x 22

    def test_initialize_square_inch(self):
        x = 258
        y = 327
        inchy = SquareInch(x, y)
        self.assertEqual(inchy.x, x)
        self.assertEqual(inchy.y, y)
        self.assertEqual(inchy.isclaimed, 0)
        self.assertEqual(inchy.isdisputed, False)

    def test_claim_and_relinquish(self):
        x = 260
        y = 330
        inchy = SquareInch(x, y)
        self.assertEqual(inchy.isclaimed, 0)
        self.assertEqual(inchy.isdisputed, False)
        inchy.claim()
        self.assertEqual(inchy.isclaimed, 1)
        self.assertEqual(inchy.isdisputed, False)
        inchy.claim()
        self.assertEqual(inchy.isclaimed, 2)
        self.assertEqual(inchy.isdisputed, True)
        inchy.claim()
        inchy.relinquish()
        self.assertEqual(inchy.isclaimed, 2)
        self.assertEqual(inchy.isdisputed, True)
        inchy.relinquish()
        self.assertEqual(inchy.isclaimed, 1)
        self.assertEqual(inchy.isdisputed, False)
        inchy.relinquish()
        inchy.relinquish()
        self.assertEqual(inchy.isclaimed, 0)
        self.assertEqual(inchy.isdisputed, False)


def get_input_array(userfile=None):
    if userfile == None:
        filename = 'input.txt'
    else:
        filename = userfile
    inputs = []
    with open(filename, "r") as inputfile:
        for lines in inputfile:
            inputs.append(lines.rstrip())
    inputfile.close()
    print("Got {} input elements from {}".format(len(inputs), filename))
    return inputs


def main():
    inputs = get_input_array('input.txt')
    claims_array = []
    x = 0
    y = 0
    fabric = {
        (x, y): 0
    }
    for i in range(1, len(inputs)+1):
        print("i = {} // inputs[i] = {}".format(i, inputs[i-1]))
        claims_array.append(Claim.create_claim_from_string(str(inputs[i - 1])))
    for this_claim in claims_array:
        for x in range(this_claim.x, this_claim.x + this_claim.width):
            for y in range(this_claim.y, this_claim.y + this_claim.height):
                if (x, y) not in fabric:
                    fabric[(x, y)] = 1
                elif (x, y) in fabric:
                    fabric[(x, y)] += 1
                else:
                    print("Something weird is going on.")
    disputes = 0
    for coords, claims in fabric.items():
        if claims > 1:
            disputes += 1
            print("Found {} competing claims at {} bringing total to {}".format(claims, coords, disputes))
        else:
            print("Found {} claim at {} bringing total to {}".format(claims, coords, disputes))
    print("Found {} total disputes".format(disputes))  # Solves Day 3 part 1

    #  Solves Day 3 part 2
    for this_claim in claims_array:
        for x in range(this_claim.x, this_claim.x + this_claim.width):
            for y in range(this_claim.y, this_claim.y + this_claim.height):
                if fabric[(x, y)] == 1:
                    pass
                elif fabric[(x, y)] > 1:
                    this_claim.isdisputed = True
                else:
                    print("WARN: found an apparently unclaimed square")
        if this_claim.isdisputed is False:
            print("Claim #{} appears to be undisputed".format(this_claim.number))

if __name__ == "__main__":
    main()
    unittest.main()

