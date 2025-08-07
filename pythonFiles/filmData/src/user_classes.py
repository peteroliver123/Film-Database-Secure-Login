# Built-In Imports
from datetime import datetime, timedelta, date

# My File Imports
from file import rewrite_file_without_line



class UserProfile:
    # Constructor #
    def __init__(self, user_name, date_created, time_created):
        # Instantiated Variables #
        self.user_name = user_name
        self.date_created = date_created
        self.time_created = time_created
        # Default Variables #
        self.is_locked = False
        self.date_unlock = None
        self.time_unlock = None
        self.num_fails = 0
        self.is_admin = False

    # GETTER Methods #
    def get_user_name(self):
        return self.user_name

    def get_date_created(self):
        return self.date_created

    def get_time_created(self):
        return self.time_created

    def get_is_locked(self):
        return self.is_locked

    def get_date_unlock(self):
        return self.date_unlock

    def get_time_unlock(self):
        return self.time_unlock

    def get_num_fails(self):
        return self.num_fails

    def get_is_admin(self):
        return self.is_admin

    def increment_num_fails(self):
        self.num_fails += 1
        self.rewrite_users()

    def write_new_user(self):
        with open("files/users.txt", "a") as file:
            file.write(f"{self.user_name} {self.date_created} {self.time_created} {self.is_locked} {self.date_unlock} {self.time_unlock} {self.num_fails} {self.is_admin}"  + "\n")

    def lock_account(self):
        self.is_locked = True
        self.date_unlock = date.today() + timedelta(days=1)
        self.time_unlock = datetime.now().time()
        self.num_fails = 0
        #rewrite file
        self.rewrite_users()

    def unlock_procedures(self):
        self.is_locked = False
        self.date_unlock = None
        self.time_unlock = None
        #rewrite file
        self.rewrite_users()
        print("Account has been unlocked! Login to continue!")

    def unlock_valid(self):
        if date.today() > self.date_unlock :
            self.unlock_procedures()
            return 1
        elif date.today() == self.date_unlock :
            if datetime.now().time() > self.time_unlock :
                self.unlock_procedures()
                return 1
        print(f"Account locked until {self.date_unlock} {self.time_unlock}!")
        return -1

    def rewrite_users(self):
        result = rewrite_file_without_line("files/users.txt", self.user_name)
        if result == -1 :
            print("Username doesn't exist!")
        else :
            self.write_new_user()

class NewUserProfile(UserProfile):
    pass

class ExistingUserProfile(UserProfile):
    def __init__(self, user_name, date_created, time_created, is_locked, date_unlock, time_unlock, num_fails, is_admin):
        super().__init__(user_name, date_created, time_created)
        self.is_locked = is_locked
        self.date_unlock = date_unlock
        self.time_unlock = time_unlock
        self.num_fails = num_fails
        self.is_admin = is_admin