import math

class Shape_kwap:
    def area_kwap(self_kwap):
        pass  # Placeholder for polymorphism


class Rectangle_kwap(Shape_kwap):
    def __init__(self_kwap, width_kwap, height_kwap):
        self_kwap.width_kwap = width_kwap
        self_kwap.height_kwap = height_kwap

    def area_kwap(self_kwap):
        return self_kwap.width_kwap * self_kwap.height_kwap


class Circle_kwap(Shape_kwap):
    def __init__(self_kwap, radius_kwap):
        self_kwap.radius_kwap = radius_kwap

    def area_kwap(self_kwap):
        return math.pi * self_kwap.radius_kwap ** 2


class Triangle_kwap(Shape_kwap):
    def __init__(self_kwap, base_kwap, height_kwap):
        self_kwap.base_kwap = base_kwap
        self_kwap.height_kwap = height_kwap

    def area_kwap(self_kwap):
        return 0.5 * self_kwap.base_kwap * self_kwap.height_kwap


# Example usage
rectangle_kwap = Rectangle_kwap(10, 5)
circle_kwap = Circle_kwap(5)
triangle_kwap = Triangle_kwap(8, 6)

print(f"Rectangle Area: {rectangle_kwap.area_kwap()}")
print(f"Circle Area: {circle_kwap.area_kwap():.1f}")
print(f"Triangle Area: {triangle_kwap.area_kwap()}")
