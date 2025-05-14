import hashlib
import uuid

class User:
    """
    Базовый класс, представляющий пользователя.
    """
    users = []  # Список для хранения всех пользователей

    def __init__(self, username, email, password):
        self.__username = username
        self.__email = email
        self.__password = password

    @staticmethod
    def hash_password(password):
        pass

    @staticmethod
    def check_password(stored_password, provided_password):
        """
        Проверка пароля.
        """
        pass

    def get_details(self):
        print(f'Имя пользователя  {self.__username}, Email {self.__email} ', end="")

class Customer(User):
    """
    Класс, представляющий клиента, наследующий класс User.
    """
    def __init__(self, username, email, password, address):
        super().__init__(username, email, password)
        self.__address = address
        User.users.append(self.get_details)

    def get_details(self):
        super().get_details()
        print(f' address {self.__address} ')
        
        

class Admin(User):
    """
    Класс, представляющий администратора, наследующий класс User.
    """
    def __init__(self, username, email, password, admin_level):
        super().__init__(username, email, password)
        self.__admin_level = admin_level
        

    def get_details(self):
        super().get_details()
        print(f' admin_level{self.__admin_level} ')

    @staticmethod
    def list_users():
        """
        Выводит список всех пользователей.
        """
        print('Количество пользователей:', len(User.users))
        for i in range(len(User.users)):
            print(User.users[i])
            
    

    @staticmethod
    def delete_user(username):
        """
        Удаляет пользователя по имени пользователя.
        """
        pass
