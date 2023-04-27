"""
Module: sum
Description: various implementations of summing a list
"""
import sys

print("\nstarting...\n")


# code goes here

def main(args):
    args = [int(arg) for arg in args]
    print(f"Main was called with the following arguments: {args}")
    sumArgs(args)

def sumArgs(args):
    print(f"the sum of the following numbers: {args} is {sum(args)}")

if __name__ == "__main__":
    main(sys.argv[1:])
