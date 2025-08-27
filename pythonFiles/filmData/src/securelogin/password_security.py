# Third Party Imports
import bcrypt

#software that changes code from one convention to another
#Function to write to password table
def write_new_password(session, new_password, secret):
    session.get_cursor().callproc('InsertPassword', [session.get_user().get_user_name(),
                                                     password_encrypter(new_password), secret])
    session.commit()


#Function to encrypt password
def password_encrypter(plain_password):
    password_bytes = plain_password.encode('utf-8')
    hashed_bytes = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
    return hashed_bytes.decode('utf-8')  # <-- decode to string


# Functions to read password table
def read_passwords_data(session):
    session.get_cursor().callproc('ReadPasswords', [session.get_user().get_user_name()])
    results = session.get_cursor().fetchone()
    return results


def read_two_fa(session):
    return read_passwords_data(session)[1]


def read_password(session):
    return read_passwords_data(session)[0]


# Function to check if given password matches stored
def do_passwords_match(session, entered_password):
    try :
        encrypted_password = read_password(session).encode('utf-8')
        check_password = entered_password.encode('utf-8')

        if bcrypt.checkpw(check_password, encrypted_password):
            return True
        else:
            return False
    except ValueError:
        # Forced Lockout
        while session.get_user().get_num_lockout() < 2:
            session.get_user().increment_num_lockout()
        return False

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

    if len(password_encrypter(password)) > 100 or len(password) > 100:
        print("Invalid Password!")
        failure = True

    return failure