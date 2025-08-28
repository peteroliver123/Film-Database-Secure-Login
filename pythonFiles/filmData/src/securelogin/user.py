from datetime import datetime, timedelta

from util import secure_input, secure_quit, NUMBER_PASSWORD_WRONG
from securelogin.two_fa import two_fa_option
from securelogin.password_security import password_checker, write_new_password, read_passwords_data
from securelogin.user_classes import ExistingUserProfile
from util import write_action


#This function reads the users file, and returns -1 if user not found
def read_users(session, user_name):
    session.get_cursor().callproc('ReadUsers', [user_name])
    results = session.get_cursor().fetchone()
    if not results:
        return -1
    else :
        name, date_created, is_locked, date_unlock, num_lockout, is_admin, failed_entry = results
        is_locked = int(is_locked)
        num_lockout = int(num_lockout)
        is_admin = int(is_admin)
        write_action(f"User {session.get_user().get_user_name()} read from file successfully")
        return ExistingUserProfile(name, date_created, is_locked,
                                   date_unlock, num_lockout, is_admin, failed_entry)


#This function creates a new user
def user_password_creation(session):
    password_count = NUMBER_PASSWORD_WRONG
    while True:
        new_password = secure_input("Enter a password: ")
        while password_checker(new_password):
            new_password = secure_input("Enter a password: ")
        if new_password.upper() == "CANCEL" :
            return -1

        confirm_password = secure_input("Confirm password: ")
        if confirm_password.upper() == "CANCEL" :
            return -1

        if new_password == confirm_password :
            if read_passwords_data(session):
                return new_password
            else :
                return user_creation(session, new_password)
        else :
            password_count -= 1
            if password_count == 0:
                secure_quit(None, "Passwords didn't match too many times!")
            print(f"Passwords didn't match! {password_count} attempts remaining!")
            write_action(f"User {session.get_user().get_user_name()} failed to match passwords when creating account")


def user_creation(session, new_password):
    secret = two_fa_option()
    write_new_password(session, new_password, secret)
    write_new_user(session)
    print("New Account Created!")
    write_action(f"User {session.get_user().get_user_name()} created as new account")
    return session.get_user()


def rewrite_user(session):
    result = session.get_cursor().callproc('DropRowUser', [session.get_user().get_user_name()])
    session.commit()
    if result :
        write_new_user(session)
    else :
        print("User not found!")


def write_new_user(session):
    username = session.get_user().get_user_name()
    is_locked = session.get_user().get_is_locked()
    date_unlock = session.get_user().get_date_unlock()
    num_lockouts = session.get_user().get_num_lockout()
    date_created = session.get_user().get_date_created()
    is_admin = session.get_user().get_is_admin()
    failed_entry = session.get_user().get_failed_entry()
    session.get_cursor().callproc('InsertUser', [username,
                                                 date_created, is_locked,
                                                 date_unlock, num_lockouts,
                                                 is_admin, failed_entry])
    session.commit()
    write_action(f"User file changed")

# LOCKING PROCEDURES #
def lock_account(session):
    session.get_user().flip_locked()

    # Exponential Lockout Logic #
    if session.get_user().get_num_lockout() >= 10:
        session.get_user().set_date_unlock(datetime.now() + timedelta(days = 32))
    elif session.get_user().get_num_lockout() >= 5:
        incremental = pow(2, session.get_user().get_num_lockout() - 5)
        session.get_user().set_date_unlock(datetime.now() + timedelta(days = incremental))
    else :
        incremental = pow(2, session.get_user().get_num_lockout())
        session.get_user().set_date_unlock(datetime.now() + timedelta(hours = incremental))

    if session.get_user().get_num_lockout() < 1000:
        session.get_user().increment_num_lockout()
    session.get_user().reset_failed_entry()
    #rewrite file
    rewrite_user(session)


def unlock_procedures(session):
    session.get_user().flip_locked()
    session.get_user().set_date_unlock(session.get_user().get_date_created())
    #rewrite file
    rewrite_user(session)
    print("Account has been unlocked! Login to continue!")