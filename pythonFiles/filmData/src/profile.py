from util import secure_input
from file import rewrite_file_without_line

def delete_accounts(name_to_delete):
    result = rewrite_file_without_line("files/passwords.txt", name_to_delete)
    result2 = rewrite_file_without_line("files/users.txt", name_to_delete)
    if result == -1 or result2 == -1:
        print("Name not found")
    else :
        print(f"Deleted {name_to_delete} successfully!")

def profile_fun(session):
    print("Welcome to Profile!")
    while True:
        command = secure_input("Enter a command. Type HELP for more info: \n").upper().split()[0]
        match command:
            case "HELP":
                print("List of Commands:")
                print("2FA = 2FA Settings")
                print("DELETE = Delete Users")
                print("RENAME = Re-name Users")
                print("PASSWORD_RESET = Reset Password")
                print("ACCOUNT_INFO = Account Info")
                print("MAIN = Return to Main Menu")
            case "2FA":
                pass
                break
            case "DELETE":
                if session.get_user().get_is_admin() :
                    name_to_delete = secure_input("Enter the username of the account you want to delete\n")
                    if name_to_delete == "ADMIN" :
                        print("Cannot delete admin!")
                    else :
                        delete_accounts(name_to_delete)
                else :
                    print("Delete requires ADMIN privileges")
                break
            case "RENAME":
                pass
                break
            case "PASSWORD_RESET":
                pass
                break
            case "ACCOUNT_INFO":
                pass
                break
            case "MAIN":
                return
            case _:
                print("Command not recognised!")