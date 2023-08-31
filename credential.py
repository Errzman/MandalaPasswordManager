class Credential:
    def __init__(self, user_name, cred_name, cred_context, cred_pwd):
        self.user_name = user_name
        self.cred_name = cred_name
        self.cred_context = cred_context
        self.cred_pwd = cred_pwd

    def __str__(self):
        return f"UserName: {self.user_name}\nCredentialName: {self.cred_name}\nCredentialContext: {self.cred_context}\nCredentialPassword: {self.cred_pwd}"
