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
                session.get_cursor().callproc('PassTwoTableNames', (locations[0], locations[1]))
                session.print_results()
                break
            elif len(locations) == 3:
                session.get_cursor().callproc('PassThreeTableNames', (locations[0], locations[1], locations[2]))
                session.print_results()
                break
            else :
                print("Too many locations!")


def location_selector(session):
    location = secure_input("Please enter the location, you would like to perform this operation (CANCEL to go back):\n")
    session.get_cursor().callproc('BasicLocationSearch', [location,"",""])
    if len(location) > 20:
        return -1
    result = session.get_cursor().fetchone()
    if result:
        return location
    elif location.upper() == "CANCEL":
        return -1
    else :
        print("Invalid Location!")
        return location_selector(session)


def id_name_selector():
    print("You can perform this operation by either id or name")
    id_val = 0
    name = ""
    while True:
        command = secure_input("Type 1 for id and type 2 for name. CANCEL to go back: \n")
        if command == "1":
            id_val = secure_input("Enter an id: ")
            if len(id_val) > 20:
                return -1 -1
            return id_val, name
        elif command == "2":
            name = secure_input("Enter film name: ")
            if len(name) > 80:
                return -1 -1
            return id_val, name
        elif command == "CANCEL":
            return -1 -1


def rename_fun(session):
    print("Welcome to Rename!")
    location = location_selector(session)
    id_val, name = id_name_selector()
    if id_val == -1 or name == -1 or location == -1:
        return
    else :
        new_name = secure_input("Enter new name for the film: ")

        session.get_cursor().callproc('RenameFilm', [name, id_val, location, new_name])
        results = session.get_cursor().fetchone()
        rows_affected = results[0]

        if rows_affected == 0:
            print("Name or id invalid!")
        else :
            print("Name Changed Successfully!")
        session.commit()


def insert_fun(session):
    print("Welcome to Insert!")
    #Location
    location = location_selector(session)

    if location == -1:
        return

    #Id
    session.get_cursor().callproc('CountIds', [location])
    results = session.get_cursor().fetchone()
    id_val = results[0] + 1

    #Name
    film_name = secure_input("Enter name for the new film: ")

    #Age Rating
    age_rating = secure_input("Enter age rating for the new film: ")

    session.get_cursor().callproc('InsertFilm', [id_val, film_name, location, age_rating])
    session.commit()
    print("Inserted Film Successfully!")


def delete_fun(session):
    print("Welcome to Delete!")
    #Location
    location = location_selector(session)

    #Id, Name
    id_val, name = id_name_selector()

    if id_val == -1 or name == -1 or location == -1:
        return
    else :
        session.get_cursor().callproc('DeleteFilm', [name, id_val, location])
        results = session.get_cursor().fetchone()
        rows_affected = results[0]

        if rows_affected == 0:
            print("Name or id invalid!")
        else :
            print("Deleted Film Successfully!")
        session.commit()


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
                rename_fun(session)
                break
            case "DUPLICATE":
                duplicate_search(session)
                break
            case "DELETE":
                delete_fun(session)
                break
            case "INSERT":
                insert_fun(session)
                break
            case "MAIN":
                return
            case _:
                print("Command not recognised!")