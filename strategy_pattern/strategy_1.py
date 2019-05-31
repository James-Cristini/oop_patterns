# 2.7
### Simple Strategy Pattern Example of using interchangable behaviors which can be defined 'at runtime' rather than Inheritance
## Goal is to keep the algorithms/behaviors separate from the client so that these algorithms can change or be altered without
## needing to make changes to the "client"

from __future__ import print_function


### ========
# Interfaces
### ========

class IDisplayBehavior(object):
    def __init__(self):
        pass

    def display(self):
        """ How should the object be displayed. """
        raise NotImplementedError("Display Behavior not yet implemented.")

    def __call__(self):
        """ Using __call__ allows us to pass in the class itself "as" the behavior's method. """
        self.display()


class IQuackBehavior(object):
    def __init__(self):
        pass

    def quack(self):
        """ How does the object quack. """
        raise NotImplementedError("Quack Behavior not yet implemented.")

    def __call__(self):
        """ Using __call__ allows us to pass in the class itself "as" the behavior's method. """
        self.quack()


class IFlyBehavior(object):
    def __init__(self):
        pass

    def fly(self):
        """ How does the object fly. """
        raise NotImplementedError("Fly Behavior not yet implemented.")

    def __call__(self):
        """ Using __call__ allows us to pass in the class itself "as" the behavior's method. """
        self.fly()


### =============
# Implementations
### =============

class CanFlyBehavior(IFlyBehavior):
    """ For objects that can fly high. """

    def fly(self):
        print("This duck is flying high!")


class CannotFlyBehavior(IFlyBehavior):
    """ For objects that cannot fly. """
    def fly(self):
        print("This duck is grounded!")


class CanQuackBehavior(IQuackBehavior):
    """ For objects that can quack loudly. """

    def quack(self):
        print("This duck is quacking loudly!")


class CannotQuackBehavior(IQuackBehavior):
    """ For mute objects that cannot quack. """

    def quack(self):
        print("This duck is mute!")


class DisplayGraphicallyBehavior(IDisplayBehavior):
    """ For objects that are to be displayed graphically. """

    def display(self):
        print("This duck is looking good!")

class DisplayAsTextBehavior(IDisplayBehavior):
    """ For objects that are to be displayed as text. """

    def display(self):
        print("This duck is just text!")


class Duck(object):
    def __init__(self, display_behavior, quack_behavior, fly_behavior):
        self.display = display_behavior
        self.quack = quack_behavior
        self.fly = fly_behavior


def main():
    # Create instances where behaviors are passed in allowing us to more felxibly create Duck objects as needed
    rubber_duck = Duck(DisplayGraphicallyBehavior(), CanQuackBehavior(), CannotFlyBehavior())
    rubber_duck.quack()
    rubber_duck.fly()
    rubber_duck.display()

    quiet_wild_duck = Duck(DisplayGraphicallyBehavior(), CannotQuackBehavior(), CanFlyBehavior())
    quiet_wild_duck.quack()
    quiet_wild_duck.fly()
    quiet_wild_duck.display()

    grounded_quiet_text_duck = Duck(DisplayAsTextBehavior(), CannotQuackBehavior(), CannotFlyBehavior())
    grounded_quiet_text_duck.quack()
    grounded_quiet_text_duck.fly()
    grounded_quiet_text_duck.display()

if __name__ == '__main__':
    main()