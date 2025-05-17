from user import User
import uuid
class AuthenticationService:
   # _current_user = None  # Текущий авторизованный пользователь
    token ={}
    
    @classmethod
    def login(cls, username, password):
        """Аутентификация пользователя"""
        if cls.token.get(username)  is not None:
            print("Ошибка: уже выполнен вход пользователем", username)
            return False
        user = User.find_by_username(username)
               
        """and user.check_password(password)"""
        
        if user and user.check_password(password):
            cls._current_user = user
            print(f"Успешный вход: {username}")
            session_token = str(uuid.uuid4())
            cls.token.update({username : session_token})
            return True
        print("Ошибка: неверный логин или пароль")
        return False
    
    @classmethod
    def logout(cls, username):
        """Завершение сеанса"""
        if cls.token.get(username)  is not None:
            print(f"Выход пользователя: {username}")
            del cls.token[username]
            
        else:
            print("Нет такого активного пользователя")
    
    @classmethod
    def get_current_user(cls):
        pass
        """Получение текущего пользователя"""
        """if cls._current_user:
            return cls._current_user
        else: return "нет активных пользователей"""

    @classmethod
    def register(cls,username, email, password):
        User(username, email, password)

    