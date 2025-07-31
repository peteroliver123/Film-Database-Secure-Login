# Connecting to Server
import pymysql

class CurrentSession:
    def __init__(self, name):
        self.user_name = name

def search_fun():
    age_range_bool = False
    id_range_bool = False
    is_film_name = False
    is_age_rating = False
    is_id_number = False
    is_location = False
    print("Welcome to Search!")
    film_name = input("Enter film name (to search by name or press enter to leave blank)")
    if film_name != "\n" :
        is_film_name = True
    age_rating = input("Enter an age rating (to search by name or press enter to leave blank)")
    if age_rating != "\n" :
        is_age_rating = True
        reply = input("Would you like to enter a range: (Y/N)")
        if reply == "Y" :
          age_range_bool = True
    id_number = input("Enter an id (to search by id or press enter to leave blank)")
    if id_number != "\n" :
        is_id_number = True
        reply = input("Would you like to enter a range: (Y/N)")
        if reply == "Y" :
            id_range_bool = True
    location = input("Enter a location (to search by location or press enter to leave blank)")
    if location != "\n" :
        is_location = True



def command_handler(command):
    match command:
        case "HELP":
           print("Here are some sample commands")
           print("SEARCH\nEDIT\nPROFILE\nLOGOUT\n")
           command = input("Try entering one of these\n")
           command_handler(command)
        case "SEARCH":
            search_fun()
        case "EDIT":
            return
           #editFun()
        case "PROFILE":
            return
           #profileFun()
        case "LOGOUT":
            exit("User logged out!")
        case _:
            command = input("Command not recognised. Try again or type HELP:\n")
            command_handler(command)

def launch(name):
    print("Logging you in ...")
    s = CurrentSession(name)
    print("Current User is " + s.user_name)

    conn = pymysql.connect(host="localhost", user="root", password="Founders72!", database="record_boxes")
    print("Connected to FilmDatabase!")

    command = input("\nHello " + s.user_name + "! How can I help you today? (Type HELP if you are new)\n").strip().upper()
    command_handler(command)

    #Cursor Setup
    cursor = conn.cursor()

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
    conn.close()

def create_new_user(new_name):
    file = open("files/passwords.txt", "a")
    new_password = input("Enter a password: ")
    confirm_password = input("Confirm password: ")
    if new_password == confirm_password :
        file.write(new_name + " " + new_password.strip() + "\n")
        file.close()
        launch(new_name)
    else :
        file.close()
        print("Passwords didn't match!")
        create_new_user(new_name)


def read_passwords(user_name):
    file = open("files/passwords.txt", "r")
    for row in file:
        name, password = row.strip().split()
        if name == user_name:
            file.close()
            return password
    file.close()
    return -1

def login():
    print("\nHello! Welcome to FilmManager 2.0! Login to continue\n")
    name = input("Enter Username: ").strip()
    stored_password = read_passwords(name)
    if stored_password != -1:
        while True:
            password = input("Enter Password: ").strip()
            if password.upper() == "CANCEL" :
                login()
            elif password == stored_password:
                print("Password Correct!")
                launch(name)
                break
            else :
                print("Password Incorrect! Type CANCEL to try another name or enter correct password")

    else:
        while True:
            command = input(f"Username {name} does not exist.\nType CREATE to make this a username, type CANCEL to try another name\n").upper()
            if command == "CREATE":
                create_new_user(name)
                break
            elif command == "CANCEL":
                login()


def main():
    login()




if __name__ == "__main__":
    main()

