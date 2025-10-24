# insecure version
def insecure_login():
    password = input("Enter admin password: ")
    if password == "admin123":  # Hardcoded password (BAD PRACTICE)
        print("Access granted!")
    else:
        print("Access denied!")

if __name__ == "__main__":
    insecure_login()