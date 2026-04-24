product_kwap = input("Enter product name: ")
price_kwap = input("Enter price: ")

with open("inventory.txt", "a") as file:
    file.write(product_kwap + "," + price_kwap + "\n")

print("Product saved successfully")
