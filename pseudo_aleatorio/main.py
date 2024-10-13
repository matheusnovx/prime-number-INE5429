from time import time

from LinearCongruentialGenerator import *
from ParkMiller import *
from random import randint


def lcg_generator(seed):
    a = 1664525
    c = 1013904223
    m = 2 ** lenght
    lcg = LinearCongruentialGenerator(seed, a, c, m)

    startTimes.append(time())
    number = lcg.next()
    endTimes.append(time())

    print("Lenght: ", number.bit_length(), "bits.")
    print("Seed: {}".format(seed))
    print("Numero gerado: {}".format(number))
    print("Tempo de execução: {:.8f} segundos.\n".format(endTimes[-1] - startTimes[-1]))


def pm_generator(seed):
    a = 48271
    m = 2 ** lenght
    pm = ParkMiller(seed, a, m)

    startTimes.append(time())
    number = pm.next()
    endTimes.append(time())

    print("Length: {} bits".format(lenght))
    print("Seed: {}".format(seed))
    print("Numero gerado: {}".format(number))
    print("Tempo de execução: {:.8f} segundos.\n".format(endTimes[-1] - startTimes[-1]))


if __name__ == "__main__":
    startTimes = []
    endTimes = []
    bitLenght = [40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096]

    seeds = [randint(1, leng - 1) for leng in bitLenght]

    print("Linear Congruential Generator: \n")
    for lenght in bitLenght:
        lcg_generator(seeds[bitLenght.index(lenght)])

    print("\n--------------------------------------------------------------------------------\n")

    print("Park Miller Generator: \n")
    for lenght in bitLenght:
        pm_generator(seeds[bitLenght.index(lenght)])

    print("Done!")
