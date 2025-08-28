# Built-In Imports
# My File Imports
from securelogin.login import login
from launch import launch
from securelogin.user_classes import ExistingUserProfile
from securelogin.session import CurrentSession
from util import write_action

TEST = 0

def main():
    if TEST:
        session = CurrentSession()
        session.open_conn()
        fake_user = ExistingUserProfile("ADMIN", None, False, None, 0, True, 0)
        session.set_user(fake_user)
        launch(session)
    else :
        session = login()
        write_action(f"User {session.get_user().get_user_name()} logged in!")
        launch(session)

if __name__ == "__main__":
    main()

