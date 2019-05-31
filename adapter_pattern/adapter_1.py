### Adapter pattern example

from __future__ import print_function

class ITarget(object):
    """ Interface to be used for the adapter. """

    def request(self):
        raise NotImplementedError("Request method not yet implemented.")


class Adapter(ITarget):
    """ Adapter object for adapting an adaptee's new 'specific_request' method to the 'old way' of calling just request. """

    def __init__(self, adaptee):
        """ Accepts the adaptee in constructor. """

        self.adaptee = adaptee

    def request(self):
        """ Adapted method for request -> specific_request. """

        print("Calling Adapter's specific_request method")
        self.adaptee.specific_request()


class Adaptee(object):
    """ Adaptee object which will need to be adapted to in order call the new 'specific_request' method. """

    def specific_request(self):
        """ Adaptee specific method. """

        print("Making Adaptee's specific request.")


def main():
    # Set up adaptee object
    that_adaptee = Adaptee()

    # Set up adapter
    my_adapter = Adapter(that_adaptee)

    # Call adapter's request method
    my_adapter.request()

if __name__ =='__main__':
    main()