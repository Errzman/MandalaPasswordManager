import bcrypt

class Encryptor:
    def hash_password(self, password):
        # Generate a salt and hash the password
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed_password

    def check_password(self, password, hashed_password):
        # Check if the provided password matches the hashed password
        return bcrypt.checkpw(password.encode('utf-8'), hashed_password)