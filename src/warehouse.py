from time import time as tt, ctime as ct


# Make this class a singleton

def singlestone(cls):
    instance = {}
    def wrapped(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]
    return wrapped

@singlestone
class Warehouse:
    
    # instance = None
    
    # def __new__(cls):
    #     if cls.instance is None:
    #         cls.instance = super().__new__(cls)
    #     return cls.instance
    
    def __init__(self):
        self.num_employees = 0
        self.creation_time = ct(tt())
        self.employee_list = []

    def add_employee(self):
        self.num_employees += 1

    def __str__(self):
        return f"Warehouse created on {self.creation_time}. Employees: {self.num_employees}"
