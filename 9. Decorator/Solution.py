class User:
    def __init__(self, is_logged_in=False):
        self.is_logged_in = is_logged_in

    def login(self):
        self.is_logged_in = True

    def logout(self):
        self.is_logged_in = False

    def view_account_info(self):
        print("Displaying account info.")


class PasswordResetRequest:
    def __init__(self, user):
        self.user = user

    def request_password_reset(self):
        print("Sending password reset email.")


class PasswordResetRequestWithLoginRequired(PasswordResetRequest):
    def request_password_reset(self):
        if self.user.is_logged_in:
            super().request_password_reset()
        else:
            print("Error: Cannot request password reset if not logged in.")


if __name__ == "__main__":
    user = User()
    reset_request = PasswordResetRequest(user)
    reset_request_with_login_required = PasswordResetRequestWithLoginRequired(user)

    # This should fail because the user is not logged in
    reset_request_with_login_required.request_password_reset()

    # Now we'll log the user in and try again
    user.login()
    reset_request_with_login_required.request_password_reset()