
import main
import pymysql
"""
CurrentSession class manages the current state. Which User is logged in
and whether they are ADMIN (and hence have access to certain privileges)
Encapsulated code inside this class and this file for functions for
extra security.
"""
class CurrentSession:
    def __init__(self, name, is_admin):
        self.user_name = name
        self.is_admin = is_admin
        self.conn = None
        self.cursor = ""

    def get_user_name(self):
        return self.user_name

    def get_is_admin(self):
        return self.is_admin

    def set_is_admin(self, boolean):
        self.is_admin = boolean

    def open_conn(self):
        self.conn = pymysql.connect(host="localhost", user="root", password="Founders72!", database="record_boxes")
        self.cursor = self.conn.cursor()

    def close_conn(self):
        self.conn.close()

    def get_cursor(self):
        return self.cursor


def secure_quit(session, code):
    session.close_conn()
    quit(code)

#This function creates a new user and saves the password
def create_new_user(new_name):
    file = open("files/passwords.txt", "a")
    password_count = 3
    while True:
        new_password = input("Enter a password: ").strip()
        if new_password.upper() == "CANCEL" :
            break
        confirm_password = input("Confirm password: ").strip()
        if confirm_password.upper() == "CANCEL" :
            break
        if new_password != confirm_password :
            password_count -= 1
            if password_count == 0:
                quit("Passwords didn't match too many times!")
            print(f"Passwords didn't match! {password_count} attempts remaining!")
        else :
            file.write(new_name + " " + new_password + "\n")
            print("New Account Created! Login to continue!")
            break
    file.close()
    login()

#This function reads the password file, and returns -1 if username not found
def read_passwords(user_name):
    file = open("files/passwords.txt", "r")
    for row in file:
        *name, password = row.strip().split()
        name = " ".join(name)
        if name == user_name:
            file.close()
            return password
    file.close()
    return -1

# This function manages user login, if username doesn't exist, creates new one,
# if it does asks for password (performs appropriate security checks) then
# creates a session and passes this session with needed info securely encapsulated
# to the launch function.
def login():
    main.print_welcome_message()
    name = input("Enter Username: ").strip()
    stored_password = read_passwords(name)
    if stored_password != -1:
        s = CurrentSession(name, False)
        s.open_conn()
        i = 3
        while i != 0:
            password = input("Enter Password: ").strip()
            if password.upper() == "CANCEL" :
                login()
            elif password == stored_password:
                print("Password Correct!")
                if name == "ADMIN":
                    manufacturer_code = "X5ry&cvgHTY6574"
                    code = input("Enter manufacturer code to gain access (Warning 1 attempt) (Warning admin can cause damage to server):\n").strip()
                    if code == manufacturer_code:
                        s.set_is_admin(True)
                        main.launch(s)
                    elif code.upper() == "CANCEL" :
                        login()
                    else :
                        secure_quit(s, "Incorrect! Logging you out!")
                else :
                    main.launch(s)
                    break
            else :
                i -= 1
                print(f"Password Incorrect! {i} attempts remaining! Type CANCEL to try another name or enter correct password")
        secure_quit(s, "Password wrong too many times!")
    else :
        while True:
            command = input(f"Username {name} does not exist.\nType CREATE to make this a username, type CANCEL to try another name\n").upper().split()[0]
            if command == "CREATE":
                create_new_user(name)
                break
            elif command == "CANCEL":
                login()
            else :
                print("Invalid Command!")