class Animal_kwap:
    def __init__(self_kwap, name_kwap):
        self_kwap.name_kwap = name_kwap

    def speak_kwap(self_kwap):
        print(self_kwap.name_kwap, "makes a sound")


class Dog_kwap(Animal_kwap):
    def bark_kwap(self_kwap):
        print(self_kwap.name_kwap, "barks")


dog1_kwap = Dog_kwap("Buddy")
dog1_kwap.speak_kwap()
dog1_kwap.bark_kwap()
