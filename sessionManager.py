from user import Customer, Admin, User
class SessionManager:
    _current_user = None  # Текущий авторизованный пользователь
    
    @classmethod
    def login(cls, username, password):
        """Аутентификация пользователя"""
        if cls._current_user is not None:
            print("Ошибка: уже выполнен вход пользователем", cls._current_user.username)
            return False
        user = User.find_by_username(username)
               
        """and user.check_password(password)"""
        
        if user and user.check_password(password):
            cls._current_user = user
            print(f"Успешный вход: {username}")
            return True
        print("Ошибка: неверный логин или пароль")
        return False
    
    @classmethod
    def logout(cls):
        """Завершение сеанса"""
        if cls._current_user:
            print(f"Выход пользователя: {cls._current_user.username}")
            cls._current_user = None
        else:
            print("Нет активного пользователя")
    
    @classmethod
    def get_current_user(cls):
        """Получение текущего пользователя"""
        if cls._current_user:
            return cls._current_user
        else: return "нет активных пользователей"
