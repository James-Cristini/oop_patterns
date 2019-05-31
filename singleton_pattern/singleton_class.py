from __future__ import print_function


class MySingleton(object):
    _instance = None

    def __new__(self):
        if not self._instance:
            self._instance = super(MySingleton, self).__new__(self)
            self.y = 10

        return self._instance

    def __init__(self):
        pass

def main():
    # Create singleton instance object
    x = MySingleton()

    # View the single instance's y value
    print('x.y', x.y)

    # Change and view the single isntance's y value
    x.y = 20
    print('x.y', x.y)

    # Create a 'new' instance of the singleton
    z = MySingleton()

    # See that the new instance's y value is not 10 because it is not a new instance
    print('z.y', z.y)

    # Proof it is in fact the same object
    print(z is x)

if __name__ == '__main__':
    main()