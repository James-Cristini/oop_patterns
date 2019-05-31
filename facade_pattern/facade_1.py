### Facade pattern provide a unified interface to a set of interfaces in a subsystem
### defines a higher level interface that makes the subsystem easier to use

from __future__ import print_function


class IObject(object):
    def __init__(self, name):
        self.name = name

    def some_method(self):
        raise NotImplementedError("Method some_method not yet implemented.")

class MyObject1(IObject):
    """ Some Object 1 with a method that will need to be invoked. """

    def some_method(self):
        print("Calling {0}'s some_method.".format(self.name))


class MyObject2(IObject):
    """ Some Object 2 with a method that will need to be invoked. """

    def some_method(self):
        print("Calling {0}'s some_method.".format(self.name))


class MyObject3(IObject):
    """ Some Object 3 with a method that will need to be invoked. """

    def some_method(self):
        print("Calling {0}'s some_method.".format(self.name))


class Facade(object):
    """ Facade object which will make interfacing with MyObject{1,2,3} easier. """

    def __init__(self, obj1, obj2, obj3):
        self.obj1 = obj1
        self.obj2 = obj2
        self.obj3 = obj3

    def obj1_method(self):
        self.obj1.some_method()

    def obj2_method(self):
        self.obj2.some_method()

    def obj3_method(self):
        self.obj3.some_method()


def main():
    object_1 = MyObject1('OBJ_1')
    object_2 = MyObject2('OBJ_2')
    object_3 = MyObject3('OBJ_3')

    facade = Facade(object_1, object_2, object_3)

    facade.obj1_method()
    facade.obj2_method()
    facade.obj3_method()

if __name__ == '__main__':
    main()