from securelogin.user_classes import ExistingUserProfile



#This function reads the users file, and returns -1 if user not found
def read_users(session, user_name):
    session.get_cursor().callproc('readUsers', [user_name])
    results = session.get_cursor().fetchone()
    if not results:
        return -1
    else :
        name, date_created, is_locked, date_unlock, num_fails, is_admin = results
        is_locked = is_locked == "True"
        num_fails = int(num_fails)
        is_admin = is_admin == "True"
        return ExistingUserProfile(name, date_created, is_locked, date_unlock, num_fails, is_admin)