#!/usr/bin/env python3
"""A simple calculator for testing the zelvinator bot."""

def add(a: int, b: int) -> int:
    return a + b

def subtract(a: int, b: int) -> int:
    return a - b

def multiply(a: int, b: int) -> int:
    return a * b

def divide(a: int, b: int) -> int:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 4:
        print("Usage: calc.py <op> <a> <b>")
        print("Operations: add, sub, mul, div")
        sys.exit(1)
    op, a, b = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
    ops = {"add": add, "sub": subtract, "mul": multiply, "div": divide}
    if op not in ops:
        print(f"Unknown operation: {op}")
        sys.exit(1)
    print(ops[op](a, b))

def modulo(a: int, b: int) -> int:
    return a % b
