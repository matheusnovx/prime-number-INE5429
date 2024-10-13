"""
    Linear Congruential Generator
    -----------------------------
    The linear congruential generator is a very simple example of a pseudo-random number generator.
    It is defined by the recurrence relation:
    X_{n+1} = (aX_n + c) mod m
    where X_0 is the seed, and a, c and m are constants.
"""

class LinearCongruentialGenerator:
    def __init__(self, seed : int, a : int, c : int, m : int):
        self.seed = seed
        self.a = a
        self.c = c
        self.m = m

    def next(self) -> int:
        self.seed = (self.a * self.seed + self.c) % self.m
        return self.seed