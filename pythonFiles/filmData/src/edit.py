from util import secure_input

def duplicate_search(session):
    while True:
        locations = secure_input("Enter any amount of locations (max 3 separated by spaces):\n").split()

        # Validity Check #
        valid_locations = ["KITCHEN", "LOUNGE", "ATTIC"]
        location_error = False
        for location in locations:
            location = location.upper()
            if location not in valid_locations:
                location = location.lower()
                print(f"{location} is not a valid location")
                location_error = True

        if location_error:
            continue
        else :
            if len(locations) == 1:
                print("Too few locations!")
            elif len(locations) == 2:
                session.get_cursor().callproc('passTwoTableNames', (locations[0], locations[1]))
                session.print_results()
                break
            elif len(locations) == 3:
                session.get_cursor().callproc('passThreeTableNames', (locations[0], locations[1], locations[2]))
                session.print_results()
                break
            else :
                print("Too many locations!")

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
                print("The DELETE functionality has not been implemented yet! Please come back later")
                break
            case "INSERT":
                print("The INSERT functionality has not been implemented yet! Please come back later")
                break
            case "MAIN":
                return
            case _:
                print("Command not recognised!")