"""
Concepts used in this example:
1. partial: pre-fills some arguments of a function.
2. Currying: creating nested functions where each call adds one argument.
3. Function composition: building specialized functions from general ones.
4. Closures: inner functions remember variables from the outer function.
"""

from functools import partial


def fun(a, b, c, x):
    return a + b + c + x


print(fun(1, 2, 3, 4))

# partial binds the first arguments and leaves the rest for later use.
g = partial(fun, 10, 20, 30)

print(g(100))
print(g(200))
print(g(300))

print("_" * 60)


def greet(msg):
    def inner(sep):
        def inner_most(name):
            return f"{msg}{sep}{name}"

        return inner_most

    return inner


# Currying: one function returns another function, step by step.
res_sep_1 = greet("Happy Deebawali")
res_name_1 = res_sep_1("===>>>")
print(res_name_1("Krish Srikanth"))
print(res_name_1("Ravi Ashwin"))
print(res_name_1("Dinesh karthick"))
print("_" * 60)

res_sep_2 = greet("Happy Deepavali")
res_name_2 = res_sep_2("===>>>")
print(res_name_2("Srinath"))
print(res_name_2("prasad"))
print(res_name_2("rahul"))
print("_" * 60)

res_sep_2 = greet("Happy Diwali")
res_name_2 = res_sep_2("===>>>")
print(res_name_2("Sewag"))
print(res_name_2("Sachin"))
print(res_name_2("Yuvi"))
print("_" * 60)




