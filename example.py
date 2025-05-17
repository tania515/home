from user import Customer, Admin
from sessionManager import AuthenticationService
import hashlib


# Создаем пользователей
try:
    customer1 = Customer(username="Mikhail", email="python@derkunov.ru", password='hhhh', address="033 Russ Bur" )
except ValueError as e:
    print(e)
try:
    customer3 = Customer(username="Mikhail", email="python@derkunov.ru", password='hhhh', address="033 Russ Bur" )
except ValueError as e:
    print(e)    
try:
    customer2 = Customer(username="Mikle", email="python@derkunov.ru", password='ttt', address=" Russ Bur" )
except ValueError as e:
    print(e)   
try:
    admin1 = Admin(username="root", email="root@derkunov.ru", password='hhhh', admin_level=5)
except ValueError as e:
    print(e)    
try:
    admin2 = Admin(username="admin", email="root1@derkunov.ru", password='qwerty123', admin_level=5)
except ValueError as e:
    print(e)     

 
customer1.get_details()
customer2.get_details()
admin1.get_details()
admin2.get_details()

Admin.list_users()
Admin.delete_user()
Admin.list_users()


AuthenticationService.login("admin", "qwerty123")  
#print('текущий пользователь ', AuthenticationService.get_current_user().username) 

AuthenticationService.login("Mikhail", "hhhh")  

AuthenticationService.login("ivan", "wrongpass")  

AuthenticationService.login("Mikhail", "hhhh")  

AuthenticationService.logout("Mikhail")  # Выход пользователя

AuthenticationService.login("Mikhail", "hhhh")  

AuthenticationService.logout("admin")  # Выход пользователя

AuthenticationService.login("admin", "wrongpass")  

AuthenticationService.register("Mikki","python@derkunov.ru",'xxxhhh')

AuthenticationService.login("Mikki", "xxxhhh") 

AuthenticationService.get_current_user()

AuthenticationService.logout("Mikhail") 

AuthenticationService.logout("Mikki") 
