# Built-In Imports
from datetime import datetime

from util import secure_quit


class UserProfile:

    # Constructor #
    def __init__(self, user_name, date_created):
        # Instantiated Variables #
        self.user_name = user_name
        if self.user_name is None:
            secure_quit(None, "Something nefarious is occurring!")
        self.date_created = date_created
        if self.date_created is None:
            secure_quit(None, "Something nefarious is occurring!")
        # Default Variables #
        self.is_locked = False
        self.date_unlock = date_created
        self.num_lockout = 0
        self.is_admin = False
        self.failed_entry = 0

    # GETTER Methods #
    def get_user_name(self):
        return self.user_name

    def get_date_created(self):
        return self.date_created

    def get_is_locked(self):
        return self.is_locked

    def get_date_unlock(self):
        return self.date_unlock

    def get_num_lockout(self):
        return self.num_lockout

    def get_is_admin(self):
        return self.is_admin

    def get_failed_entry(self):
        return self.failed_entry

    # SETTER METHODS #
    def set_user_name(self, new_name):
        self.user_name = new_name

    def flip_locked(self):
        self.is_locked = self.is_locked == False

    def set_date_unlock(self, date_time):
        self.date_unlock = date_time

    def increment_num_lockout(self):
        self.num_lockout += 1

    def increment_failed_entry(self):
        self.failed_entry += 1

    def reset_failed_entry(self):
        self.failed_entry = 0

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
                 num_lockout, is_admin, failed_entry):
        super().__init__(user_name, date_created)
        self.is_locked = is_locked
        self.date_unlock = date_unlock
        self.num_lockout = num_lockout
        self.is_admin = is_admin
        self.failed_entry = failed_entry



