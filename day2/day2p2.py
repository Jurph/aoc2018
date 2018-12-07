#!/usr/bin/python
# Solves (https://adventofcode.com/2018/day/2#part2) given input.txt in the same path


def matchmaker(longstring1,longstring2):
    matches = ""
    mismatches = int(0)
    if len(longstring1) != len(longstring2):
        print("{} and {} FAIL - different lengths".format(longstring1, longstring2))
        return None
    for i in range(0, len(longstring1)):
        if (mismatches <= 1) & (longstring1[i] == longstring2[i]):
            matches += longstring1[i]
        elif longstring1[i] != longstring2[i]:
            mismatches += 1
            matches += " "
        elif mismatches > 1:
            print("{} and {} FAIL - too many mismatches".format(longstring1, longstring2))
        else:
            print("Reached an unreachable segment - oh no")
    if mismatches == 1:
        print("{} and {} PASS - returning {}".format(longstring1, longstring2, matches))
        return matches
    elif mismatches == 0:
        print("These strings are identical. FAIL")
        return None


def main():
    # Get file input into a list
    # Probably ought to save this as a function
    barcodes = []
    with open('input.txt', "r") as inputfile:
        for lines in inputfile:
            barcodes.append(lines.rstrip())
        inputfile.close()
    for i in range(0, len(barcodes)):
        for j in range(0, len(barcodes)):
            matches = matchmaker(barcodes[i], barcodes[j])
            if matches != None:
                print("Found a matching string:\n{} AND\n{} SHARE\n{}".format(barcodes[i],barcodes[j], matches))
                quit(0)


if __name__ == "__main__":
    main()
