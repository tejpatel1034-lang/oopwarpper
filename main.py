"""
--- Choose another operation ---
"""

print("\n---Python OOP Project: Employee Management System---\n")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Employee(Person):
    def __init__(self, name, age, emp_id, salary):
        super().__init__(name, age)
        self.__emp_id = emp_id
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        self.__salary = value

    def display(self):
        super().display()
        print("Employee ID:", self.__emp_id)
        print("Salary:", self.__salary)


class Manager(Employee):
    def __init__(self, name, age, emp_id, salary, department):
        super().__init__(name, age, emp_id, salary)
        self.department = department

    def display(self):
        super().display()
        print("Department:", self.department)

person = []
employee = []
manager = []

while True:
    print("Choose an operation:")
    print("1. Create Person")
    print("2. Create Employee")
    print("3. Create Manager")
    print("4. Show Details")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    match choice:

        case 1:
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            person.append(Person(name, age))
            print(f"\nPerson created with name: {name} and age: {age}.")

        case 2:
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            emp_id = input("Enter Employee ID: ")
            salary = float(input("Enter Salary: "))
            employee.append(Employee(name, age, emp_id, salary))
            print(f"\nEmployee created with name: {name}, age: {age}, ID: {emp_id} and salary: ${salary}.")

        case 3:
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            emp_id = input("Enter Employee ID: ")
            salary = float(input("Enter Salary: "))
            dept = input("Enter Department: ")
            manager.append(Manager(name, age, emp_id, salary, dept))
            print(f"\nManager created with name: {name}, age: {age}, ID: {emp_id}, salary: ${salary} and department: {dept}.")

        case 4:
            print("\n1. Person")
            print("2. Employee")
            print("3. Manager")

            show = int(input("Enter choice: "))

            match show:
                case 1 if person:
                    print("\nPerson Details:")
                    for p in person:
                        p.display()
                        print()

                case 2 if employee:
                    print("\nEmployee Details:")
                    for e in employee:
                        e.display()
                        print()

                case 3 if manager:
                    print("\nManager Details:")
                    for m in manager:
                        m.display()
                        print()

                case _:
                    print("Object not created yet")

        case 5:
            print("Exiting the system. All resources have been freed.")
            print("\nGoodbye!")
            break

        case _:
            print("Invalid choice")

    print(__doc__)
