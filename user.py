import hashlib
import uuid

class User:
    """
    Базовый класс, представляющий пользователя.
    """
    users = {}  #  хранения всех пользователей

    def __init__(self, username, email, password):
        if User.is_username_unique(username):
            self.__username = username
            self.__email = email
            self.__password = User.hash_password(password)
            User.users.update({self.__username : self})
            return True
        else: print('Объект не создан, такой пользователь уже есть')
        
    @property
    def username(self):
        return self.__username    

    @staticmethod
    def is_username_unique(username):
        return username not in User.users


    @staticmethod
    def hash_password(password):
        md5_hash = hashlib.new('md5')
        md5_hash.update(password.encode('utf-8'))
        return md5_hash.hexdigest()

    
    def check_password(self,password):
        """
        Проверка пароля.
        """
        return self.__password == User.hash_password(password)

    def get_details(self):
        print(f'Имя пользователя  {self.__username}, Email {self.__email} ', end="")
    
    @classmethod
    def find_by_username(cls, username):
        return cls.users.get(username)  # Возвращает user_object или None

class Customer(User):
    """
    Класс, представляющий клиента, наследующий класс User.
    
    """
    customers = []
    
    def __init__(self, username, email, password, address):
       if super().__init__(username, email, password):
           self.__address = address
           Customer.customers.append(self)
 

    
    def get_details(self):
        super().get_details()
        print(f' address {self.__address} ')
        
        

class Admin(User):
    """
    Класс, представляющий администратора, наследующий класс User.
    """
    def __init__(self, username, email, password, admin_level):
        if super().__init__(username, email, password):
            self.__admin_level = admin_level
        

    def get_details(self):
        super().get_details()
        print(f' admin_level{self.__admin_level} ')

    @staticmethod
    def list_users():
        """
        Выводит список всех пользователей.
        """
        print('Количество пользователей:', len(Customer.customers))
        for i in range(len(Customer.customers)):
            Customer.customers[i].get_details()
            
    

    @staticmethod
    def delete_user():
        """
        Удаляет пользователя по имени пользователя.
        """
        print("введите имя пользователя для удаления")
        username = input() 
        index = next((i for i, p in enumerate(Customer.customers) if p.username == username), None)
        del Customer.customers[index]
        del User.users[username]
 