### Provides a surogate or placeholder for another object in order to control access to it
# Instead of calling the thing you want to call, you call a thing that calls the thing you want to call
# Remote: When you to access a resource outside the 'safe' boundaries of your application
# Virtual: controls access to a resource that is expensive to create
# Protection: Controls access to a resource based on access rights


from __future__ import print_function
import time


### ========
# Interfaces
### ========

class ISubject(object):
    """ Subject interface to be used by both the RealSubject and the Proxy objects. """

    def __init__(self):
        pass

    def request(self):
        raise NotImplementedError("Request method not yet implemented")


### =============
# Implementations
### =============

class Subject(ISubject):
    """ The real subject or resource, typically something with expensive operations. """

    def __init__(self, name):
        self.name = name

    def request(self, value):
        """ Some expensive method. """

        print("Executing {0}'s request method for value: {1}".format(self.name, value))
        time.sleep(1.2)
        return "FIXED: {0}".format(value.upper())


class Proxy(ISubject):
    """ Proxy object which will reduce need to call the real subject's expensive operations everytime. """

    real_subject = None
    response_cache = {}

    def __init__(self, name, subject):
        """ Expcts subject as a Class definition and not an instance of that class! """
        self.name = name
        self.subject = subject

    def request(self, value):
        """ Proxy request, cache response values to return faster and reduce uneeded expensive calls. """

        print('Executing {0}s request method'.format(self.name))

        # Instantiate the real subject only when it is needed
        if not self.real_subject:
            print("Instantiating the real subject")
            time.sleep(2.5)
            self.real_subject = self.subject('The Real Subject')

        try: # Check cache for request response
            response = self.response_cache[value]
            print("This response has been previously cached and returns faster.")
            time.sleep(.2)
            print('.')

        except KeyError: # Call and add to cache if not there
            response = self.real_subject.request(value)
            self.response_cache[value] = response
            print("This response was not found in the cache but has been added")

        return response


def main():

    # Set up proxy object
    subject_proxy = Proxy('The Subject Proxy', Subject)

    # Make initial calls to the real subject via proxy object
    print(subject_proxy.request('Test_1'))
    print(subject_proxy.request('Test_2'))
    print(subject_proxy.request('Test_3'))

    # Make repeated calls via the proxy and see the improvement
    print(subject_proxy.request('Test_1'))
    print(subject_proxy.request('Test_3'))

if __name__ == '__main__':
    main()