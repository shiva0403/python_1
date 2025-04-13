class Employee:
    employee_count = 101
    def __init__(self, name, salary, designation):
        self.name = name
        self.salary = salary
        self.emp_id = 'e' + str(Employee.employee_count)
        self.designation = designation
        Employee.employee_count +=  1

    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")
        print(f"Employee ID: {self.emp_id}")
        print(f"Designation: {self.designation}")
        print(f"Employee Count: {self.employee_count}")

    @classmethod
    def total_emp(cls):
        return cls.employee_count - 101

e1 = Employee("John", 50000, "Manager")
e2 = Employee("Jane", 60000, "Developer")

e1.show_details()
e2.show_details()
print(f"Total Employees: {Employee.total_emp()}")