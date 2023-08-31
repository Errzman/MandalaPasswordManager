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
        character_sets = []
        if self.use_uppercase:
            character_sets.append(string.ascii_uppercase)
        if self.use_lowercase:
            character_sets.append(string.ascii_lowercase)
        if self.use_numbers:
            character_sets.append(string.digits)
        if self.use_symbols:
            character_sets.append(self.use_symbols)

        # Check if at least one character set is selected
        if not character_sets:
            raise ValueError("At least one character set must be selected")

        # Calculate the number of characters from each set to include
        characters_per_set = self.pwd_length // len(character_sets)
        remaining_characters = self.pwd_length % len(character_sets)

        # Initialize the password as an empty list
        password = []

        # Generate the password with equal representation of character types
        for char_set in character_sets:
            for _ in range(characters_per_set):
                password.append(random.choice(char_set))

        # Add any remaining characters randomly
        for _ in range(remaining_characters):
            char_set = random.choice(character_sets)
            password.append(random.choice(char_set))

        # Shuffle the password to mix characters from different sets
        random.shuffle(password)

        # Convert the password list to a string
        password_str = ''.join(password)
        return password_str