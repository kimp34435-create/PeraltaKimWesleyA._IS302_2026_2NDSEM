class Animal_kwap:
    def speak_kwap(self_kwap):
        print("Animal makes a sound")


class Dog_kwap(Animal_kwap):
    def speak_kwap(self_kwap):
        print("Dog barks")


class Cat_kwap(Animal_kwap):
    def speak_kwap(self_kwap):
        print("Cat meows")


animals_kwap = [Dog_kwap(), Cat_kwap()]
for animal_kwap in animals_kwap:
    animal_kwap.speak_kwap()
