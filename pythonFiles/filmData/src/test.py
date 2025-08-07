import pyotp
import qrcode

def set_up_2fa():
    user_email = "Brackenp18@gmail.com"
    secret = pyotp.random_base32()
    totp = pyotp.TOTP(secret)

    uri = totp.provisioning_uri(name=user_email, issuer_name="GoogleAuthenticator")
    img = qrcode.make(uri)
    img.show()

    print("Save this secret:", secret)  # 👈 COPY THIS
    return secret

set_up_2fa()
