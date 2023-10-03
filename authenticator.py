import json
from encryptor import Encryptor

class Authenticator:
    def __init__(self):
        self.logged_in_user = None
        self.encryptor = Encryptor()  # Make sure to initialize the encryptor
        self.credentials = self.load_credentials()

    def load_credentials(self):
        try:
            with open("credentials.json", "r") as file:
                encrypted_credentials = json.load(file)

            credentials = {}
            for username, encrypted_password in encrypted_credentials.items():
                password = self.encryptor.decrypt_password(encrypted_password)
                credentials[username] = password

            return credentials
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def save_credentials(self):
        credentials_to_save = {}
        for username, password in self.credentials.items():
            # Convert the bytes password to a string representation
            password_str = password.decode('utf-8')
            credentials_to_save[username] = password_str

        with open("credentials.json", "w") as file:
            json.dump(credentials_to_save, file, indent=4)

    def create_or_update_user(self, username, password):
        hashed_password = self.encryptor.hash_password(password)
        self.credentials[username] = hashed_password
        self.save_credentials()

    def validate_user(self, username, password):
        hashed_password = self.credentials.get(username)
        if hashed_password and self.encryptor.check_password(password, hashed_password):
            self.logged_in_user = username
            return True
        return False

