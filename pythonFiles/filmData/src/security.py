# Built-In Imports
import pymysql
from datetime import datetime, timedelta

# My File Imports
from util import secure_input, secure_quit, NUMBER_PASSWORD_WRONG, PROJECT_NAME
from user_classes import NewUserProfile, ExistingUserProfile

"""
CurrentSession class manages the current state. Which User is logged in
and whether they are ADMIN (and hence have access to certain privileges)
Encapsulated code inside this class and this file for functions for
extra security.
"""

class CurrentSession:
    def __init__(self):
        self.user_profile = None
        self.conn = None
        self.cursor = None

    def get_user(self):
        return self.user_profile

    def get_cursor(self):
        return self.cursor

    def set_user(self, user_profile):
        self.user_profile = user_profile

    def open_conn(self):
        self.conn = pymysql.connect(host="localhost", user="root", password="Founders72!", database="record_boxes")
        self.cursor = self.conn.cursor()

    def close_conn(self):
        self.conn.close()

    def commit(self):
        self.conn.commit()

    def print_results(self):
        results = (self.cursor.fetchall())
        for row in results:
            print(row)
        if not results :
            print("No matching films found!")

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
def create_new_user(session):
        new_password = secure_input("Enter a password: ")

        while password_checker(new_password):
            new_password = secure_input("Enter a password: ")
        if new_password.upper() == "CANCEL" :
            login()

        confirm_password = secure_input("Confirm password: ")

        if confirm_password.upper() == "CANCEL" :
            login()

        if new_password == confirm_password :
            write_new_password(session, new_password)
            write_new_user(session)
            print("New Account Created!")
            return session.get_user()
        else :
            return -1


def lock_account(session):
    session.get_user().flip_locked()
    session.get_user().set_date_unlock(datetime.now() + timedelta(days=1))
    session.get_user().reset_num_fails()
    #rewrite file
    rewrite_user(session)

def unlock_procedures(session):
    session.get_user().flip_locked()
    session.get_user().set_date_unlock(session.get_user().get_date_created())
    #rewrite file
    rewrite_user(session)
    print("Account has been unlocked! Login to continue!")

def rewrite_user(session):
    result = session.get_cursor().callproc('dropRowUser', [session.get_user().get_user_name()])
    session.commit()
    if result :
        write_new_user(session)
    else :
        print("User not found!")

def write_new_password(session, new_password):
    session.get_cursor().callproc('insertPassword', [session.get_user().get_user_name(), new_password])
    session.commit()

def write_new_user(session):
    is_locked = session.get_user().get_is_locked()
    if is_locked :
        is_locked = "True"
    else :
        is_locked = "False"
    date_unlock = session.get_user().get_date_unlock()
    date_created = session.get_user().get_date_created()
    session.get_cursor().callproc('insertUser', [session.get_user().get_user_name(), date_created, is_locked, date_unlock, session.get_user().get_num_fails()])
    session.commit()

def create_new_user_loop(session):
    password_count = NUMBER_PASSWORD_WRONG
    outcome = create_new_user(session)
    while outcome == -1:
        password_count -= 1
        if password_count == 0:
            secure_quit(None, "Passwords didn't match too many times!")
        print(f"Passwords didn't match! {password_count} attempts remaining!")
        outcome = create_new_user(session)

    return outcome


#This function reads the password file, and returns -1 if username not found
def read_passwords(session, user_name):
    session.get_cursor().callproc('readPasswords', [user_name])
    results = session.get_cursor().fetchone()
    if not results:
        return -1
    else :
        return results[0]

#This function reads the users file, and returns -1 if user not found
def read_users(session, user_name):
    session.get_cursor().callproc('readUsers', [user_name])
    results = session.get_cursor().fetchone()
    if not results:
        return -1
    else :
        name, date_created, is_locked, date_unlock, num_fails, is_admin = results
        is_locked = is_locked == "True"
        num_fails = int(num_fails)
        is_admin = is_admin == "True"
        return ExistingUserProfile(name, date_created, is_locked, date_unlock, num_fails, is_admin)

# These functions manage user login, if username doesn't exist, creates new one,
# if it does asks for password (performs appropriate security checks) then
# creates a session and passes this session with needed info securely encapsulated
# to the launch function.

def login_to_new(session):
    while True:
        command = secure_input(f"Username {session.get_user().get_user_name()} does not exist.\nType CREATE to make this a username, type CANCEL to try another name\n").upper().split()[0]
        if command == "CREATE":
            user = create_new_user_loop(session)
            session.set_user(user)
            return session
        elif command == "CANCEL":
            login()
            break
        else :
            print("Invalid Command!")

def login_to_old(session, stored_password):
    if session.get_user().get_is_locked() :
        if session.get_user().unlock_valid() == -1:
            secure_quit(None, "You are locked out!")
        else :
            unlock_procedures(session)
            return login()
    else :
        while True:
            password = secure_input("Enter Password: ")
            if password.upper() == "CANCEL" :
                return login()
            elif password == stored_password:
                print("Password Correct!")
                return session
            else :
                session.get_user().increment_num_fails()
                rewrite_user(session)
                if session.get_user().get_num_fails() < NUMBER_PASSWORD_WRONG:
                    print(f"Password Incorrect! {NUMBER_PASSWORD_WRONG - session.get_user().get_num_fails()} attempts remaining! Type CANCEL to try another name or enter correct password")
                else :
                    lock_account(session)
                    secure_quit(session, f"Password wrong too many times! Your account has been locked until {session.get_user().get_date_unlock()}")

def login():
    while True:
        print(f"\nHello! Welcome to {PROJECT_NAME}! Login to continue\n")
        name = secure_input("Enter Username: ")
        session = CurrentSession()
        session.open_conn()
        if len(name.split()[0]) > 20:
            print("Username too long!")
        else :
            stored_password = read_passwords(session, name)
            if stored_password == -1:
                new_user = NewUserProfile(name, datetime.now())
                session.set_user(new_user)
                return login_to_new(session)
            else :
                user = read_users(session, name)
                if user == -1:
                    secure_quit(session, "User Data Incomplete!")
                else :
                    session.set_user(user)
                    return login_to_old(session, stored_password)


# Note could use prompt to have passwords protected with ****
# Only works in terminal ():

# Password hashing

# Exponential backoff: Lockout duration increases after repeated offenses.
# Optionally, track by IP address or device too.