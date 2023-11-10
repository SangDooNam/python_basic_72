from time import time as tt, ctime as ct


# Make this class a singleton
class Warehouse:
    def __init__(self):
        self.num_employees = 0
        self.creation_time = ct(tt())
        self.employee_list = []

    def add_employee(self):
        self.num_employees += 1

    def __str__(self):
        return f"Warehouse created on {self.creation_time}. Employees: {self.num_employees}"
