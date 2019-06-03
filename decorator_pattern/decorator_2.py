
class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return '{0} is {1} years old'.format(self.name, self.age)


class PersonDecorator(Person):
    def __init__(self, person):
        self._person = person

    def __getattr__(self, name):
        return getattr(self._person, name)

    def __str__(self):
        age = self._person.age
        wrap_text = ' *** '
        return '{0}{1}{2}'.format(wrap_text, self._person.__str__(), wrap_text)

def main():
    p = []

    p.append(Person('Mike', 25))
    p.append(Person('Kay', 22))
    p.append(Person('John', 42))
    p.append(Person('Tom', 33))

    for person in p:
        person = PersonDecorator(person)
        print person

if __name__ == '__main__':
    main()
