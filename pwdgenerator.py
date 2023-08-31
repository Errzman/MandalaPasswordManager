import random
import string

class PwdGenerator:
    def __init__(self, pwd_length=12, use_uppercase=True, use_lowercase=True, use_numbers=True, use_symbols="!@#$%^&*()_-+=<>?"):
        self.pwd_length = pwd_length
        self.use_uppercase = use_uppercase
        self.use_lowercase = use_lowercase
        self.use_numbers = use_numbers
        self.use_symbols = use_symbols

    def generate_password(self):
        # Define character sets based on options
        characters = ""
        if self.use_uppercase:
            characters += string.ascii_uppercase
        if self.use_lowercase:
            characters += string.ascii_lowercase
        if self.use_numbers:
            characters += string.digits
        characters += self.use_symbols

        # Check if at least one character set is selected
        if not characters:
            raise ValueError("At least one character set must be selected")

        # Generate the password
        password = ''.join(random.choice(characters) for _ in range(self.pwd_length))
        return password