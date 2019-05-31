def singleton(myClass):
    instances = {}

    def getInstance(*args, **kwargs):
        if myClass not in instances:
            instances[myClass] = myClass(*args, **kwargs)

        return instances[myClass]

    return getInstance


@singleton
class Animal(object):
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def talk(self):
        print('{0} says: {1}!'.format(self.name, self.sound))

def main():
    # Create a singleton animal object
    x = Animal('Kitty', 'Meow')
    x.talk()

    # Try to create a second singleton animal object and see that it is not as specified
    y = Animal('Doggy', 'Bark')
    y.talk()

    # Prove the 2 are in fact the same
    print(x is y)

if __name__ == '__main__':
    main()