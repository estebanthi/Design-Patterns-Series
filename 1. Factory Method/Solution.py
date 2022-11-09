from abc import ABC, abstractmethod


class Dialog(ABC):
    @abstractmethod
    def render(self):
        pass


class WindowsDialog(Dialog):
    def render(self):
        return "WindowsDialog"


class macOSDialog(Dialog):
    def render(self):
        return "macOSDialog"


class LinuxDialog(Dialog):
    def render(self):
        return "LinuxDialog"


class Button(ABC):
    @abstractmethod
    def render(self):
        pass


class WindowsButton(Button):
    def render(self):
        return "WindowsButton"


class macOSButton(Button):
    def render(self):
        return "macOSButton"


class LinuxButton(Button):
    def render(self):
        return "LinuxButton"


class DialogFactory:
    @staticmethod
    def get_dialog(config):
        if config == "Windows":
            return WindowsDialog()
        elif config == "macOS":
            return macOSDialog()
        elif config == "Linux":
            return LinuxDialog()
        else:
            raise Exception("Unknown config")


class ButtonFactory:
    @staticmethod
    def get_button(config):
        if config == "Windows":
            return WindowsButton()
        elif config == "macOS":
            return macOSButton()
        elif config == "Linux":
            return LinuxButton()
        else:
            raise Exception("Unknown config")


class Application:
    def __init__(self, config):
        self.dialog = DialogFactory.get_dialog(config)
        self.button = ButtonFactory.get_button(config)

    def render(self):
        return self.dialog.render() + " " + self.button.render()


if __name__ == "__main__":
    app = Application("Windows")
    print(app.render())

    app = Application("macOS")
    print(app.render())

    app = Application("Linux")
    print(app.render())

    app = Application("Unknown")
    print(app.render())