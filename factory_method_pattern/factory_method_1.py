### Factory method
##

from __future__ import print_function

### ========
# Interfaces
### ========
class IAnimal(object):

    def walk(self):
        raise NotImplementedError("Walk method not yet implemented.")

    def talk(self):
        raise NotImplementedError("Talk method not yet implemented.")


class IAnimalFactory(object):

    def create_animal(self):
        raise NotImplementedError("Create animal method not yet implemented.")

### =============
# Implementations
### =============
class Animal(IAnimal):
    def __init__(self, name, sound, num_legs):
        self.name = name
        self.sound = sound
        self.num_legs = num_legs

    def walk(self):
        print("{0} is walking around on its {1} legs".format(self.name, self.num_legs))

    def talk(self):
        print("{0} says: {1}!".format(self.name, self.sound))


class AnimalFactory(IAnimalFactory):

    animals = []

    def create_animal(self, name, sound, num_legs):
        # Insert additional creation logic (e.g. randomization, balance, based on outside states)
        animal = Animal(name, sound, num_legs)
        self.animals.append(animal)
        return animal


def main():
    animal_factory = AnimalFactory()
    cat = animal_factory.create_animal('Kitty', 'meow', 4)
    dog = animal_factory.create_animal('Doggy', 'bark', 4)
    ant = animal_factory.create_animal('Antibody', '...', 6)
    bee = animal_factory.create_animal('Beezle', 'buzz buzz', 6)

    cat.walk()
    cat.talk()

    dog.walk()
    dog.talk()

    ant.walk()
    ant.talk()

    bee.walk()
    bee.talk()

if __name__ == '__main__':
    main()