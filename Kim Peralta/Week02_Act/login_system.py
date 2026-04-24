correct_username_kwap = "admin"
correct_password_kwap = "1234"
attempts_kwap = 0

while attempts_kwap < 3:
    username_kwap = input("Enter username: ")
    password_kwap = input("Enter password: ")
    
    if username_kwap == correct_username_kwap and password_kwap == correct_password_kwap:
        print("Login Successful")
        break
    else:
        print("Invalid Credentials")
        attempts_kwap += 1

if attempts_kwap == 3:
    print("Account Locked")
