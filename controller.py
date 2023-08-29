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
                username = input("Enter your username: ")
                password = input("Enter your password: ")

                if self.authenticator.validate_user(username, password):
                    self.view.display_message("Login successful!")
                    # Rest of your program goes here
                    self.view.display_message("Access granted. You can now use the application.")
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