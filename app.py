import getpass

def secure_login():
    password = getpass.getpass("Enter admin password: ")
    stored_password = "UseENVorHash123"  # Example: use env variable or hashed password
    if password == stored_password:
        print("Access granted!")
    else:
        print("Access denied!")

if __name__ == "__main__":
    secure_login()
