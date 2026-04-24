class Employee_kwap:
    def work_kwap(self_kwap):
        print("Employee performs tasks")


class Programmer_kwap(Employee_kwap):
    def work_kwap(self_kwap):
        print("Programmer writes code")


class Designer_kwap(Employee_kwap):
    def work_kwap(self_kwap):
        print("Designer creates UI designs")


employees_kwap = [Programmer_kwap(), Designer_kwap()]
for emp_kwap in employees_kwap:
    emp_kwap.work_kwap()
