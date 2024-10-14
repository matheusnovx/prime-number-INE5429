from time import time

from Fermat import is_prime as is_prime_fermat
from MillerRabin import is_prime as is_prime_miller_rabin
from pseudo_aleatorio.LinearCongruentialGenerator import LinearCongruentialGenerator
from pseudo_aleatorio.ParkMiller import ParkMiller

def generate_prime_number(lenght, generator, test_method) -> int:
    random_number = 0
    number_of_loops = 5

    is_prime = False

    start_time = 0
    end_time = 0

    while not is_prime :
        start_time = time()

        random_number = generator.lcg(lenght)
        # random_number = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        if test_method(random_number, number_of_loops):
            is_prime = True

        end_time = time()

    print("Numero gerado: ", random_number)
    print("Lenght: ", random_number.bit_length(), "bits.")
    print("Tempo de execução: {:.8f} segundos.\n".format(end_time - start_time))

    return random_number

if __name__ == "__main__":
    bit_lengths =  [40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096]

        # # Teste com o metodo de Miller-Rabin
        # print("Miller-Rabin")
        # for lenght in bit_lengths:
        #     lcg = LinearCongruentialGenerator()
        #     number_generated = generate_prime_number(lenght, lcg, is_prime_miller_rabin)

    # Teste com o metodo de Fermat
    print("Fermat")
    for lenght in bit_lengths:
        lcg = LinearCongruentialGenerator()
        number_generated = generate_prime_number(lenght, lcg, is_prime_fermat)