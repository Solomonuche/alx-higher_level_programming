#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    n = len(argv)
    if n == 1:
        print(f"{n - 1} arguments.")
    else:
        print(f"{n - 1} arguments:")
    for i in range(1, n):
        print(f"{i}: {argv[i]}")
