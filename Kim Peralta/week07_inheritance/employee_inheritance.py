class Employee_kwap:
    def __init__(self_kwap, name_kwap, salary_kwap):
        self_kwap.name_kwap = name_kwap
        self_kwap.salary_kwap = salary_kwap


class Manager_kwap(Employee_kwap):
    def __init__(self_kwap, name_kwap, salary_kwap, department_kwap):
        super().__init__(name_kwap, salary_kwap)
        self_kwap.department_kwap = department_kwap

    def display_manager_kwap(self_kwap):
        print("Name:", self_kwap.name_kwap)
        print("Salary:", self_kwap.salary_kwap)
        print("Department:", self_kwap.department_kwap)


manager1_kwap = Manager_kwap("John", 50000, "IT")
manager1_kwap.display_manager_kwap()
