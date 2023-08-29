class View:
    def display_menu(self):
        print("Main Menu:")
        print("1. Login")
        print("2. Create/Update User")
        print("3. Quit")

    def display_message(self, message):
        print(message)

    def display_user_menu(self):
        print("\nUser Menu:")
        print("1. List Saved Credentials")
        print("2. Search Saved Credentials")
        print("3. Create New/Modify Credential")
        print("4. Delete Credential")
        print("5. Logout")
        print("6. Quit")

    def get_user_choice(self):
        return input("Enter your choice: ")