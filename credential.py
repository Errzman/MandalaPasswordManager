# Define the Credential class to represent user credentials
class Credential:
    # Constructor to initialize the credential attributes
    def __init__(self, user_name, cred_name, cred_context, cred_pwd):
        self.user_name = user_name        # Username associated with the credential
        self.cred_name = cred_name        # Name of the credential
        self.cred_context = cred_context  # Context or description of the credential
        self.cred_pwd = cred_pwd          # Password associated with the credential

    # Method to provide a string representation of the credential
    def __str__(self):
        # Format the credential information as a string
        return (
            f"UserName: {self.user_name}\n"
            f"CredentialName: {self.cred_name}\n"
            f"CredentialContext: {self.cred_context}\n"
            f"CredentialPassword: {self.cred_pwd}"
        )
