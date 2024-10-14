"""
    Park-Miller pseudo-random number generator.
    -------------------------------------------
    The Park-Miller random number generator is a simple and fast pseudo-random number generator.
    It is defined by the recurrence relation:
    X_{n+1} = (aX_n) mod m
    where X_0 is the seed, and a and m are constants.

    Using the parameters cited in the page https://en.wikipedia.org/wiki/Lehmer_random_number_generator#Parameters_in_common_use
    "In 1988, Park and Miller[3] suggested a Lehmer RNG with particular parameters m = 2^31 − 1 = 2,147,483,647
    (a Mersenne prime M31) and a = 75 = 16,807 (a primitive root modulo M31), now known as MINSTD."
"""
from time import time_ns


class ParkMiller:
    def __init__(self, m: int = (2 ** 32) - 1, a: int = 16807):
        self.a = a
        self.m = m  # Módulo

    def pm(self, n_bits, seed=None):
        # Máscara para limitar os bits gerados
        mask = (1 << n_bits) - 1
        m, a = self.m, self.a

        # Define o seed com base no tempo atual se não for fornecido
        if seed is None:
            seed = time_ns() % m

        number_generated = (a * seed) % m
        result = []
        bits_collected = 0

        # Gera números até alcançar a quantidade desejada de bits
        while bits_collected < n_bits:
            number_generated = (a * number_generated) % m
            new_generated = number_generated & ((1 << 32) - 1)

            result.append(new_generated)
            bits_collected += 32

        # Combina os números gerados em um único resultado
        final_result = 0
        for part in result:
            final_result = (final_result << 32) | part

        return final_result & mask
