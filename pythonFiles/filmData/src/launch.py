from util import secure_quit, secure_input
from edit import edit_fun
from search import search_fun
from profile import profile_fun

def command_handler(command, session):
    match command:
        case "HELP":
            print("Here are some sample commands")
            print("SEARCH\nEDIT\nPROFILE\nLOGOUT\n")
            command = secure_input("Try entering one of these\n").upper().split()[0]
            command_handler(command, session)
        case "SEARCH":
            search_fun(session)
        case "EDIT":
            edit_fun(session)
        case "PROFILE":
            profile_fun(session)
        case "LOGOUT":
            secure_quit(session, "User logged out!")
        case _:
            command = secure_input("Command not recognised. Try again or type HELP:\n").upper().split()[0]
            command_handler(command, session)
    main_menu(session)

def main_menu(session):
    command = secure_input("\nHello " + session.get_user().get_user_name() + "! How can I help you today? (Type HELP if you are new)\n").split()[0].upper()
    command_handler(command, session)

def launch(session):
    if session is None:
        secure_quit(session, "A strange error occurred")
    print("Logging you in ...")
    print("Current User is " + session.get_user().get_user_name())

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