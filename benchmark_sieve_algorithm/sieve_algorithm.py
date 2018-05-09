#!/usr/bin/env python
# vim: set fileencoding=utf-8

from sys import argv


def sieve(n):
    multiples = set()
    for i in range(2, n+1):
        if i not in multiples:
            yield i
            multiples.update(range(i*i, n+1, i))


if __name__ == "__main__":
    if len(argv) < 2:
        print("usage: python sieve_algorithm repeat_count")
        exit(1)

    max_value = int(argv[1])
    primes = list(sieve(max_value))
    print(len(primes))
