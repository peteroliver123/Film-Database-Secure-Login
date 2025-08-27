# Imports
from datetime import datetime

# Constants #
NUMBER_PASSWORD_WRONG = 3
PROJECT_NAME = "Film Manager 2.0"

# Functions #
def secure_quit(session, code):
    if session :
        session.close_conn()
    quit(code)

def secure_input(prompt):
    output = input(prompt).strip()
    while output == "":
        output = input(prompt).strip()
    return output

def write_action(action_performed):
    with open("../files/log.txt", "a") as file:
        file.write(f"{datetime.now()} : {action_performed}\n")