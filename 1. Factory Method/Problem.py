class WindowsDialog:
    def render(self):
        return "WindowsDialog"


class macOSDialog:
    def render(self):
        return "macOSDialog"


if __name__ == "__main__":
    config = "Windows"
    if config == "Windows":
        dialog = WindowsDialog()
    elif config == "macOS":
        dialog = macOSDialog()
    else:
        raise Exception("Error!")

    print(dialog.render())
