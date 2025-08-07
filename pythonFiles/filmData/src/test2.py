import pyotp

def authenticate_2fa(user_secret):
    totp = pyotp.TOTP(user_secret)
    user_otp = input("Enter the 2FA code from your app: ")

    if totp.verify(user_otp):
        print("2FA passed. Login successful.")
    else:
        print("Invalid 2FA code.")

# Paste the saved secret here
saved_secret = "HSLL5GXPRDHZI57H6N4MDK3BARVRMRXX"
authenticate_2fa(saved_secret)