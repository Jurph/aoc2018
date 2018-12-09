#!usr/bin/python
# Solves Day 4 of Advent of Code 2018
# Details at https://adventofcode.com/2018/day/4
# Input looks like:
# [1518-11-01 00:00] Guard #10 begins shift
# [1518-11-01 00:05] falls asleep
# [1518-11-01 00:25] wakes up
# [1518-11-01 00:30] falls asleep
# [1518-11-01 00:55] wakes up
# [1518-11-01 23:58] Guard #99 begins shift
# [1518-11-02 00:40] falls asleep
import unittest


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

























if __name__ == "__main__":
    main()
    unittest.main()