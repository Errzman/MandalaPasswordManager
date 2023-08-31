import json

class CredController:
    def __init__(self, logged_in_username):
        self.logged_in_username = logged_in_username
        self.filename = f"{logged_in_username}_credentials.json"
        self.credentials = self.load_credentials()

    def load_credentials(self):
        try:
            with open(self.filename, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_credentials(self):
        with open(self.filename, "w") as file:
            json.dump(self.credentials, file, indent=4)

    def add_credential(self, credential):
        self.credentials.append(credential)
        self.save_credentials()

    def remove_credential(self, username):
        self.credentials = [cred for cred in self.credentials if cred['userName'] != username]
        self.save_credentials()

    def modify_credential(self, username, new_credential):
        for cred in self.credentials:
            if cred['userName'] == username:
                cred.update(new_credential)
        self.save_credentials()