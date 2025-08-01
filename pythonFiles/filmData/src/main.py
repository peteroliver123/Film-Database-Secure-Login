# Connecting to Server
import pymysql
import security

def search_fun(session):
    print("Welcome to Search!")
    print("Separate multiple entries with spaces")
    film_name = input("Enter film name (to search by name or press enter to leave blank)\n")
    age_rating = input("Enter any amount of age ratings (to search by age or press enter to leave blank)\n")
    id_number = input("Enter an id (to search by id or press enter to leave blank)\n")
    location = input("Enter any amount of locations (to search by location or press enter to leave blank)\n")

    print(f"You entered:\n{film_name}\n{age_rating}\n{id_number}\n{location}")
    while True :
        command = input("If you are happy with these type GO, type REENTER to re-enter and type MAIN to return to main menu")
        match command:
            case "GO":
                #launch_search()
                break
            case "REENTER":
                search_fun(session)
                break
            case "MAIN":
                main_menu(session)
                break

def command_handler(command, session):
    match command:
        case "HELP":
            print("Here are some sample commands")
            print("SEARCH\nEDIT\nPROFILE\nLOGOUT\n")
            command = input("Try entering one of these\n")
            command_handler(command, session)
        case "SEARCH":
            search_fun(session)
        case "EDIT":
            return
        #editFun()
        case "PROFILE":
            return
        #profileFun()
        case "LOGOUT":
            quit(session, "User logged out!")
        case _:
            command = input("Command not recognised. Try again or type HELP:\n")
            command_handler(command, session)

def main_menu(session):
    command = input("\nHello " + session.user_name + "! How can I help you today? (Type HELP if you are new)\n").strip().upper()
    command_handler(command, session)

def launch(session):
    print("Logging you in ...")
    print("Current User is " + session.user_name)

    main_menu(session)

    # Call stored procedure getAllFilms and output result to the screen
    # fetchmany, fetchone, fetchall
    #cursor.callproc('getAllFilms')
    #results = (cursor.fetchall())
    #for row in results:
    #     print(*row)

    #cursor.callproc('getAllFilms')
    #results2 = (cursor.fetchall())
    #for row in results:
    #    print(*row)
    #conn.close()

def print_welcome_message():
    print("\nHello! Welcome to FilmManager 2.0! Login to continue\n")

def main():
    security.login()

if __name__ == "__main__":
    main()

