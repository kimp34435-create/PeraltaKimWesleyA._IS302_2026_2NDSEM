def register_kwap():
    username_kwap = input("Enter username: ")
    password_kwap = input("Enter password: ")
    with open("users.txt", "a") as file_kwap:
        file_kwap.write(username_kwap + "," + password_kwap + "\n")
    print("Registration successful!")

def login_kwap():
    username_kwap = input("Enter username: ")
    password_kwap = input("Enter password: ")
    try:
        with open("users.txt", "r") as file_kwap:
            for line_kwap in file_kwap:
                stored_user_kwap, stored_pass_kwap = line_kwap.strip().split(",")
                if username_kwap == stored_user_kwap and password_kwap == stored_pass_kwap:
                    print("Login successful!")
                    return
        print("Invalid credentials!")
    except FileNotFoundError:
        print("No users registered yet!")

def main_kwap():
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")
        choice_kwap = input("Enter choice: ")
        
        if choice_kwap == "1":
            register_kwap()
        elif choice_kwap == "2":
            login_kwap()
        elif choice_kwap == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

main_kwap()
