"""
Concepts used in this example:
1. Higher-Order Functions (HOF): functions that accept or return other functions.
2. Decorators: modify behavior of a function without changing its logic.
3. Callable objects: classes with __call__ can be used like functions.
4. Callback pattern: a function passed to another function for later execution.
"""

# HOF / decorator example
import time

# This is the traditional function-based decorator idea.
# def introspect_time(fnc):
#     def inner_fun(*arg,**kwargs):
#         start = time.time()
#         result = fnc(*arg,**kwargs)  # callback
#         end = time.time()
#         print(f"Time Taken is {end - start}")
#         return result
#     return inner_fun


# Class-based decorator using __call__.
# A callable object behaves like a function when invoked.
class introspect_time:
    def __init__(self, fnc):
        self.fnc = fnc

    def __call__(self, *args, **kwds):
        start = time.time()
        result = self.fnc(*args, **kwds)  # callback
        end = time.time()
        print(f"Time Taken is Class : [ {end - start} ]")
        return result


# @introspect_time is decorator syntax.
# Python automatically passes add_fun to introspect_time.__init__ and wraps it.
@introspect_time
def add_fun(x, y):
    time.sleep(1)
    return x + y


@introspect_time
def print_list(lst):
    for index, item in enumerate(lst):
        time.sleep(0.25)
        print(f"{index} -> {item}", end="\t:\t")
    print()

#traditional way of using decorator without @ syntax
# # add_fun = introspect_time(add_fun(10,20)) 
# add_fun = introspect_time(add_fun)   
# print_list = introspect_time(print_list)
# print(f"{add_fun(10, 20)}")


# print("addfun ", add_fun.__name__)
# print("print_list ", print_list.__name__)

res1 = add_fun(10, 20)
print("result add ", res1, sep="\t:\t")
print("_" * 60)

# List comprehension + HOF combination example
# lst1 = list(map(lambda x:x**3,filter(lambda x:x>4, range(1,11))))

lst = [x**2 for x in range(1, 11) if x > 4]
print_list(lst)





 