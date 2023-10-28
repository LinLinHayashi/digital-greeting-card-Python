#!/usr/bin/env python3
'''a42'''
print(__doc__)

import random

class ArtConfig:
    '''ArtConfig class'''
    def __init__(self, lower: int, upper: int):
        self.lower: int = lower
        self.upper: int = upper

class GenRandom:
    '''GenRandom class'''
    def __init__(self, conf: ArtConfig):
        self.number: int = random.randrange(conf.lower, conf.upper)

def printNumber(conf: ArtConfig):
    '''printNumber method'''
    number: GenRandom = GenRandom(conf)
    print(f"{number.number:>4}", end = '')

def printTable(line: int):
    '''printTable method'''
    print("CNT SHA   X   Y RAD  RX  RY   W   H   R   G   B  OP")
    i: int = 0
    for i in range(line):
        print(f"{i:>3}", end = '') # CNT
        printNumber(ArtConfig(0, 4)) # SHA
        printNumber(ArtConfig(0, 501)) # X
        printNumber(ArtConfig(0, 301)) # Y
        printNumber(ArtConfig(0, 101)) # RAD
        printNumber(ArtConfig(10, 31)) # RX
        printNumber(ArtConfig(10, 31)) # RY
        printNumber(ArtConfig(10, 101)) # W
        printNumber(ArtConfig(10, 101)) # H
        printNumber(ArtConfig(0, 256)) # R
        printNumber(ArtConfig(0, 256)) # G
        printNumber(ArtConfig(0, 256)) # B
        op = GenRandom(ArtConfig(0, 11)).number * 0.1
        print(" %1.1f" % op) # OP

def main():
    '''main method'''
    printTable(10)

main()