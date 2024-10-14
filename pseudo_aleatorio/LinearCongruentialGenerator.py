"""
    Linear Congruential Generator
    -----------------------------
    The linear congruential generator is a very simple example of a pseudo-random number generator.
    It is defined by the recurrence relation:
    X_{n+1} = (aX_n + c) mod m
    where X_0 is the seed, and a, c and m are constants.

    Using parameters as default as cited in the 'Parameters in common use' section of the page: https://en.wikipedia.org/wiki/Linear_congruential_generator.
    Where a = 1664525, c = 1013904223 came from Numerical Recipes Chapter 7.1, §An Even Quicker Generator, Eq. 7.1.6 parameters from Knuth and H. W. Lewis
"""
from time import time_ns


class LinearCongruentialGenerator:
    def __init__(self, m: int, a: int = 1664525, c: int = 1013904223):
        self.m = m  # Modulo
        self.a = a
        self.c = c

    def lcg(self, n_bits, seed=None):
        # Máscara para limitar os bits gerados
        mask = (1 << n_bits) - 1
        m, a, c = 2 ** 32, self.a, self.c

        # Define o seed com base no tempo atual se não for fornecido
        if seed is None:
            seed = time_ns() % m

        number_generated = (a * seed + c) % m
        final_result = 0
        bits_generated = 0

        # Gera números até alcançar a quantidade desejada de bits
        while bits_generated < n_bits:
            number_generated = (a * number_generated + c) % m
            new_generated = number_generated & ((1 << 32) - 1)

            final_result = (final_result << 32) | new_generated
            bits_generated += 32

        return final_result & mask

