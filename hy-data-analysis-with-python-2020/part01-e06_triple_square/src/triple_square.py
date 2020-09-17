#!/usr/bin/env python3


def main():
    for i in range(1, 10):
        tripl = triple(i)
        sqr = square(i)
        if sqr <= tripl:
            string = "triple(" + str(i) + ")==" + str(tripl) + " square(" + str(i) + ")==" + str(sqr)
            print(string)
        else:
            break


def triple(i):
    return i * 3


def square(i):
    return i ** 2


if __name__ == "__main__":
    main()
