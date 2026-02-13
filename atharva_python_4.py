class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def myfunction(self, name, age):
        self.name = name
        self.age = age
class Employee(Person):
    def __init__(self, name, age, emp_id, salary):
        Person.myfunction(self, name, age)   
        self.emp_id = emp_id
        self.salary = salary
class Manager(Employee):
    def __init__(self, name, age, emp_id, salary, department):
        Employee.__init__(self, name, age, emp_id, salary)
        self.department = department
m = Manager("Rahul", 35, 101, 75000, "IT")
print(m.name, m.age, m.emp_id, m.salary, m.department)