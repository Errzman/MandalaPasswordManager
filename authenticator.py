from encryptor import Encryptor
import json

class Authenticator:
    def __init__(self):
        self.credentials = self.load_credentials()
        self.encryptor = Encryptor()

    def load_credentials(self):
        try:
            with open("credentials.json", "r") as file:
              return json.load(file)
        except FileNotFoundError:
          print("Credentials file not found. Returning to main menu.")
          return {}
        except json.JSONDecodeError as e:
         print(f"Error decoding credentials file: {e}. Returning to main menu.")
        return {}


    def save_credentials(self):
        credentials_to_save = {username: password.decode('utf-8') for username, password in self.credentials.items()}
        with open("credentials.json", "w") as file:
            json.dump(credentials_to_save, file, indent=4)

    def create_or_update_user(self, username, password):
        hashed_password = self.encryptor.hash_password(password)
        self.credentials[username] = hashed_password
        self.save_credentials()

    def validate_user(self, username, password):
        hashed_password = self.credentials.get(username)
        return hashed_password and self.encryptor.check_password(password, hashed_password)
