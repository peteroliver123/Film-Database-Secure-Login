from securelogin.password_security import password_encrypter, read_two_fa
from securelogin.user import user_password_creation
from util import secure_input, NUMBER_PASSWORD_WRONG, write_action
from securelogin.two_fa import two_fa_option, unlock_two_fa


def delete_accounts(session, name_to_delete):
    session.get_cursor().callproc('ReadUsers', [name_to_delete])
    result = session.get_cursor().fetchone()
    session.get_cursor().callproc('ReadPasswords', [name_to_delete])
    result2 = session.get_cursor().fetchone()
    if result and result2:
        if result[0] == "ADMIN":
            print("Cannot delete ADMIN")
            write_action(f"User {session.get_user().get_user_name()} attempted to delete ADMIN")
        else :
            session.get_cursor().callproc('DropRowPassword', [name_to_delete])
            session.commit()
            session.get_cursor().callproc('DropRowUser', [name_to_delete])
            session.commit()
            print(f"Deleted {name_to_delete} successfully!")
            write_action(f"User {session.get_user().get_user_name()} deleted {name_to_delete} successfully")
    else :
        print("Name not found")
        write_action(f"User {session.get_user().get_user_name()} tried to delete an account that didn't exist")


def account_into(session):
    write_action(f"User {session.get_user().get_user_name()} read account info")
    session.get_cursor().callproc('ReadUsers', [session.get_user().get_user_name()])
    results = session.get_cursor().fetchone()
    print(f"Username: {results[0]}, Date Created: {results[1]}, "
          f"Locked Out? {results[2]}, Number of Previous Lockouts: {results[4]},"
          f"\nAdmin? {results[5]}, Password Attempts Remaining before Lockout: {NUMBER_PASSWORD_WRONG - results[6]}")


def rename(session):
    if session.get_user().get_is_admin():
        print("Cannot rename ADMIN!")
        write_action(f"User {session.get_user().get_user_name()} attempted to rename ADMIN")
    else :
        change_flag = False
        while True:
            if change_flag:
                break
            new_name = secure_input("Enter the username you would like to rename the active account to (CANCEL to go back):\n")
            if new_name.upper() == "CANCEL":
                break
            while True:
                confirmation = secure_input(f"Rename {session.get_user().get_user_name()} to {new_name}. Proceed (Y/N): ").upper()
                if confirmation == "Y" or confirmation == "YES":
                    session.get_cursor().callproc('RenameUser', [session.get_user().get_user_name(), new_name])
                    session.commit()
                    session.get_user().set_user_name(new_name)
                    change_flag = True
                    write_action(f"User {session.get_user().get_user_name()} renamed to {new_name}")
                    break
                elif confirmation == "N" or confirmation == "NO":
                    break


def reset_password(session):
    print("Setup a New Password: ")
    new_password = user_password_creation(session)
    session.get_cursor().callproc('ResetPassword', [session.get_user().get_user_name(), password_encrypter(new_password)])
    session.commit()
    write_action(f"User {session.get_user().get_user_name()} successfully reset their password")


def profile_fun(session):
    print("Welcome to Profile!")
    while True:
        command = secure_input("Enter a command. Type HELP for more info: \n").upper().split()[0]
        match command:
            case "HELP":
                print("List of Commands:")
                print("2FA = Turn On 2FA")
                print("DELETE = Delete Users (ADMIN only)")
                print("RENAME = Re-name this Account")
                print("RESET = Reset Password")
                print("INFO = Account Info")
                print("MAIN = Return to Main Menu")
            case "2FA":
                if read_two_fa(session):
                    print("TwoFa already on!")
                else :
                    secret = two_fa_option()
                    if secret:
                        session.get_cursor().callproc('UpdateTwoFa', [session.get_user().get_user_name(), secret])
                        session.commit()
                break
            case "DELETE":
                if session.get_user().get_is_admin() :
                    name_to_delete = secure_input("Enter the username of the account you want to delete\n")
                    if name_to_delete == "ADMIN" :
                        print("Cannot delete admin!")
                    else :
                        delete_accounts(session, name_to_delete)
                else :
                    print("Delete requires ADMIN privileges")
                break
            case "RENAME":
                rename(session)
                break
            case "RESET":
                # could make this require 2fa
                if not unlock_two_fa(session) == -1:
                    reset_password(session)
                else :
                    print("Reset requires 2FA")
                break
            case "INFO":
                account_into(session)
                break
            case "MAIN":
                return
            case _:
                print("Command not recognised!")