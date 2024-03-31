from Season import Season
from Teams import Teams


class Association:
    def __init__(self):
        self.teams = Teams()
        self.season = Season()

    def use(self):
        print("Welcome to the Association! Please make a selection from the menu:\n"
              "1. Explore the teams.\n"
              "2. Arrange a new season.\n"
              "X. Exit the system.")
        choice = input("Enter a choice: ")

        if choice == "1":
            Teams.main_menu()
        elif choice == "2":
            Season.main_menu()
        elif choice.upper() == "X":
            print("Done")
        else:
            print("Please enter a number 1 or 2, or press X to exit.")
            self.use()

    @staticmethod
    def user():
        print("Welcome to the Association! Please make a selection from the menu:\n"
              "1. Explore the teams.\n"
              "2. Arrange a new season.\n"
              "X. Exit the system.")
        choice = input("Enter a choice: ")

        if choice == "1":
            Teams.main_menu()
        elif choice == "2":
            Season.main_menu()
        elif choice.upper() == "X":
            print("Done")
        else:
            print("Please enter a number 1 or 2, or press X to exit.")
            Association.user()

if __name__ == "__main__":
    Association().use()