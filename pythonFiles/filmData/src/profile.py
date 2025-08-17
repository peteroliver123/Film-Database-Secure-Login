from util import secure_input

def switch_two_fa(is_on):
    print("The 2FA functionality has not been implemented yet! Please come back later")

def two_fa_settings(session):
    print("Welcome to 2FA!")
    session.get_cursor().callproc('twoFaSettings')
    is_on = session.get_cursor().fetchone()[0]
    if is_on :
        print("2FA is currently on!")
    else :
        print("2FA is currently off!")

    while True:
        command = secure_input("Enter SWITCH to change this setting or CANCEL to go back").strip().upper().split()[0]
        match command:
            case "SWITCH":
                switch_two_fa(is_on)
            case "CANCEL":
                profile_fun(session)
            case _:
                print("Command not recognised!")

def delete_accounts(session, name_to_delete):
    result = session.get_cursor().callproc('basicNameSearch', [name_to_delete])
    session.commit()
    if result :
        session.get_cursor().callproc('dropRowPassword', [name_to_delete])
        session.commit()
        session.get_cursor().callproc('dropRowUser', [name_to_delete])
        session.commit()
        print(f"Deleted {name_to_delete} successfully!")
    else :
        print("Name not found")

def profile_fun(session):
    print("Welcome to Profile!")
    while True:
        command = secure_input("Enter a command. Type HELP for more info: \n").upper().split()[0]
        match command:
            case "HELP":
                print("List of Commands:")
                print("2FA = 2FA Settings")
                print("DELETE = Delete Users (ADMIN only)")
                print("RENAME = Re-name Users (ADMIN only)")
                print("PASSWORD_RESET = Reset Password")
                print("ACCOUNT_INFO = Account Info")
                print("MAIN = Return to Main Menu")
            case "2FA":
                two_fa_settings(session)
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
                if session.get_user().get_is_admin() :
                    print("The RENAME functionality has not been implemented yet! Please come back later")
                else :
                    print("Re-name requires ADMIN privileges")
                break
            case "PASSWORD_RESET":
                # could make this require 2fa
                print("The RESET functionality has not been implemented yet! Please come back later")
                break
            case "ACCOUNT_INFO":
                print("The Account Info functionality has not been implemented yet! Please come back later")
                break
            case "MAIN":
                return
            case _:
                print("Command not recognised!")