
"""
== Pisano period Sequence ==

In number theory, the nth Pisano period, written as π(n), is the period with which the sequence of Fibonacci numbers taken modulo n repeats.

https://en.wikipedia.org/wiki/Pisano_period

OEIS: A001175

"""

# Author : Darío Clavijo (https://github.com/daedalus)

import sys


def pisano_period(m):
    """
    
    """
    if m == 1:
        return 1
    a = b = 1
    n = i = 0
    while i <= (m**2):
        b, a = a, (a + b) % m
        if a == 1 and b == 0:
            return n + 2
        n += 1


if __name__ == "__main__":
    for i in range(1, 100):
        print((pisano_period(i)))
