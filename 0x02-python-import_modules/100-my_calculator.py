#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv
    num_arg = len(argv)
    if num_arg != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif argv[2] == '+':
        print(f"{int(argv[1])} + {int(argv[3])} = " 
                f"{add(int(argv[1]), int(argv[3]))}")
    elif argv[2] == "-":
        print(f"{int(argv[1])} - {int(argv[3])} = "
                f"{sub(int(argv[1]), int(argv[3]))}")
    elif argv[2] == '*':
        print(f"{int(argv[1])} * {int(argv[3])} = "
                f"{mul(int(argv[1]), int(argv[3]))}")
    elif argv[2] == "/":
        print(f"{int(argv[1])} / {int(argv[3])} = "
                f"{div(int(argv[1]), int(argv[3]))}")
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
