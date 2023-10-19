class Employee:
    idGen=100
    def __init__(self, name,dept):
        Employee.idGen+=1
        self.ID=Employee.idGen
        self.name=name
        self.dept=dept
    def show(self):
        print("Id:",self.ID)
        print("Name:",self.name)
        print("Dept:",self.dept)

class PermanentEmployee(Employee):
     def __init__(self,name,dept,salary):
         super().__init__(name,dept)
         self.salary=salary
     def show(self):
        super().show()
        print("Salary:",self.salary)

class ContractEmployee(Employee):
    def __init__(self,name,dept,period,amount):
         super().__init__(name,dept)
         self.period=period
         self.amount=amount
    def show(self):
        super().show()
        print("Period:",self.period)
        print("Amount:",self.amount)

pe1=PermanentEmployee("Jenney","Admin",75000.00)
pe1.show()
ce1=ContractEmployee("Mary","Sales",3,300000.00)
ce1.show()


        
