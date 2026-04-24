class Employee_kwap:
    def __init__(self_kwap, name_kwap):
        self_kwap.__name = name_kwap
        self_kwap.__salary = 0

    def set_salary_kwap(self_kwap, salary_kwap):
        if salary_kwap > 0:
            self_kwap.__salary = salary_kwap

    def get_salary_kwap(self_kwap):
        return self_kwap.__salary


emp_kwap = Employee_kwap("Ana")
emp_kwap.set_salary_kwap(30000)
print("Salary:", emp_kwap.get_salary_kwap())
