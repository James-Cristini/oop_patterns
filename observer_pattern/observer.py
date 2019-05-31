# 2.7
### Observer pattern - one to many relationship whereby the one (the observed) object changes state all
## of its dependents are notified and updated automatically
##

from __future__ import print_function


### ========
# Interfaces
### ========
class IObservable(object):
    """ Interface for Observable object. """

    def add_observer(self, observer):
        raise NotImplementedError("Add observer method not yet implemented.")

    def remove_abserver(self, observer):
        raise NotImplementedError("Remove observer method not yet implemented.")

    def notify(self):
        raise NotImplementedError("Notify method not yet implemented.")


class IObserver(object):
    """ Interface for Observer object. """

    def update(self, observer):
        raise NotImplementedError("Update method not yet implemented.")

    def confirm_removed(self, observer):
        raise NotImplementedError("Confirm removed method not yet implemented.")


### =============
# Implementations
### =============
class Observable(IObservable):
    """ Abstract Observable object. """
    observers = []

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        print('Setting attribute for this object')
        self._name = new_name
        self.notify()

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_abserver(self, observer):
        print('Removing {0} from list of observers'.format(observer.name))
        self.observers.remove(observer)
        observer.confirm_removed()

    def notify(self):
        print('Notifying observers')
        for obs in self.observers:
            obs.update() # This is push-pull pattern
            # we could send the data via update to make this push-push

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

class Observer(IObserver):
    """ Abstract Observer object. """
    def __init__(self, name, observable):
        self.name = name
        self.observable = observable
        self.observables_attr = self.observable.name
        self.observable.add_observer(self)

    def update(self):
        print("Updating object")
        self.observables_attr = self.observable.name

    def confirm_removed(self):
        print("This object was successfully unsubscribed.")

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name


def main():
    # Instantiate obervables and observers
    O = Observable('MY NAME')
    a = Observer('observer_A', O)
    b = Observer('observer_B', O)

    print('O', O.name)
    print('a', a.observables_attr)
    print('b', b.observables_attr)

    # Change observables attribute
    O.name = 'Completely new name'

    print('O', O.name)
    print('a', a.observables_attr)
    print('b', b.observables_attr)

    # Remove/unsubscribe an observer
    print("Observers list:", O.observers)
    O.remove_abserver(a)
    print("Observers list:", O.observers)

    # Change the name and see which observers are updated
    O.name = 'Another new name'

    print('O', O.name)
    print('a', a.observables_attr)
    print('b', b.observables_attr)

    # Add an observer
    O.add_observer(a)
    print("Observers list:", O.observers)

    # Change observables name once more to see which were updated
    O.name = 'The final new name'

    print('O', O.name)
    print('a', a.observables_attr)
    print('b', b.observables_attr)

if __name__ == '__main__':
    main()