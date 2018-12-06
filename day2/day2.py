#!/usr/bin/python
# Solves (https://adventofcode.com/2018/day/2) given input.txt in the same path
from string import ascii_lowercase


def hastuples(barcode):
    fizz = False  # has doubles
    buzz = False  # has triples
    checklist = []
    print("Evaluating (for DOUBLES) barcode:  {}".format(barcode))
    for letter in barcode:
        checklist.append(letter)
    checklist.sort()  # I'm not actually using the opportunity this presents. I probably should.
    # print("Built checklist:     {}".format(checklist))
    while True:
        try:
            found = checklist.pop(-1)
        except(IndexError):
            # print("Finished looking in this one!")
            break
        # print("Looking for {} in {}".format(found, checklist))
        if found in checklist:
            fizz = True
            # print("Found {} in the list - removing it and searching for more".format(found))
            checklist.remove(found)
            if found in checklist:
                print("Found triplicate {} in  {}".format(found, barcode))
                fizz = False
                buzz = True
                break
            else:
                print("{} was duplicate but not triplicate in {}".format(found, barcode))
                fizz = True
                buzz = False
                break
        else:
            # print("{} was not a duplicate in {}".format(found, barcode))
            fizz = False
            buzz = False
    return fizz, buzz


def main():
    doubles = 0
    triples = 0
    # test inputs
    # barcodes = ('jan', 'dogs', 'abcdefabcdefa', 'dongtar', 'chupacabra')
    with open('input.txt', "r") as inputfile:
        while True:
            barcode = inputfile.readline()
            if barcode == "":
                print("Out of lines!")
                break
            else:
                hasdoubles, hastriples = hastuples(barcode)
                if hasdoubles:
                    doubles += 1
                    print("Barcode {} has doubles / total is now {}".format(barcode, doubles))
                else:
                    doubles *= 1
                if hastriples:
                    triples += 1
                    print("Barcode {} has triples / total is now {}".format(barcode, triples))
                else:
                    triples *= 1
    inputfile.close()
    checksum = doubles * triples
    print("Found {} doubles and {} triples // Checksum is {}".format(doubles, triples, checksum))


if __name__ == "__main__":
    main()
