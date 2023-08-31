from authenticator import Authenticator
from view import View

class Controller:
    def __init__(self):
        self.authenticator = Authenticator()
        self.view = View()

    def run(self):
        while True:
            self.view.display_menu()
            choice = input("Enter your choice: ")

            if choice == '1':
                # Check if the credentials file exists
                if not self.authenticator.credentials:
                    self.view.display_message("No credentials found. Please create a user or select another option.")
                    continue  # Return to the main menu

                username = input("Enter your username: ")
                password = input("Enter your password: ")

                # Check if username and password are not empty
            if not username or not password:
                self.view.display_message("Username and password cannot be empty. Please try again.")
                continue  # Return to the main menu

                if self.authenticator.validate_user(username, password):
                    self.view.display_message("Login successful!")
                    self.user_menu()  # User menu is displayed after successful login
                else:
                    self.view.display_message("Invalid username or password. Please try again.")
            elif choice == '2':
                username = input("Enter the username: ")
                password = input("Enter the new password: ")
                self.authenticator.create_or_update_user(username, password)
                self.view.display_message("User created/updated successfully.")
            elif choice == '3':
                self.view.display_message("Goodbye!")
                break
            else:
                self.view.display_message("Invalid choice. Please select a valid option.")

                
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

    def list_saved_credentials(self):
        if not self.authenticator.credentials:
            self.view.display_message("No credentials found. Please create a user or select another option.")
            return

        for cred in self.cred_controller.credentials:
            self.view.display_message(f"Username: {cred['userName']}")
            self.view.display_message(f"Credential Name: {cred['credName']}")
            self.view.display_message(f"Credential Context: {cred['credContext']}")
            self.view.display_message(f"Credential Password: {cred['credPwd']}")
            self.view.display_message("-" * 20)

    def search_saved_credentials(self):
        # Implement the logic to search saved credentials using the CredController
        pass

    def create_new_credential(self):
        user_name = self.authenticator.logged_in_user
        cred_name = input("Enter the Credential Name: ")
        cred_context = input("Enter the Credential Context: ")

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
        use_symbols = input("Include Symbols (Y/N)? ").strip().lower() == 'y'

        # Generate a password using the PwdGenerator
        password_generator = PwdGenerator(
            pwd_length=pwd_length,
            use_uppercase=use_uppercase,
            use_lowercase=use_lowercase,
            use_numbers=use_numbers,
            use_symbols=use_symbols
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
        
    def modify_credential(self):
        # Implement the logic to modify a credential using the CredController
        pass

    def delete_credential(self):
        # Implement the logic to delete a credential using the CredController
        pass