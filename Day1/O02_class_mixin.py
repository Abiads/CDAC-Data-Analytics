
"""
Concepts used in this example:
1. Inheritance: child classes inherit attributes and methods from parent classes.
2. Mixin: a class that provides extra reusable behavior without being a main class.
3. Introspection: examining object attributes dynamically using vars() and getattr().
4. Method Resolution Order (MRO): Python searches parent classes in order for methods.
"""

class StateMixin:
    """Reusable behavior for showing the current object's attributes."""

    def ShowState(self):
        # vars(self) returns the dictionary of instance attributes
        # Example: {'id': 101, 'name': 'Sachin', 'age': 51}
        # getattr(self, mem) fetches the value of each attribute by name
        members = {mem: getattr(self, mem) for mem in vars(self)}#Introspecting the attributes of the object
        print(members)


class Person:
    """Parent class for a person object."""

    def __init__(self):
        self.id = 101
        self.name = "Sachin"
        self.age = 51


class Employee:
    """Parent class for an employee object."""

    def __init__(self):
        self.eid = 1001
        self.e_name = "tendulkar"
        self.salary = 100
        self.dept = "cricket"


class Product:
    """Parent class for a product object."""

    def __init__(self):
        self.p_pid = 111
        self.p_name = "nail polish"
        self.price = 125
        self.p_qty = 10
# what is introspecting classes in python?
# Introspecting classes in Python refers to the ability to examine the attributes, methods, 
# and properties of a class or an object at runtime. This allows developers to dynamically inspect and interact with classes and objects,
#  enabling features like debugging, serialization, and dynamic method invocation. Python provides
#  built-in functions and modules for introspection, such as `dir()`, `vars()`, `getattr()`, `hasattr()`, and the `inspect` module.
#example of introspecting classes in python
#ar

# A class can inherit from both a normal base class and a mixin.
# The mixin provides the ShowState() method to all introspecting classes.
class PersonIntrospect(Person, StateMixin):
    pass


class EmployeeIntrospect(Employee, StateMixin):
    pass


class ProductIntrospect(Product, StateMixin):
    pass


# Object creation
person_intro = PersonIntrospect()
employee_intro = EmployeeIntrospect()
product_intro = ProductIntrospect()

# Calling the mixin method prints all attributes of each instance.
person_intro.ShowState()
employee_intro.ShowState()
product_intro.ShowState()
