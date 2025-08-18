from datetime import datetime, timedelta

from util import secure_input, secure_quit, NUMBER_PASSWORD_WRONG
from securelogin.two_fa import two_fa_option
from securelogin.password_security import password_checker, write_new_password
from securelogin.user_classes import ExistingUserProfile


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
        return ExistingUserProfile(name, date_created, is_locked,
                                   date_unlock, num_fails, is_admin)


#This function creates a new user
def user_creation(session):
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
            secret = two_fa_option()
            write_new_password(session, new_password, secret)
            write_new_user(session)
            print("New Account Created!")
            return session.get_user()
        else :
            password_count -= 1
            if password_count == 0:
                secure_quit(None, "Passwords didn't match too many times!")
            print(f"Passwords didn't match! {password_count} attempts remaining!")


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
    session.get_cursor().callproc('insertUser', [session.get_user().get_user_name(),
                                                 date_created, is_locked, date_unlock,
                                                 session.get_user().get_num_fails()])
    session.commit()


# LOCKING PROCEDURES #
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