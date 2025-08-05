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

def delete_accounts(session, name_to_delete):
    if not session :
        print("Session Empty")
        return -1
    found_name = False
    file = open("files/passwords.txt", "r")
    lines = file.readlines()
    new_lines = []
    for line in lines :
        *name, _ = line.strip().split()
        name = " ".join(name)
        if not name == name_to_delete :
           new_lines.append(line)
        else :
            found_name = True
    if not found_name :
        print("Name not found!")
        return -1
    file.close()
    file = open("files/passwords.txt", "w")
    file.writelines(new_lines)
    file.close()
    return 1


def password_checker(password):
    failure = False
    # check password is minimum 8 letters
    if len(password) < 8:
       print("Password must be min 8 characters")
       failure = True

    # check if password contains upperCase
    has_h = False
    has_l = False
    has_symbol = False
    has_digit = False

    for char in password :
        if 'A' <= char <= 'Z':
            has_h = True
        elif 'a' <= char <= 'z':
            has_l = True
        elif '0' <= char <= '9':
            has_digit = True
        elif char == '\n' :
            continue
        else :
            has_symbol = True
    if not has_l or not has_h :
        print("Password must contain upper and lower")
        failure = True

    # check if password contains symbol
    if not has_symbol :
        print("Password must contain a symbol")
        failure = True

    # check if password contains digit
    if not has_digit :
        print("Password must contain a digit")
        failure = True

    return failure

def secure_quit(session, code):
    if session :
        session.close_conn()
    quit(code)

#This function creates a new user and saves the password
def create_new_user(new_name):
    file = open("files/passwords.txt", "a")
    password_count = 3
    while True:
        new_password = input("Enter a password: ").strip()

        while password_checker(new_password):
            new_password = input("Enter a password: ").strip()

        if new_password.upper() == "CANCEL" :
            break
        confirm_password = input("Confirm password: ").strip()
        if confirm_password.upper() == "CANCEL" :
            break
        if new_password != confirm_password :
            password_count -= 1
            if password_count == 0:
                secure_quit(None, "Passwords didn't match too many times!")
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
    split_name = name.split()[0]
    if len(split_name) > 20 :
        print("Username too long!")
        login()
    stored_password = read_passwords(name)
    if stored_password != -1:
        s = CurrentSession(name, False)
        s.open_conn()
        password_attempts = 3
        while password_attempts != 0:
            password = input("Enter Password: ").strip()
            if password.upper() == "CANCEL" :
                login()
            elif password == stored_password:
                print("Password Correct!")
                if name == "ADMIN":
                    #manufacturer_code = "X5ry&cvgHTY6574"
                    manufacturer_code = "X"
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
                password_attempts -= 1
                print(f"Password Incorrect! {password_attempts} attempts remaining! Type CANCEL to try another name or enter correct password")
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


# Note could use prompt to have passwords protected with ****
# Only works in terminal ):

# Password hashing

# Validate:
# usernames (length, characters)
# passwords (strength, common-password checks)

#password strength library
#pip install zxcvbn
#from zxcvbn import zxcvbn
#print(zxcvbn("hunter2"))

#audit logging

# Don't store passwords in plaintext
# Don't rely on base64 or ROT13 for “security”
# Don’t roll your own crypto – use trusted libraries
# Don’t hardcode secrets or keys
# track number of failed attempts (across sessions) per user and lockout time
# Show generic message: “Login failed” (not "wrong password" or "user not found").
# Exponential backoff: Lockout duration increases after repeated offenses.
# Optionally, track by IP address or device too.