from util import secure_input

def duplicate_search(session):
    locations = secure_input("Enter any amount of locations (max 3)")
    if len(locations) == 3:
        session.get_cursor().callproc('passThreeTableNames', locations[0], locations[1], locations[3])
    elif len(locations) == 2:
        session.get_cursor().callproc('passTwoTableNames', locations[0], locations[1])
    elif len(locations) == 1:
        print("Too few locations!")
        duplicate_search(session)
    else :
        print("Too many locations!")
        duplicate_search(session)

def edit_fun(session):
    print("Welcome to Edit!")
    while True:
        command = secure_input("Enter a command. Type HELP for more info: \n").upper().split()[0]
        match command:
            case "HELP":
                print("List of Commands:")
                print("RENAME = Re-name Films")
                print("DUPLICATE = Find repeated films")
                print("DELETE = Delete films")
                print("INSERT = Add films")
                print("MAIN = Return to Main Menu")
            case "RENAME":
                pass
                break
            case "DUPLICATE":
                duplicate_search(session)
                break
            case "DELETE":
                pass
                break
            case "INSERT":
                pass
                break
            case "MAIN":
                return
            case _:
                print("Command not recognised!")