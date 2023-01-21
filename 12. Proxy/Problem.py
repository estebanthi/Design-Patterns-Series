class File:
    def __init__(self, file_path):
        self.file_path = file_path

    def download(self):
        # Code to download the file
        print(f'Downloading {self.file_path}')

class User:
    def __init__(self, name):
        self.name = name

    def download_file(self, file):
        if self.name != 'admin':
            print('You are not authorized to download this file')
        else:
            file.download()


if __name__ == "__main__":
    file = File('important_file.txt')
    user = User('guest')
    user.download_file(file)

    user = User('admin')
    user.download_file(file)
