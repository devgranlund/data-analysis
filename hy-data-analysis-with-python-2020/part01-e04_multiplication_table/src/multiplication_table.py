#!/usr/bin/env python3


def main():
    for j in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
        row = ""
        for i in [1,2,3,4,5,6,7,8,9,10]:
            row = row + str(i*j) + " "
        print(row)


if __name__ == "__main__":
    main()
