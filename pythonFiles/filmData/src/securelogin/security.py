# Built-In Imports
from datetime import datetime, timedelta

# My File Imports
from securelogin.read_data import read_users
from securelogin.session import CurrentSession
from util import secure_input, secure_quit, NUMBER_PASSWORD_WRONG, PROJECT_NAME
from securelogin.user_classes import NewUserProfile
from securelogin.two_fa import two_fa_option, unlock_two_fa
from securelogin.password_security import is_account, password_checker, is_two_fa, write_new_password, do_passwords_match


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
        secret = two_fa_option()
        write_new_password(session, new_password, secret)
        write_new_user(session)
        print("New Account Created!")
        return session.get_user()
    else :
        return -1

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


def login_to_old(session):
    if session.get_user().get_is_locked() :
        if session.get_user().unlock_valid() == -1:
            if is_two_fa(session):
                if unlock_two_fa(session) == 1:
                    unlock_procedures(session)
                    return login()
                else :
                    secure_quit(None, "You are locked out!")
            else :
                secure_quit(None, "You are locked out!")

        else :
            unlock_procedures(session)
            return login()
    else :
        while True:
            password = secure_input("Enter Password: ")
            if password.upper() == "CANCEL" :
                return login()
            elif do_passwords_match(session, password):
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
        new_user = NewUserProfile(name, datetime.now())
        session.set_user(new_user)
        if len(name.split()[0]) > 20:
            print("Username too long!")
        else :
            if not is_account(session):
                return login_to_new(session)
            else :
                user = read_users(session, name)
                if user == -1:
                    secure_quit(session, "User Data Incomplete!")
                else :
                    session.set_user(user)
                    return login_to_old(session)


# Note could use prompt to have passwords protected with ****
# Only works in terminal ():

# Password hashing

# Exponential backoff: Lockout duration increases after repeated offenses.
# Optionally, track by IP address or device too.