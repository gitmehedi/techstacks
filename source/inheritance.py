class Animal:
    name = ""
    age = 20

    def eat(self):
        print("I can eat {}".format(self.name))


class Dog(Animal):
    def display(self):
        print("My name is {0} and age is {1}".format(self.name,self.age))


labrador = Dog()

labrador.name = "Rohu"
labrador.age = 30
labrador.eat()
labrador.display()


# Multiple Inheritance: 

class Mother:
    mothername = ""

class Father:
    fathername = ""

class Son(Mother,Father):
    name = ""
    def parents(self):
        print("{0} parents is {1} and {2}".format(self.name,self.fathername,self.mothername))


son = Son()
son.mothername = "tammanna"
son.fathername = "swapon"
son.name="sudha"
son.parents()



# Multilevel Inheritance :

class GrandFather:
    def __init__(self,grandfather):
        self.grandfather=grandfather

class Father(GrandFather):
    def __init__(self, father,grandfather):
        self.father=father
        GrandFather.__init__(self,grandfather)

class Son(Father):
    def __init__(self, son, father, grandfather):
        self.name = son
        Father.__init__(self,father,grandfather)

    def print_name(self):
        print('Grandfather name :', self.grandfather)
        print("Father name :", self.father)
        print("Son name :", self.name)

s1 = Son('Prince','Rampa','Lal Mia')
print(s1.print_name())