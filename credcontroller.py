import json

# Define the CredController class responsible for managing user credentials
class CredController:
    def __init__(self, logged_in_username):
        # Initialize the CredController with the logged-in username
        self.logged_in_username = logged_in_username
        # Define the filename for the user's credentials JSON file
        self.filename = f"{logged_in_username}_credentials.json"
        # Initialize the credentials list
        self.credentials = []
        # Load the user's credentials from the JSON file
        self.load_credentials()

    # Method to load user credentials from the JSON file
    def load_credentials(self):
        try:
            with open(self.filename, "r") as file:
                # Attempt to load the credentials from the JSON file
                self.credentials = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            # Handle exceptions if the file doesn't exist or is invalid JSON
            self.credentials = []

    # Method to add a new credential to the credentials list
    def add_credential(self, credential):
        self.credentials.append(credential)
        # Save the updated credentials list to the JSON file
        self.save_credentials()

    # Method to remove a credential with the specified username
    def remove_credential(self, username):
        self.credentials = [cred for cred in self.credentials if cred['userName'] != username]
        # Save the updated credentials list to the JSON file
        self.save_credentials()

    # Method to modify a credential with the specified username
    def modify_credential(self, username, new_credential):
        for cred in self.credentials:
            if cred['userName'] == username:
                # Update the existing credential with the new information
                cred.update(new_credential)
        # Save the updated credentials list to the JSON file
        self.save_credentials()

    # Method to save the credentials list to the JSON file
    def save_credentials(self):
        with open(self.filename, "w") as file:
            # Write the credentials list to the JSON file with proper indentation
            json.dump(self.credentials, file, indent=4)