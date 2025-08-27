# Built-In Imports
# My File Imports
from securelogin.login import login
from launch import launch
from securelogin.user_classes import ExistingUserProfile
from securelogin.session import CurrentSession
from edit import delete_fun

TEST = 0


def main():
    if TEST:
        session = CurrentSession()
        session.open_conn()
        fake_user = ExistingUserProfile("fake", None, False, None, 0, True, 0)
        session.set_user(fake_user)
        delete_fun(session)
    else :
        session = login()
        launch(session)

if __name__ == "__main__":
    main()

