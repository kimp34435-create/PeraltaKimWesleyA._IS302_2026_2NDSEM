class Car_kwap:
    def __init__(self_kwap, brand_kwap, model_kwap, year_kwap):
        self_kwap.brand_kwap = brand_kwap
        self_kwap.model_kwap = model_kwap
        self_kwap.year_kwap = year_kwap
    
    def display_car_kwap(self_kwap):
        print(self_kwap.brand_kwap, self_kwap.model_kwap, self_kwap.year_kwap)

car1_kwap = Car_kwap("Toyota", "Corolla", 2020)
car1_kwap.display_car_kwap()
