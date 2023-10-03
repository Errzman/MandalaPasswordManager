import bcrypt

class Encryptor:
    def hash_password(self, password):
        # Generate a salt and hash the password
        salt = bcrypt.gensalt()
        password_bytes = password.encode('utf-8') if isinstance(password, str) else password
        hashed_password = bcrypt.hashpw(password_bytes, salt)
        return hashed_password

    def check_password(self, password, hashed_password):
        # Encode the provided password before checking
        encoded_password = password.encode('utf-8')
        # Convert the hashed password to bytes
        hashed_password_bytes = hashed_password if isinstance(hashed_password, bytes) else hashed_password.encode('utf-8')
        return bcrypt.checkpw(encoded_password, hashed_password_bytes)

    def encrypt_password(self, password):
        # Generate a salt and hash the password for storage
        hashed_password = self.hash_password(password)
        # Return the hashed password directly without base64 encoding
        return hashed_password

    def decrypt_password(self, encrypted_password):
        # No decoding needed, as bcrypt is a one-way hash
        return encrypted_password