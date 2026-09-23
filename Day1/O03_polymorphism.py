"""
Concepts used in this example:
1. Polymorphism: different classes can share the same method name and be used uniformly.
2. Abstract Base Class (ABC): defines common interface for derived classes.
3. Abstract method: method declared in base class but implemented in child classes.
4. Dynamic object creation: using class metadata to instantiate subclasses.
"""

from abc import ABC, abstractmethod


# Abstract Base Class defines the required common behavior.
# Any subclass must implement do_job().
class Account(ABC):
    @abstractmethod
    def do_job(self):
        pass


# Business() accepts a list of account objects and calls the same method name.
# Even though each account type behaves differently, the interface is the same.
def Business(acc_lst):
    print("Business Started")
    for acc in acc_lst:
        acc.do_job()  # Polymorphism: same method, different implementation
    else:
        print("Completed All account type verification")
    print("Business Completed")


print("_" * 60)
# -----------------------------------------------------


class Savings(Account):
    def do_job(self):
        print("Savings job done")


class Current(Account):
    def do_job(self):
        print("Current job done")


class DMat(Account):
    def do_job(self):
        print("DMat job done")


class OD(Account):
    def do_job(self):
        print("OD job done")


# acc = Account()  # Can't instantiate abstract class Account

# sa = Savings()
# curr = Current()
# dmat = DMat()

# Business([sa, curr, dmat])
# sub_classes = [sub for sub in Account.__subclasses__()]
sub_classes = [sub.__name__ for sub in Account.__subclasses__()]
print(sub_classes)
str_class_name = "Savings"
# sub_object = [eval(f"{str_class_name}()")]
sub_object = [eval(f"{sub.__name__}()") for sub in Account.__subclasses__()]
Business(sub_object)
