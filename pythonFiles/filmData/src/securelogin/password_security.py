import bcrypt

#Password class
class Password:
    def __init__(self, password, secret):
        self.password = password
        self.secret = secret

    # GETTER METHODS #
    def get_password(self):
        return self.password

    def get_secret(self):
        return self.secret

#Function to write password
def write_new_password(session, new_password, secret):
    session.get_cursor().callproc('insertPassword', [session.get_user().get_user_name(), password_encrypter(new_password), secret])
    session.commit()

def read_two_fa(session):
    session.get_cursor().callproc('readPasswords', [session.get_user().get_user_name()])
    results = session.get_cursor().fetchone()
    return results[1]

def read_password(session):
    session.get_cursor().callproc('readPasswords', [session.get_user().get_user_name()])
    results = session.get_cursor().fetchone()
    return results[0]

#Function to read password
def is_account(session):
    session.get_cursor().callproc('readPasswords', [session.get_user().get_user_name()])
    results = session.get_cursor().fetchone()
    if not results:
        return False
    else :
        return True

def is_two_fa(session):
    session.get_cursor().callproc('readPasswords', [session.get_user().get_user_name()])
    results = session.get_cursor().fetchone()
    if not results[1]:
        return False
    else :
        return True

def do_passwords_match(session, entered_password):
    encrypted_password = read_password(session).encode('utf-8')
    check_password = entered_password.encode('utf-8')

    if bcrypt.checkpw(check_password, encrypted_password):
        return True
    else:
        return False

#Function to encrypt password
def password_encrypter(plain_password):
    password_bytes = plain_password.encode('utf-8')
    hashed_bytes = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
    return hashed_bytes.decode('utf-8')  # <-- decode to string

#Function to check password strength
def password_checker(password):
    failure = False
    # check password is minimum 8 letters
    if len(password) < 8:
        print("Password must be min 8 characters")
        failure = True

    # check if password contains upperCase
    has_h = False
    has_l = False
    has_symbol = False
    has_digit = False

    for char in password :
        if 'A' <= char <= 'Z':
            has_h = True
        elif 'a' <= char <= 'z':
            has_l = True
        elif '0' <= char <= '9':
            has_digit = True
        elif char == '\n' :
            continue
        else :
            has_symbol = True
    if not has_l or not has_h :
        print("Password must contain upper and lower")
        failure = True

    # check if password contains symbol
    if not has_symbol :
        print("Password must contain a symbol")
        failure = True

    # check if password contains digit
    if not has_digit :
        print("Password must contain a digit")
        failure = True

    return failure