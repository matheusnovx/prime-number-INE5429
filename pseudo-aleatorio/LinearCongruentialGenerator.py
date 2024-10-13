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


class LinearCongruentialGenerator:
    def __init__(self, seed: int, m: int, a: int = 1664525, c: int = 1013904223):
        self.seed = seed
        self.m = m
        self.a = a
        self.c = c

    def next(self) -> int:
        self.seed = (self.a * self.seed + self.c) % self.m
        return self.seed
