import os
def insecure_login():
    password = input("Enter admin password: ")
    if password == "admin123":  # Hardcoded password (bad practice)
        print("Access granted!")
    else:
        print("Access denied!")

if __name__ == "__main__":
    insecure_login()