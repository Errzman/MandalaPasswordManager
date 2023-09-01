# Import necessary classes from other modules
from authenticator import Authenticator
from view import View
from pwdgenerator import PwdGenerator
from credcontroller import CredController
import getpass

# Define the Controller class
class Controller:
    def __init__(self):
        # Initialize the Authenticator, View, and CredController objects
        self.authenticator = Authenticator()
        self.view = View()
        self.cred_controller = None

    # Method to run the main controller loop
    def run(self):
        while True:
            self.view.display_menu()
            choice = input("Enter your choice: ")

            if choice == '1':
                self.login_menu()
            elif choice == '2':
                self.create_update_user_menu()
            elif choice == '3':
                self.view.display_message("Goodbye!")
                break
            else:
                self.view.display_message("Invalid choice. Please select a valid option.")

    def login_menu(self):
        if not self.authenticator.credentials:
            self.view.display_message("No credentials found. Please create a user or select another option.")
            return

        username = input("Enter your username: ")
        password = getpass.getpass("Enter your password: ")

        if not username or not password:
            self.view.display_message("Username and password cannot be empty. Please try again.")
            return

        if self.authenticator.validate_user(username, password):
            self.cred_controller = CredController(username)
            self.view.display_message("Login successful!")
            self.user_menu()
        else:
            self.view.display_message("Invalid username or password. Please try again.")

    def create_update_user_menu(self):
        username = input("Enter the username: ")

        if username in self.authenticator.credentials:
            existing_password = getpass.getpass("Enter the existing password: ")
            if not self.authenticator.validate_user(username, existing_password):
                print("Incorrect existing password. Aborting operation.")
                return

        while True:
            new_password1 = getpass.getpass("Enter the new password: ")
            new_password2 = getpass.getpass("Confirm the new password: ")

            if new_password1 == new_password2:
                self.authenticator.create_or_update_user(username, new_password1)
                self.view.display_message("User created/updated successfully.")
                break
            else:
                print("Passwords do not match. Please try again.")


    # Method to display the user menu and handle user choices
    def user_menu(self):
        while True:
            self.view.display_user_menu()
            choice = self.view.get_user_choice()

            if choice == '1':
                # List Saved Credentials
                self.list_saved_credentials()
            elif choice == '2':
                # Search Saved Credentials
                self.search_saved_credentials()
            elif choice == '3':
                # Create New Credential
                self.create_new_credential()
            elif choice == '4':
                # Modify Credential
                self.modify_credential()
            elif choice == '5':
                # Delete Credential
                self.delete_credential()
            elif choice == '6':
                self.view.display_message("Logged out successfully.")
                break
            elif choice == '7':
                self.view.display_message("Goodbye!")
                exit()
            else:
                self.view.display_message("Invalid choice. Please select a valid option.")

    # Method to list saved credentials
    def list_saved_credentials(self):
        if not self.cred_controller.credentials:
            self.view.display_message("No stored credentials found.")
            return

        for cred in self.cred_controller.credentials:
            self.view.display_message("-" * 20)
            self.view.display_message(f"Username: {cred['userName']}")
            self.view.display_message(f"Credential UserName: {cred['credName']}")
            self.view.display_message(f"Credential Context: {cred['credContext']}")
            self.view.display_message(f"Credential Password: {cred['credPwd']}")
            self.view.display_message("-" * 20)

            # Display a message to hit "Enter" to continue
            input("Press Enter to continue...")


    # Method to search saved credentials
    def search_saved_credentials(self):
        # Implement the logic to search saved credentials using the CredController
        pass

    # Method to create a new credential
    def create_new_credential(self):
        user_name = self.authenticator.logged_in_user
        cred_name = input("Enter the Credential UserName: ")
        cred_context = input("Enter the Credential Context (Eg. Application or Website): ")

        # Prompt the user for password length
        while True:
            try:
                pwd_length = int(input("Enter the Password Length: "))
                if pwd_length <= 0:
                    raise ValueError()
                break
            except ValueError:
                print("Invalid input. Please enter a positive integer for the password length.")

        # Prompt the user for password generation options
        use_uppercase = input("Include Uppercase letters (Y/N)? ").strip().lower() == 'y'
        use_lowercase = input("Include Lowercase letters (Y/N)? ").strip().lower() == 'y'
        use_numbers = input("Include Numbers (Y/N)? ").strip().lower() == 'y'
        
        # Prompt the user to enter symbols
        use_symbols_input = input("Include Symbols (Y/N)? ").strip().lower()
        if use_symbols_input == 'y':
            symbols = input("Enter the symbols to include: ")
        else:
            symbols = ""

        # Generate a password using the PwdGenerator
        password_generator = PwdGenerator(
            pwd_length=pwd_length,
            use_uppercase=use_uppercase,
            use_lowercase=use_lowercase,
            use_numbers=use_numbers,
            use_symbols=symbols
        )
        cred_pwd = password_generator.generate_password()

        # Create a new credential dictionary
        new_credential = {
            'userName': user_name,
            'credName': cred_name,
            'credContext': cred_context,
            'credPwd': cred_pwd
        }

        # Add the new credential using the CredController
        self.cred_controller.add_credential(new_credential) 
        self.view.display_message("Credential created successfully.")
        
    # Method to modify a credential
    def modify_credential(self):
        # Implement the logic to modify a credential using the CredController
        pass

    # Method to delete a credential
    def delete_credential(self):
        # Implement the logic to delete a credential using the CredController
        pass
