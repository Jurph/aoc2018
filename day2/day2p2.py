#!/usr/bin/python
# Solves (https://adventofcode.com/2018/day/2#part2) given input.txt in the same path
from string import ascii_lowercase
import binascii
import unittest


def binvalue(longstring):
    bytesum = 0
    for ascii_letter in longstring:
        bytesum += int(ord(ascii_letter))
    return bytesum



def main():
    # Get file input into a list
    # Probably ought to save this as a function
    barcodes = []
    with open('input.txt', "r") as inputfile:
        for lines in inputfile:
            barcodes.append(lines.rstrip())
        inputfile.close()
    barcodes.sort()
    scorelist = []
    for barcode in barcodes:
        scorelist.append(binvalue(barcode))
    receipts = dict(zip(barcodes, scorelist))
    for key, value in receipts:
        # For each barcode
        # Get a list of all barcodes whose scores are off by strictly one
        # Pass primary and one of its candidates into "matchem(barcode1, barcode2)"
        # Check the first letter of each
        # if they match pop them into the tentative answer vector
        # Catch one - and only one - off-by-one error
        # Continue comparing until equality fails
        # return an answer vector or None


if __name__ == "__main__":
    main()
