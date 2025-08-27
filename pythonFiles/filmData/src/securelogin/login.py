# Standard Library Imports
from datetime import datetime

from profile import reset_password
# Local Imports
from securelogin.password_security import do_passwords_match, read_passwords_data
from securelogin.session import CurrentSession
from securelogin.two_fa import unlock_two_fa
from securelogin.user import rewrite_user, user_password_creation, read_users, lock_account, unlock_procedures
from securelogin.user_classes import NewUserProfile
from util import secure_input, secure_quit, NUMBER_PASSWORD_WRONG, PROJECT_NAME

"""
These functions manage user login, they are the primary logic controllers of the
secure login system. The logic is broken down into three sections login_to_new(),
login_to_old() and login(). The login() function launches the secure login system
and it requires that the launch function be present as the first function of whatever
program you seek to protect.
"""


def login_to_new(session):
    while True:
        command = secure_input(f"Username {session.get_user().get_user_name()} does not "
                               f"exist.\nType CREATE to make this a username, type CANCEL to try "
                               f"another name\n").upper().split()[0]
        if command == "CREATE":
            user = user_password_creation(session)
            if not user == -1:
                session.set_user(user)
                return session
            else :
                return login()
        elif command == "CANCEL":
            return login()
        else :
            print("Invalid Command!")


def login_to_old(session):
    if session.get_user().get_is_locked() :
        if session.get_user().unlock_valid() == -1:
            result = unlock_two_fa(session)
            if not result == -1:
                unlock_procedures(session)
                reset_password(session)
                return login()
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
                session.get_user().increment_failed_entry()
                rewrite_user(session)
                if session.get_user().get_failed_entry() < NUMBER_PASSWORD_WRONG:
                    print(f"Password Incorrect! {NUMBER_PASSWORD_WRONG - session.get_user().get_failed_entry()} "
                          f"attempts remaining! Type CANCEL to try another name or enter correct password")
                else :
                    lock_account(session)
                    secure_quit(session, f"Password wrong too many times! Your "
                                         f"account has been locked until {session.get_user().get_date_unlock()}")


def login():
    while True:
        print(f"\nHello! Welcome to {PROJECT_NAME}! Login to continue\n")
        name = secure_input("Enter Username: ")
        if len(name) > 60:
            secure_quit(None, "User attempted to break the system!")
        session = CurrentSession()
        session.open_conn()
        new_user = NewUserProfile(name, datetime.now())
        session.set_user(new_user)
        if len(name.split()[0]) > 20:
            print("Username too long!")
        else :
            if not read_passwords_data(session):
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