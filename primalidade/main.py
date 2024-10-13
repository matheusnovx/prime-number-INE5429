from random import randint
from time import time

from Fermat import is_prime as is_prime_fermat
from MillerRabin import is_prime as is_prime_miller_rabin
from pseudo_aleatorio.LinearCongruentialGenerator import LinearCongruentialGenerator

def generate_prime_number(generator, test_method) -> int:
    random_number = 0
    number_of_loops = 5

    is_prime = False

    start_time = 0
    end_time = 0

    while not is_prime :
        start_time = time()

        random_number = generator.next()
        if test_method(random_number, number_of_loops):
            is_prime = True

        end_time = time()

    print("Numero gerado: ", random_number)
    print("Lenght: ", random_number.bit_length(), "bits.")
    print("Tempo de execução: {:.8f} segundos.\n".format(end_time - start_time))

    return random_number

if __name__ == "__main__":
    bit_length = [40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096]
    seeds = [randint(1, length - 1) for length in bit_length]

    print("Fermat: \n")
    for length in bit_length:
        lcg = LinearCongruentialGenerator(seeds[bit_length.index(length)], 2 ** length)
        generate_prime_number(lcg, is_prime_fermat)

    print("\n--------------------------------------------------------------------------------\n")

    print("Miller Rabin: \n")
    for length in bit_length:
        lcg = LinearCongruentialGenerator(seeds[bit_length.index(length)], 2 ** length)
        generate_prime_number(lcg, is_prime_miller_rabin)

    print("Done!")