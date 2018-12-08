#!usr/bin/python
# Solves Day 3, Part 1 of Advent of Code 2018
# Details at https://adventofcode.com/2018/day/3
# Input looks like:     #1 @ 258,327: 19x22


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
    def __init__(self, xcoordinate, ycoordinate, starting_claim=None):
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
        elif self.isclaimed == 1 | self.isclaimed == 0:
            self.isdisputed = False
        elif self.isclaimed < 0:
            self.isclaimed = 0
            self.isdisputed = False
        else:
            print("WARN: relinquishing this claim has created problems at {}, {}".format(self.x, self.y))


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
    for i in range(0, len(inputs)+1):
        print("i = {} // inputs[i] = {}".format(i, inputs[i-1]))
        claims_array.append(Claim.create_claim_from_string(str(inputs[i - 1])))
    print("Got many claims including {}".format(claims_array[420].name))
    for this_claim in claims_array:
        for x in range(this_claim.x, this_claim.x + this_claim.width):
            for y in range(this_claim.y, this_claim.y + this_claim.height):
                this_square = SquareInch(x, y)
                this_square.claim()
                print("[{}, {}] is claimed {} times".format(this_square.x, this_square.y, this_square.isclaimed))
    disputes = 0

    for x in range(0, 1500):
        for y in range(0, 1500):
            if SquareInch(x, y).isdisputed is True:
                disputes += 1
                print("[{},{}] - Disputed with {} claims | TOTAL: {}".format(x, y, SquareInch(x, y).isclaimed, disputes))
            elif not SquareInch(x, y).isdisputed:
                print("[{},{}] - Available with {} claims | TOTAL: {}".format(x, y, SquareInch(x, y).isclaimed, disputes))
            else:
                print("[{},{}] - something strange going on here.".format(x, y))
    print("Found {} disputes".format(disputes))


if __name__ == "__main__":
    main()