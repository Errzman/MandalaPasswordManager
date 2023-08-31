import bcrypt

class Encryptor:
    def hash_password(self, password):
        # Generate a salt and hash the password
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed_password

    def check_password(self, password, hashed_password):
        # Encode the provided password before checking
        encoded_password = password.encode('utf-8')
        hash_encoded_password = hashed_password.encode('utf-8')
        # Check if the provided password matches the hashed password
        return bcrypt.checkpw(encoded_password, hash_encoded_password)