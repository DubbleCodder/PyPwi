from time import *

class Read:
    def __init__(self, file, amt):
        self.fn = open(file, "r")
        self.amt = amt
        Lines = self.fn.readlines()

        count = 0

        for line in Lines:
            sleep(self.amt)
            count += 1
            print("{}".format(line.strip()))

file("thing.txt", 0.09)
