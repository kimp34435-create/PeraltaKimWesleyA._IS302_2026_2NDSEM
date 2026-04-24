class Product_kwap:
    def __init__(self_kwap, name_kwap, price_kwap, quantity_kwap):
        self_kwap.__name = name_kwap
        self_kwap.__price = price_kwap
        self_kwap.__quantity = quantity_kwap

    def get_product_info_kwap(self_kwap):
        print("Product:", self_kwap.__name)
        print("Price:", self_kwap.__price)
        print("Quantity:", self_kwap.__quantity)

    def update_quantity_kwap(self_kwap, new_quantity_kwap):
        if new_quantity_kwap >= 0:
            self_kwap.__quantity = new_quantity_kwap

    def update_price_kwap(self_kwap, new_price_kwap):
        if new_price_kwap > 0:
            self_kwap.__price = new_price_kwap


# Example usage
product_kwap = Product_kwap("Laptop", 45000, 10)
product_kwap.get_product_info_kwap()
