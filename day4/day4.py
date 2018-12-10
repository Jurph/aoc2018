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
        self.employee = employee
        self.year_month_day = main_DTG.date
        (self.year, self.month, self.day, self.hour, self.minute, self.second, self.weekday, self.yday, self.dst) = main_DTG.timetuple()
        self.time_of_day = main_DTG.time
        self.events = {
            (self.year_month_day, self.time_of_day): "START"
        }

    def parse_input_string(self, inputstring):
        raw_time_string, event_text = inputstring.split("]")
        raw_time_string = str(raw_time_string[1:])
        event_datetime = datetime.datetime.fromisoformat(raw_time_string)  # Requires python 3.7 or newer
        return event_text, event_datetime


    @classmethod
    def initialize_timecard_from_guard_string(cls, inputstring):
        event_text, shift_began_at = parse_input_string(inputstring)
        if "Guard" in event_text:
            employee = int(str(event_text[8:].split(" ")[0]))
        else:
            print("Got input string without a Guard #")
            employee = None
        new_timecard = cls(employee, shift_began_at)
        return new_timecard


def get_a_nap_from_input_strings(inputstring1, inputstring2):
    start_event_text, nap_started_at = inputstring1.TimeCard.parse_input_string()
    end_event_text, nap_ended_at = inputstring2.TimeCard.parse_input_string()
    if ("falls asleep" in start_event_text) and ("wakes up" in end_event_text):
        return nap_started_at, nap_ended_at
    elif "falls asleep" not in start_event_text:
        print("No start event in {}".format(inputstring1))
    elif "wakes up" not in end_event_text:
        print("No end event in {}".format(inputstring2))
    else:
        print("Well this is awkward.")
        quit(1)


def get_input_array(userfile=None):
    if userfile == None:
        filename = 'input.txt'
    else:
        filename = userfile
    inputs = []
    with open(filename, "r") as inputfile:
        for lines in inputfile:
            inputs.append(lines.rstrip())
    print("Got {} input elements from {}".format(len(inputs), filename))
    inputs.sort()
    return inputs


def main():
    inputs = []
    inputs = get_input_array('input.txt')
    for i in range(20):
        print(inputs[i])


class TestCustomFunctions(unittest.TestCase):

    def test_initialize_a_timecard(self):
        init_string = "[1518-09-05 23:59] Guard #79 begins shift"
        card = TimeCard.initialize_timecard_from_guard_string(init_string)
        self.assertEqual(card.employee, 79)
        self.assertEqual(card.year, 1518)
        self.assertEqual(card.month, 9)
        self.assertEqual(card.day, 5)

    def test_init_safe_failure(self):
        init_string = "[1518-04-15 00:27] wakes up"
        card = TimeCard.initialize_timecard_from_guard_string(init_string)
        self.assertEqual(card.employee, None)
        self.assertEqual(card.year, 1518)
        self.assertEqual(card.month, 4)
        self.assertEqual(card.day, 15)

    def test_nap_measurement(self):
        inits = ["[1518-03-10 23:57] Guard #73 begins shift",
                    "[1518-03-11 00:06] falls asleep",
                    "[1518-03-11 00:22] wakes up",
                    "[1518-03-11 00:38] falls asleep",
                    "[1518-03-11 00:41] wakes up"]
        card = TimeCard.initialize_timecard_from_guard_string(inits[1])
        init_string1 = inits[2]
        init_string2 = inits[3]
        nap_start, nap_end = get_a_nap_from_input_strings(init_string1, init_string2)



if __name__ == "__main__":
    main()
    unittest.main()