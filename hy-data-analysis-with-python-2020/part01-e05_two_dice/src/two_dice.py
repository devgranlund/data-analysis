#!/usr/bin/env python3

def main():
    dice = [1,2,3,4,5,6]
    for d1 in dice:
        for d2 in dice:
            if d1+d2 == 5:
                string = "("+str(d1)+","+str(d2)+")"
                print(string)

if __name__ == "__main__":
    main()
