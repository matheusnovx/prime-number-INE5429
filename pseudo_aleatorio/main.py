from time import time

from LinearCongruentialGenerator import *
from ParkMiller import *
from random import randint


if __name__ == "__main__":
    bit_lenght = [40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096]

    # for lenght in bit_lenght:
    #     times = []
    #     for _ in range(1_000_000):
    #         lcg = LinearCongruentialGenerator()
    #         start = time()
    #         number_generated = lcg.lcg(lenght)
    #         end = time()
    #         times.append(end - start)
    #     print("Length: {} bits".format(lenght))
    #     print("Tempo de execução: {:.8f} segundos.\n".format((sum(times)/len(times))))
    #
    for lenght in bit_lenght:
        times = []
        for _ in range(1_000_000):
            pm = ParkMiller()
            start = time()
            number_generated = pm.pm(lenght)
            end = time()
            times.append(end - start)
        print("Length: {} bits".format(lenght))
        print("Tempo de execução: {:.8f} segundos.\n".format((sum(times)/len(times))))