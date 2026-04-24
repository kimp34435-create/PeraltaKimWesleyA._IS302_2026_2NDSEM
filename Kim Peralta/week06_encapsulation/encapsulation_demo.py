class Person_kwap:
    def __init__(self_kwap, name_kwap, age_kwap):
        self_kwap.__name = name_kwap
        self_kwap.__age = age_kwap

    def get_name_kwap(self_kwap):
        return self_kwap.__name

    def get_age_kwap(self_kwap):
        return self_kwap.__age


p1_kwap = Person_kwap("Maria", 20)
print("Name:", p1_kwap.get_name_kwap())
print("Age:", p1_kwap.get_age_kwap())
