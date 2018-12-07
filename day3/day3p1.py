#!usr/bin/python


def getinputarray(userfile=None):
    if userfile == None:
        filename = 'input.txt'
    else:
        filename = userfile
    inputs = []
    with open(filename, "r") as inputfile:
        for lines in inputfile:
            inputs.append(lines.rstrip())
    inputfile.close()
    return inputs


