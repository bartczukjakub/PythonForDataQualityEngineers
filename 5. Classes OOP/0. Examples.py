class Pet:
    def __init__(self, name = 'noname', sound = 'uuuu'):
        self.name = name
        self.sound = sound
        self.age = 0

    def make_sound(self):
        print(self.sound)

    def increase_age(self):
        self.age += 1

    def sleep(self):
        print('Zzz...')

pet1 = Pet('Jack', 'rrrrr')

#pet1.make_sound()
#print(pet1.age)
#pet1.increase_age()
#print(pet1.age)

class Dog(Pet):
    def __init__(self, name= 'John', sound= 'woof'):
        Pet.__init__(self, name, sound)
        self.weight = 5

    def eat(self):
        self.weight += 0.5


#dog1 = Dog()
#dog1.make_sound()
#print(dog1.weight)
#dog1.eat()
#print(dog1.weight)


class Cat(Pet):
    def __init__(self, name= 'Sonia', sound= 'Meow'):
        Pet.__init__(self, name, sound)
        self.weight = 4

    def eat(self):
        self.weight += 0.4

    def make_sound(self):
        print(self.sound)


#cat1 = Cat()
#print(cat1.weight)
#cat1.eat()
#print(cat1.weight)
#cat1.make_sound()