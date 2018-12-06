#!/usr/bin/python

# Solves (https://adventofcode.com/2018/day/1) given input.txt in the same path


def tuner(frequency, seenbefore, tuned):
    with open('input.txt', "r") as inputfile:
        while tuned == False:
            inputline = inputfile.readline()
            if inputline == "":
                return frequency, seenbefore, tuned
            # print("Got {}".format(inputline))
            direction = str(inputline[0])
            # print("Direction is {}".format(direction))
            magnitude = int(inputline[1:])
            # print("Magnitude is {}".format(magnitude))
            if direction == "+":
                frequency += magnitude
            #    print("Added {}      // new frequency is {}".format(magnitude, frequency))
            elif direction == "-":
                frequency -= magnitude
            #    print("Subtracted {} // new frequency is {}".format(magnitude, frequency))
            else:
                break

            if frequency in seenbefore:
                print("Saw repeated frequency at {} MHz".format(frequency))
                tuned = True
                break
            else:
                seenbefore.append(frequency)
                print("Added {} MHz to list of {} seen frequencies".format(frequency, len(seenbefore)))
    inputfile.close()
    return frequency, seenbefore, tuned


def main():
    frequency = 0
    seenbefore = []
    tuned = False
    while True:
        frequency, seenbefore, tuned = tuner(frequency, seenbefore, tuned)
        if tuned:
            break

    print("The frequency is {}".format(frequency))


if __name__ == "__main__":
    main()