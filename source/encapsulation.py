class Employee:
    # constructor
    def __init__(self, name, salary, project):
        # data members
        self.name = name

        # protected members only accessible through within class or subclasses
        self._salary = salary

        # private members only accessible through within class
        self.__project = project

    # method
    # to display employee's details
    def show(self):
        # accessing public data member
        print("Name: ", self.name, 'Salary:', self._salary)

    # method
    def work(self):
        print(self.name, 'is working on', self.__project)

# creating object of a class
emp = Employee('Jessa', 8000, 'NLP')

# calling protected property
print(emp._salary)

# calling private property
print(emp.__project)

# calling public method of the class
emp.show()
emp.work()