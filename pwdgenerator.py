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
        character_sets = []

        if self.use_uppercase:
            character_sets.append(string.ascii_uppercase)
        if self.use_lowercase:
            character_sets.append(string.ascii_lowercase)
        if self.use_numbers:
            character_sets.append(string.digits)
        if self.use_symbols:
            character_sets.append(self.use_symbols)

        if not character_sets:
            raise ValueError("At least one character set must be selected")

        password = []

        for _ in range(self.pwd_length):
            char_set = random.choice(character_sets)
            password.append(random.choice(char_set))

        return ''.join(password)