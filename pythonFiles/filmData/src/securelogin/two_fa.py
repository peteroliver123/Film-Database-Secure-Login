import pyotp
import qrcode
from util import secure_input
from securelogin.password_security import read_two_fa


def unlock_two_fa(session):
    secret = read_two_fa(session)
    if secret:
        print("You are locked out! But can get back into your account using 2fa.")
        user_otp = secure_input("Enter the onetime passcode on your two "
                                "factor app (NO SPACES):\n")
        totp = pyotp.TOTP(secret)
        if totp.verify(user_otp):
            print("2FA correct!")
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
                              "recovery and reset: (Y/N): ")
        if result.upper() == "Y" or result.upper() == "YES":
            return two_fa_setup()
        elif result.upper() == "N" or result.upper() == "NO":
            return None


def two_fa_setup():
    user_email = secure_input("Enter your email address: ")
    secret = pyotp.random_base32()
    totp = pyotp.TOTP(secret)
    uri = totp.provisioning_uri(name=user_email, issuer_name="GoogleAuthenticator")
    img = qrcode.make(uri)
    img.show()
    print("Scan the QR code in the GoogleAuthenticator App to finish setup")
    return secret