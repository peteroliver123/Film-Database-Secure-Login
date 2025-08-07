from util import secure_input

def search_fun(session):
    print("Welcome to Search!")
    print("Separate multiple entries with spaces")
    film_name = secure_input("Enter film name (to search by name or press enter to leave blank)\n")
    age_rating = secure_input("Enter any amount of age ratings (to search by age or press enter to leave blank)\n")
    id_number = secure_input("Enter an id (to search by id or press enter to leave blank)\n")
    location = secure_input("Enter any amount of locations (to search by location or press enter to leave blank)\n")

    print(f"You entered:\n{film_name}\n{age_rating}\n{id_number}\n{location}")
    while True :
        command = secure_input("If you are happy with these type GO, type REENTER to re-enter and type MAIN to return to main menu").split()[0].upper()
        match command:
            case "GO":
                #launch_search()
                break
            case "REENTER":
                search_fun(session)
                break
            case "MAIN":
                return
            case _:
                print("Command not recognised!")