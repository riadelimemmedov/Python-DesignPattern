from abc import ABC, abstractmethod

""" 
    The Template Design Pattern is a behavioral design pattern that defines the skeleton of an algorithm in a base class and allows subclasses to override specific steps of the algorithm without changing its structure.
"""


# *DataStorage
class DataStorage(ABC):
    @abstractmethod
    def setup(self):
        pass

    def check_data(self, data):
        print(f"DataStorage : checking data {data}")

    @abstractmethod
    def write_data(self, data):
        pass

    @abstractmethod
    def commit(self):
        pass

    @abstractmethod
    def log(self):
        pass

    def template(self, data):
        self.setup()
        self.check_data(data)
        self.write_data(data)
        self.commit()
        self.log()


#!DatabaseDataStorage
class DatabaseDataStorage(DataStorage):
    def setup(self):
        print("Database connection established")

    def write_data(self, data):
        print(f"Database : writing data {data}")

    def commit(self):
        print("Database : data committed successfully")

    def log(self):
        print("Database : writing completed")


#!FileSystemDataStorage
class FileSystemDataStorage(DataStorage):
    def setup(self):
        print("FileSystem connection established")

    def write_data(self, data):
        print(f"FileSystem : writing data {data}")

    def commit(self):
        print("FileSystem : data committed successfully")

    def log(self):
        print("FileSystem : writing completed")


if __name__ == "__main__":
    databases = DatabaseDataStorage()
    databases.template("All BlockChain Transaction Data")

    print()

    filesystem = FileSystemDataStorage()
    filesystem.template("All Python File")
