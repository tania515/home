from user import Customer, Admin
from sessionManager import SessionManager
import hashlib
import uuid

# Создаем пользователей
customer1 = Customer(username="Mikhail", email="python@derkunov.ru", password='hhhh', address="033 Russ Bur" )
customer3 = Customer(username="Mikhail", email="python@derkunov.ru", password='hhhh', address="033 Russ Bur" )
customer2 = Customer(username="Mikle", email="python@derkunov.ru", password='ttt', address=" Russ Bur" )
admin1 = Admin(username="root", email="root@derkunov.ru", password='hhhh', admin_level=5)
admin2 = Admin(username="admin", email="root1@derkunov.ru", password='qwerty123', admin_level=5)

customer1.get_details()
customer2.get_details()
admin1.get_details()
admin2.get_details()

Admin.list_users()
Admin.delete_user()
Admin.list_users()


SessionManager.login("admin", "qwerty123")  
print('текущий пользователь ', SessionManager.get_current_user().username) 

SessionManager.login("Mikhail", "hhhh")  

SessionManager.login("ivan", "wrongpass")  

SessionManager.logout()  # Выход пользователя

SessionManager.login("Mikhail", "hhhh")  

SessionManager.logout()  # Выход пользователя

SessionManager.login("admin", "wrongpass")  
