class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def eat(self):
        print('{} is eating.'.format(self.name))


dog = Animal('aaa',123)
dog.eat()


class Dog(Animal):
    def __init__(self,name,age,color):
        Animal.__init__(self,name,age)
        self.color = color
