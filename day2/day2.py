#!/usr/bin/python
# Solves (https://adventofcode.com/2018/day/2) given input.txt in the same path
from string import ascii_lowercase


def hasdoubles(barcode):
    fizz = False
    checklist = []
    print("Evaluating barcode:  {} for DOUBLES".format(barcode))
    for letter in barcode:
        checklist.append(letter)
    checklist.sort()
    print("Built checklist:     {}".format(checklist))
    while True:
        try:
            found = checklist.pop(-1)
        except(IndexError):
            print("Finished looking in this one!")
            break
        print("Looking for {} in {}".format(found, checklist))
        if found in checklist:
            print("Found duplicate {} in {}".format(found, barcode))
            fizz = True
            break
        else:
            print("{} was not a duplicate in {}".format(found, barcode))
    return fizz


def hastriples(barcode):
    buzz = False
    checklist = []
    print("Evaluating barcode:  {} for TRIPLES".format(barcode))
    for letter in barcode:
        checklist.append(letter)
    checklist.sort()
    print("Built checklist:     {}".format(checklist))
    while True:
        try:
            found = checklist.pop(-1)
        except(IndexError):
            print("Finished looking in this one!")
            break
        print("Looking for {} in {}".format(found, checklist))
        if found in checklist:
            print("Found {} in the list - removing it and searching for more".format(found))
            checklist.remove(found)
            if found in checklist:
                print("Found triplicate {} in  {}".format(found, barcode))
                buzz = True
                break
            else:
                print("{} was duplicate but not triplicate in {}".format(found, barcode))
                # Theoretically I could return both fizz and buzz here.  
                fizz = True
                buzz = False
        else:
            print("{} was not a duplicate in {}".format(found, barcode))
            fizz = False
    return buzz


def main():
    doubles = 0
    triples = 0
    barcodes = ('jan', 'dogs', 'abcdefabcdefa','dongtar', 'chupacabra')
    with open('input.txt', "r") as inputfile:
        # barcode = inputfile.readline()
        for barcode in barcodes:
            if hasdoubles(barcode):
                doubles += 1
            else:
                doubles *= 1
            if hastriples(barcode):
                triples += 1
            else:
                triples *= 1
    inputfile.close()
    checksum = doubles * triples
    print("Found {} doubles and {} triples // Checksum is {}".format(doubles, triples, checksum))


if __name__ == "__main__":
    main()
