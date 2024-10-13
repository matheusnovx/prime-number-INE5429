"""
    Park-Miller pseudo-random number generator.
    -------------------------------------------
    The Park-Miller random number generator is a simple and fast pseudo-random number generator.
    It is defined by the recurrence relation:
    X_{n+1} = (aX_n) mod m
    where X_0 is the seed, and a and m are constants.

    Using the parameters cited in the page https://en.wikipedia.org/wiki/Lehmer_random_number_generator#Parameters_in_common_use
    "In 1988, Park and Miller[3] suggested a Lehmer RNG with particular parameters m = 231 − 1 = 2,147,483,647 (a Mersenne prime M31) and a = 75 = 16,807 (a primitive root modulo M31), now known as MINSTD."
    But, m is being used as 2 ** lenght, where lenght is the number of bits.
"""


class ParkMiller:
    def __init__(self, seed: int, m: int, a: int = 16807):
        self.seed = seed
        self.a = a
        self.m = m

    def next(self) -> int:
        self.seed = (self.a * self.seed) % self.m
        return self.seed
