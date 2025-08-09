# Built-In Imports
import pymysql
from datetime import datetime, date

# My File Imports
from util import secure_input, secure_quit, NUMBER_PASSWORD_WRONG, PROJECT_NAME
from user_classes import NewUserProfile, ExistingUserProfile
from file import rewrite_file_without_line

"""
CurrentSession class manages the current state. Which User is logged in
and whether they are ADMIN (and hence have access to certain privileges)
Encapsulated code inside this class and this file for functions for
extra security.
"""

class CurrentSession:
    def __init__(self, user_profile):
        self.user_profile = user_profile
        self.conn = None
        self.cursor = None

    def get_user(self):
        return self.user_profile

    def open_conn(self):
        self.conn = pymysql.connect(host="localhost", user="root", password="Founders72!", database="record_boxes")
        self.cursor = self.conn.cursor()

    def close_conn(self):
        self.conn.close()

    def get_cursor(self):
        return self.cursor

    def print_results(self):
        results = (self.cursor.fetchall())
        for row in results:
            print(row)
        if not results :
            print("No matching films found!")

def delete_accounts(name_to_delete):
    result = rewrite_file_without_line("files/passwords.txt", name_to_delete)
    result2 = rewrite_file_without_line("files/users.txt", name_to_delete)
    if result == -1 or result2 == -1:
        print("Name not found")
    else :
        print(f"Deleted {name_to_delete} successfully!")

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

#This function creates a new user and saves the password
def create_new_user(new_name):
        new_password = secure_input("Enter a password: ")

        while password_checker(new_password):
            new_password = secure_input("Enter a password: ")
        if new_password.upper() == "CANCEL" :
            login()

        confirm_password = secure_input("Confirm password: ")

        if confirm_password.upper() == "CANCEL" :
            login()

        if new_password == confirm_password :
            with open("files/passwords.txt", "a") as file:
                file.write(new_name + " " + new_password + "\n")
            print("New Account Created!")
            new_user = NewUserProfile(new_name, date.today(), datetime.now().time())
            new_user.write_new_user()
            return new_user
        else :
            return -1

def create_new_user_loop(new_name):
    password_count = NUMBER_PASSWORD_WRONG
    outcome = create_new_user(new_name)
    while outcome == -1:
        password_count -= 1
        if password_count == 0:
            secure_quit(None, "Passwords didn't match too many times!")
        print(f"Passwords didn't match! {password_count} attempts remaining!")
        outcome = create_new_user(new_name)

    return outcome


#This function reads the password file, and returns -1 if username not found
def read_passwords(user_name):
    with open("files/passwords.txt", "r") as file:
        for row in file:
            *name, password = row.strip().split()
            name = " ".join(name)
            if name == user_name:
                return password
    return -1

#This function reads the users file, and returns -1 if user not found
def read_users(user_name):
    with open("files/users.txt", "r") as file:
        for row in file:
            *name, date_created, time_created, is_locked, date_unlock, time_unlock, num_fails, is_admin = row.strip().split()

            name = " ".join(name)
            if date_created == "None":
                date_created = None
            else :
                date_created = datetime.strptime(date_created, "%Y-%m-%d").date()
            if time_created == "None":
                time_created = None
            else :
                time_created = datetime.strptime(time_created, "%H:%M:%S.%f").time()
            is_locked = is_locked == "True"
            if date_unlock == "None":
                date_unlock = None
            else :
                date_unlock = datetime.strptime(date_unlock, "%Y-%m-%d").date()
            if time_unlock == "None":
                time_unlock = None
            else :
                time_unlock = datetime.strptime(time_unlock, "%H:%M:%S.%f").time()
            num_fails = int(num_fails)
            is_admin = is_admin == "True"

            existing_user = ExistingUserProfile(name, date_created, time_created, is_locked, date_unlock, time_unlock, num_fails, is_admin)
            if name == user_name:
                return existing_user
    return -1

# These functions manage user login, if username doesn't exist, creates new one,
# if it does asks for password (performs appropriate security checks) then
# creates a session and passes this session with needed info securely encapsulated
# to the launch function.

def login_to_new(name):
    while True:
        command = secure_input(f"Username {name} does not exist.\nType CREATE to make this a username, type CANCEL to try another name\n").upper().split()[0]
        if command == "CREATE":
            user = create_new_user_loop(name)
            s = CurrentSession(user)
            s.open_conn()
            return s
        elif command == "CANCEL":
            login()
            break
        else :
            print("Invalid Command!")

def login_to_locked(user):
    result_unlock = user.unlock_valid()
    if result_unlock == -1 :
        secure_quit(None, "You are locked out!")
    else :
        login()

def login_to_old(user, stored_password):
    if user.get_is_locked() :
        login_to_locked(user)
    else :
        session = CurrentSession(user)
        session.open_conn()
        while True:
            password = secure_input("Enter Password: ")
            if password.upper() == "CANCEL" :
                login()
                break
            elif password == stored_password:
                print("Password Correct!")
                return session
            else :
                session.get_user().increment_num_fails()
                if session.get_user().get_num_fails() < NUMBER_PASSWORD_WRONG:
                    print(f"Password Incorrect! {NUMBER_PASSWORD_WRONG - session.get_user().get_num_fails()} attempts remaining! Type CANCEL to try another name or enter correct password")
                else :
                    session.get_user().lock_account()
                    secure_quit(session, f"Password wrong too many times! Your account has been locked until {session.get_user().get_date_unlock()} {session.get_user().get_time_unlock()}")
                    break

def login():
    while True:
        print(f"\nHello! Welcome to {PROJECT_NAME}! Login to continue\n")
        name = secure_input("Enter Username: ")
        if len(name.split()[0]) > 20:
            print("Username too long!")
        else :
            stored_password = read_passwords(name)
            if stored_password == -1:
                return login_to_new(name)
            else :
                user = read_users(name)
                if user == -1:
                    exit("User Data Incomplete!")
                else :
                    return login_to_old(user, stored_password)


# Note could use prompt to have passwords protected with ****
# Only works in terminal ():

# Password hashing

# Exponential backoff: Lockout duration increases after repeated offenses.
# Optionally, track by IP address or device too.