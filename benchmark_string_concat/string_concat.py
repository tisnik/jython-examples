#!/usr/bin/env python
# vim: set fileencoding=utf-8

from sys import argv, exit


def perform_benchmark(repeat_count):
    s = ""
    for i in range(1, 1 + repeat_count):
        s += str(i) + " "

    print(len(s))
    return s


if __name__ == "__main__":
    if len(argv) < 2:
        print("usage: python string_concat repeat_count")
        exit(1)

    repeat_count = int(argv[1])
    perform_benchmark(repeat_count)
