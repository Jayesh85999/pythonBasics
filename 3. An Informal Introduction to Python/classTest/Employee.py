class Employee:
    
    id: 0
    name: 'default'
    salary: 0000
    
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary
        
    
    def isMySalaryHigh(self):
        if self.salary < 3000:
            print('No!!')
        else:
            print('Yes!!')



class EmployeeII:

    id: 0
    name: 'default'
    salary: 0000

    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary


    def isMySalaryHigh(self):
        if self.salary < 1500:
            print('No!!')
        else:
            print('Yes!!')

  