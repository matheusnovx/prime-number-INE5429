from LinearCongruentialGenerator import *
from ParkMiller import *
from random import randint

def pseudo_aleatorio():
    seed = randint(0, 1000)
    print("Seed: ", seed)
    print("Linear Congruential Generator: ", LinearCongruentialGenerator(seed, 1664525, 1013904223, 2**32))
    print("Park Miller: ", ParkMiller(seed, 16807, 2**31 - 1))

pseudo_aleatorio()