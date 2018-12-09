#!usr/bin/python
# Solves Day 4 of Advent of Code 2018
# Details at https://adventofcode.com/2018/day/4
# Input looks like:
# [1518-09-05 23:59] Guard #79 begins shift
# [1518-04-15 00:27] wakes up
# [1518-03-21 00:03] Guard #1951 begins shift
# [1518-09-29 00:45] wakes up
# [1518-06-22 00:00] Guard #479 begins shift
# [1518-09-22 00:12] falls asleep
# [1518-11-11 00:39] wakes up
# [1518-06-18 00:01] Guard #79 begins shift
import unittest
import datetime

class TimeCard:
    def __init__(self, employee: int, main_DTG: datetime):
        self.guardnumber = employee
        self.year_month_day = main_DTG.date
        self.time_of_day = main_DTG.time
        self.events = {
            (self.year_month_day, self.time_of_day): "START"
        }

    @classmethod
    def initialize_timecard_from_guard_string(cls, inputstring):
        chunk1, chunk2 = inputstring.split("]")
        main_DTG = datetime.fromtimestamp(chunk1[1:])  # Requires python 3.7 or newer
        if "Guard" in chunk2:
            employee = int(chunk2[8:].split(" "))
        else:
            print("Got input string without a Guard #")
            employee = 0
        new_timecard = cls(employee, main_DTG)
        return new_timecard


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
    return inputs.sort()


def main():
    inputs = get_input_array('input.txt')























if __name__ == "__main__":
    main()
    unittest.main()