# Built-In Imports
from datetime import datetime


class UserProfile:

    # Constructor #
    def __init__(self, user_name, date_created):
        # Instantiated Variables #
        self.user_name = user_name
        self.date_created = date_created
        # Default Variables #
        self.is_locked = False
        self.date_unlock = date_created
        self.num_fails = 0
        self.is_admin = False

    # GETTER Methods #
    def get_user_name(self):
        return self.user_name

    def get_date_created(self):
        return self.date_created

    def get_is_locked(self):
        return self.is_locked

    def get_date_unlock(self):
        return self.date_unlock

    def get_num_fails(self):
        return self.num_fails

    def get_is_admin(self):
        return self.is_admin

    # SETTER METHODS #
    def flip_locked(self):
        self.is_locked = self.is_locked == False

    def set_date_unlock(self, date_time):
        self.date_unlock = date_time

    def increment_num_fails(self):
        self.num_fails += 1

    def reset_num_fails(self):
        self.num_fails = 0

    def unlock_valid(self):
        if self.date_unlock == self.date_created:
            return -1
        if datetime.now() >= self.date_unlock :
            return 1
        print(f"Account locked until {self.date_unlock}!")
        return -1


class NewUserProfile(UserProfile):

    pass


class ExistingUserProfile(UserProfile):

    def __init__(self, user_name, date_created, is_locked, date_unlock,
                 num_fails, is_admin):
        super().__init__(user_name, date_created)
        self.is_locked = is_locked
        self.date_unlock = date_unlock
        self.num_fails = num_fails
        self.is_admin = is_admin


