import getpass
import os

def secure_login():
    password = getpass.getpass("Enter admin password: ")
    stored_password = os.environ.get("ADMIN_PASSWORD")  # Get password from environment
    if password == stored_password:
        print("Access granted!")
    else:
        print("Access denied!")

if __name__ == "__main__":
    secure_login()
