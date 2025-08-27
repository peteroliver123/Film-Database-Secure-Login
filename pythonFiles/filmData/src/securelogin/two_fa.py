import pyotp
import qrcode
from util import secure_input, secure_quit, write_action
from securelogin.password_security import read_two_fa


def unlock_two_fa(session):
    secret = read_two_fa(session)
    if secret:
        user_otp = secure_input("Enter the onetime passcode on your two "
                                "factor app to continue (NO SPACES):\n")
        totp = pyotp.TOTP(secret)
        if totp.verify(user_otp):
            print("2FA correct!")
            write_action(f"User {session.get_user().get_user_name()} successfully verified 2fa")
            return 1
        else:
            print("Invalid 2FA code.")
            return -1
    else :
        return -1


def two_fa_option():
    while True:
        print("Would you like to add two factor authentication to your account")
        result = secure_input("This will be needed for account "
                              "recovery and reset: (Y/N): ").upper()
        if result == "Y" or result == "YES":
            return two_fa_setup()
        elif result == "N" or result == "NO":
            return None


def two_fa_setup():
    user_email = secure_input("Enter your email address: ")
    if len(user_email) > 65:
        write_action(f"User attempted to enter email that would break the system")
        secure_quit(None, "User attempted to break system!")
    secret = pyotp.random_base32()
    totp = pyotp.TOTP(secret)
    uri = totp.provisioning_uri(name=user_email, issuer_name="GoogleAuthenticator")
    img = qrcode.make(uri)
    img.show()
    print("Scan the QR code in the GoogleAuthenticator App to finish setup")
    write_action(f"User successfully triggered 2fa setup")
    return secret