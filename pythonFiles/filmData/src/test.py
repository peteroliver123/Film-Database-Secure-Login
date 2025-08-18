import bcrypt

# Hashing a password
password = b"super_secret_password"
hashed = bcrypt.hashpw(password, bcrypt.gensalt())

print(hashed)  # stored in DB

# Verifying a password
entered = b"super_secret_password"
if bcrypt.checkpw(entered, hashed):
    print("Password matches!")
else:
    print("Invalid password")
