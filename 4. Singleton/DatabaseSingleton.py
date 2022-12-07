class DatabaseSingleton:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(DatabaseSingleton, cls).__new__(cls, *args, **kwargs)
        return cls.__instance

    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.initialized = True
            self.connection = None

    def connect(self):
        if not self.connection:
            self.connection = "Database"
        return self.connection

    def disconnect(self):
        self.connection = None


if __name__ == '__main__':
    db1 = DatabaseSingleton()
    db2 = DatabaseSingleton()
    print(db1 is db2)
    print(db1.connect())
    print(db1.disconnect())
    print(db2.connect())
    print(db2.disconnect())