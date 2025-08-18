# Built-In Imports
# My File Imports
from securelogin.security import login
from launch import launch

def main():
    session = login()
    launch(session)

if __name__ == "__main__":
    main()

