# class with static variable in Python to auto generate id

class Employee:
    idGenerator=100
    def __init__(self, name, salary):
        Employee.idGenerator+=1
        self.id=Employee.idGenerator
        self.name=name
        self.salary=salary

    def show(self):
        print("---------------")
        print(self.id)
        print(self.name)
        print(self.salary)
        
    def __str__(self):
       return str(self.id)+"-"+self.name+"-"+str(self.salary)


