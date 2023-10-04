# Import necessary classes from other modules
import random
from authenticator import Authenticator
from view import View
from pwdgenerator import PwdGenerator
from credcontroller import CredController
import getpass
import os
import shutil

# Define the Controller class
class Controller:
    def __init__(self):
        # Initialize the Authenticator, View, and CredController objects
        
        self.authenticator = Authenticator()
        self.view = View()
        self.cred_controller = None
        
        # Check if a backup folder exists, if not, create one
        backup_folder = "backup"
        if not os.path.exists(backup_folder):
            os.makedirs(backup_folder)

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
                self.create_manual_backup()
            elif choice == '4':
                self.view.display_message("Goodbye!")
                break
            else:
                self.view.display_message("Invalid choice. Please select a valid option.")

    def validate_password(self, password):
        # Check if password meets the specified criteria
        return len(password) >= 12 and any(c.isdigit() for c in password) and any(c.isupper() for c in password) and any(c.islower() for c in password) and any(c in r"!@#$%^&*()-_=+[]{}|;:'\",.<>/?`~" for c in password)

    def login_menu(self):
        if not self.authenticator.credentials:
            self.view.display_message("No credentials found. Please create a user or select another option.")
            return

        username = input("Enter your username: ")
        password = getpass.getpass("Enter your password: ")

        if not username or not password:
            self.view.display_message("Username and password cannot be empty. Please try again.")
            return

        if self.validate_password(password):
            if self.authenticator.validate_user(username, password):
                self.cred_controller = CredController(username)
                self.view.display_message("Login successful!")
                self.user_menu()
            else:
                self.view.display_message("Invalid username or password. Please try again.")
        else:
            self.view.display_message("Invalid password. Please ensure it is at least 12 characters long and includes at least one number, uppercase letter, and symbol.")

    def create_update_user_menu(self):
        username = input("Enter the username: ")

        if username in self.authenticator.credentials:
            existing_password = getpass.getpass("Enter the existing password: ")
            if not self.authenticator.validate_user(username, existing_password):
                print("Incorrect existing password. Aborting operation.")
                return

        while True:
            new_password1 = getpass.getpass("Enter the new password. It must be at least 12 characters in length, and contain a Uppercase Letter, Lowercase Letter, Number and Symbol: ")
            new_password2 = getpass.getpass("Confirm the new password: ")

            if new_password1 == new_password2 and self.validate_password(new_password1):
                self.authenticator.create_or_update_user(username, new_password1)
                self.view.display_message("User created/updated successfully.")
                break
            else:
                print("Invalid password. Passwords do not match or do not meet the criteria. Please try again.")

    def create_manual_backup(self):
        backup_folder = "manual_backup"
        
        if os.path.exists(backup_folder):
            # Backup folder already exists
            user_input = input("An existing backup is already present. Do you want to replace it? (Y/N): ").strip().lower()
            
            if user_input == 'y':
                # Delete the existing backup folder
                shutil.rmtree(backup_folder)
                os.makedirs(backup_folder)
            else:
                # User chose not to replace the existing backup
                self.view.display_message("Backup creation canceled.")
                return
        else:
            # Backup folder doesn't exist, create it
            os.makedirs(backup_folder)

        # Copy all JSON files to the backup folder
        for file in os.listdir():
            if file.endswith(".json"):
                shutil.copy(file, os.path.join(backup_folder, file))

        self.view.display_message("Manual backup created successfully in 'manual_backup' folder. To use the backedup data, delete all JSON files in main directory and replace them with those in the manual_backup directory.")

    # Method to display the user menu and handle user choices
    def user_menu(self):
        while True:
            self.view.display_user_menu()
            choice = self.view.get_user_choice()

            if choice == '1':
                # List Saved Credentials
                self.list_saved_credentials()
            elif choice == '2':
                # Create New Credential
                self.create_new_credential()
            elif choice == '3':
                # Modify Credential
                self.modify_credential()
            elif choice == '4':
                # Delete Credential
                self.delete_credential()
            elif choice == '5':
                self.view.display_message("Logged out successfully.")
                break
            elif choice == '6':
                self.view.display_message("Goodbye!")
                exit()
            else:
                self.view.display_message("Invalid choice. Please select a valid option.")

    # Method to list saved credentials
    def list_saved_credentials(self):
        if not self.cred_controller.credentials:
            self.view.display_message("No stored credentials found.")
            return

        # Display the list of existing credentials
        self.display_existing_credentials()

        credentials = self.cred_controller.credentials

        while True:
            self.view.display_message("Enter the number of the credential to display the password (0 to cancel): ")

            try:
                choice = int(input())
                if choice == 0:
                    return  # Cancel operation

                if 1 <= choice <= len(credentials):
                    selected_credential = credentials[choice - 1]
                    old_password = selected_credential.get('oldPwd', "N/A")
                    current_password = selected_credential['credPwd']
    
                    self.view.display_message("-" * 20)
                    self.view.display_message(f"Old Password: {old_password}")
                    self.view.display_message(f"Current Password: {current_password}")
                    self.view.display_message("-" * 20)
                    self.view.display_message("Press Enter to continue...")
                    input()  # Wait for user input
                    return
                else:
                    raise ValueError()
            except ValueError:
                self.view.display_message("Invalid input. Please enter a valid number or 0 to cancel.")


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

        # Create a dictionary with password generation parameters
        password_params = {
            'pwd_length': pwd_length,
            'use_uppercase': use_uppercase,
            'use_lowercase': use_lowercase,
            'use_numbers': use_numbers,
            'use_symbols': symbols
        }


        # Create a new credential dictionary
        new_credential = {
            'userName': user_name,
            'credName': cred_name,
            'credContext': cred_context,
            'credPwd': cred_pwd,
            'PwdSettings': password_params
        }

        # Add the new credential using the CredController
        self.cred_controller.add_credential(new_credential) 
        self.view.display_message("Credential created successfully.")
        
    # Method to modify a credential
    def modify_credential(self):
        # Generate and display the list of existing credentials
        self.display_existing_credentials()

        # Access the credentials from the CredController
        credentials = self.cred_controller.credentials

        # Prompt the user to select a credential by entering the associated number
        while True:
            try:
                choice = int(input("Enter the number of the credential to modify (0 to cancel): "))
                if choice == 0:
                    return  # Cancel modification
                if 1 <= choice <= len(credentials):
                    selected_credential = credentials[choice - 1]
                    break
                else:
                    raise ValueError()
            except ValueError:
                print("Invalid input. Please enter a valid number or 0 to cancel.")

        # Prompt the user whether they want to generate a new password
        while True:
            generate_new_password = input("Generate a new password using existing settings (Y/N)? ").strip().lower()
            if generate_new_password == 'y':
                # Generate a new password using the existing settings
                password_generator = PwdGenerator(
                    pwd_length=selected_credential['PwdSettings']['pwd_length'],
                    use_uppercase=selected_credential['PwdSettings']['use_uppercase'],
                    use_lowercase=selected_credential['PwdSettings']['use_lowercase'],
                    use_numbers=selected_credential['PwdSettings']['use_numbers'],
                    use_symbols=selected_credential['PwdSettings']['use_symbols']
                )
                new_password = password_generator.generate_password()
                selected_credential['oldPwd'] = selected_credential['credPwd']  # Store the old password
                selected_credential['credPwd'] = new_password
                self.view.display_message("New password generated and updated.")
                break
            elif generate_new_password == 'n':
                # Keep the existing password
                self.view.display_message("Password not changed.")
                break
            else:
                print("Invalid input. Please enter 'Y' for Yes or 'N' for No.")

        # Save the updated credentials list using the CredController
        self.cred_controller.save_credentials()
        self.view.display_message("Credential password modified successfully.")
        self.view.display_message("Please update your password using the following information:")
        self.view.display_message(f"Old Password:" + selected_credential['oldPwd'])
        self.view.display_message(f"Current Password: " + selected_credential['credPwd'])

    # Method to delete a credential
    def delete_credential(self):
        # Display the list of existing credentials
        self.display_existing_credentials()
    
        credentials = self.cred_controller.credentials
    
        while True:
            try:
                # Prompt the user to select a credential by entering the associated number
                choice = int(input("Enter the number of the credential to delete (0 to cancel): "))
                if choice == 0:
                    return  # Cancel operation
    
                if 1 <= choice <= len(credentials):
                    selected_credential = credentials[choice - 1]
    
                    # Ask for user confirmation
                    confirmation = input(f"Are you sure you want to delete '{selected_credential['credName']}'? (Y/N): ").strip().lower()
                    if confirmation == 'y':
                        # Generate a random 4-digit code
                        verification_code = str(random.randint(1000, 9999))

                         # Display the verification code to the user
                        self.view.display_message(f"Verification Code: {verification_code}")
    
                        # Prompt the user to enter the verification code
                        user_code = input(f"Enter the 4-digit verification code to confirm deletion: ")
    
                        if user_code == verification_code:
                            # Delete the selected credential using the CredController
                            self.cred_controller.remove_credential(selected_credential['credName'])
                            self.view.display_message("Credential deleted successfully.")
                            return
                        else:
                            self.view.display_message("Incorrect verification code. Deletion canceled.")
                            return
                    elif confirmation == 'n':
                        self.view.display_message("Deletion canceled.")
                        return
                    else:
                        self.view.display_message("Invalid input. Please enter 'Y' for Yes or 'N' for No.")
                else:
                    raise ValueError()
            except ValueError:
                self.view.display_message("Invalid input. Please enter a valid number or 0 to cancel.")

    
    # Method to generate and display the list of existing credentials
    def display_existing_credentials(self):
        credentials = self.cred_controller.credentials

        # Check if there are any credentials to display
        if not credentials:
            self.view.display_message("No credentials found.")
            return

        # Display the list of credentials to the user
        self.view.display_message("List of Existing Credentials:")
        for i, credential in enumerate(credentials, start=1):
            self.view.display_message(f"{i}. {credential['credName']} ({credential['credContext']})")