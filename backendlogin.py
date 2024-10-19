import bcrypt

username = input("Enter your username: ")
password = input("Enter your password: ")

password_bytes = password.encode('utf-8')
salt = bcrypt.gensalt()
hashed_password = bcrypt.hashpw(password_bytes, salt)

while True:
    check_password = input("Re-enter your password to verify: ")  

    if bcrypt.checkpw(check_password.encode('utf-8'), hashed_password):
        print("Password verified successfully!")
        break  
    else:
        print("Password does not match. Please try again.")


print("Username: ", username)
print("Hashed password: ", hashed_password)