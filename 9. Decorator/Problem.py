class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.logged_in = False

    def signup(self):
        # code to sign up a new user
        pass

    def login(self, password):
        if password == self.password:
            self.logged_in = True
            return True
        return False

    def view_account_info(self):
        if self.logged_in:
            # code to view the user's account information
            pass
        else:
            print("You must be logged in to view your account information.")

    def request_password_reset(self):
        if self.logged_in:
            print("Sending password reset email.")
        else:
            print("You must be logged in to request a password reset.")


if __name__ == "__main__":
    user = User("test", "test")
    user.request_password_reset()

    user.login("test")
    user.request_password_reset()
