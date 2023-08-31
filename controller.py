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
                # Implement List Saved Credentials
                pass
            elif choice == '2':
                # Implement Search Saved Credentials
                pass
            elif choice == '3':
                # Implement Create New/Modify Credential
                pass
            elif choice == '4':
                # Implement Create New/Modify Credential
                pass
            elif choice == '5':
                # Implement Delete Credential
                pass
            elif choice == '6':
                self.view.display_message("Logged out successfully.")
                break
            elif choice == '7':
                self.view.display_message("Goodbye!")
                exit()
            else:
                self.view.display_message("Invalid choice. Please select a valid option.")