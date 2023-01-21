class File:
    def __init__(self, file_path):
        self.file_path = file_path

    def download(self):
        print(f'Downloading {self.file_path}')


class FileProxy:
    def __init__(self, file_path, user):
        self.file = File(file_path)
        self.user = user

    def download(self):
        if self.user != 'admin':
            print('You are not authorized to download this file')
        else:
            self.file.download()


class User:
    def __init__(self, name):
        self.name = name

    def download_file(self, file):
        file.download()


if __name__ == "__main__":
    user = User('guest')
    file = FileProxy('important_file.txt', user.name)
    user.download_file(file)

    user = User('admin')
    file = FileProxy('important_file.txt', user.name)
    user.download_file(file)
