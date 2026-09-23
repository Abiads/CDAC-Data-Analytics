"""
Concepts used in this example:
1. Context manager: manages setup and cleanup around a block of code.
2. with statement: executes __enter__() before block and __exit__() after block.
3. Resource management: useful for files, locks, DB connections, etc.
"""

'''
Develop a context manager
1. context manager work with "with" statements
'''


class CA:
    def __init__(self):
        print("self", id(self))

    def fun(self):
        print("fun")

    # __enter__ runs when entering the with block.
    def __enter__(self):
        print("Enter")
        return self

    # __exit__ runs when leaving the with block, even if an exception happens.
    def __exit__(self, exc_type, exc, tb):
        print("Exit")


# obj = CA()
# print(id(obj))

obj1 = CA()
with obj1:
    obj1.fun()
    # print(id(obj1))

