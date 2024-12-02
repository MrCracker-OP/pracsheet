# Base class: Employee
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_details(self):
        return f"Name: {self.name}, Salary: {self.salary}"

# Derived class: Manager
class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)  # Initialize the base class attributes
        self.department = department

    # Override the get_details method
    def get_details(self):
        return f"Name: {self.name}, Salary: {self.salary}, Department: {self.department}"

# Example usage
employee = Employee("Alice", 50000)
manager = Manager("Bob", 80000, "Sales")

# Printing details
print(employee.get_details())  # Output: Name: Alice, Salary: 50000
print(manager.get_details())   # Output: Name: Bob, Salary: 80000, Department: Sales
