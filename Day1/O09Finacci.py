"""
Concepts used in this example:
1. Generator function: yields values one by one without storing the whole sequence.
2. Fibonacci sequence: a series where each number is sum of previous two.
3. Lazy evaluation: computation happens only when next value is requested.
"""


def fib(n):
    curr = 1
    prev = 0
    index = 1
    yield prev
    while index < n:
        yield curr
        prev, curr = curr, prev + curr
        index += 1


for num in fib(10):
    print(num, end="\t:\t")
print()

