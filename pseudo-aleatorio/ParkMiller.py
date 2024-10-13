"""
    Park-Miller pseudo-random number generator.
    -------------------------------------------
    The Park-Miller random number generator is a simple and fast pseudo-random number generator.
    It is defined by the recurrence relation:
    X_{n+1} = (aX_n) mod m
    where X_0 is the seed, and a and m are constants.
"""

class ParkMiller:
    def __init__(self, seed: int, a: int, m: int):
        self.seed = seed
        self.a = a
        self.m = m

    def next(self) -> int:
        self.seed = (self.a * self.seed) % self.m
        return self.seed