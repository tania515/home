from user import Customer, Admin
import hashlib
import uuid

# Создаем пользователей
customer1 = Customer(username="Mikhail", email="python@derkunov.ru", password='hhhh', address="033 Russ Bur" )
customer3 = Customer(username="Mikhail", email="python@derkunov.ru", password='hhhh', address="033 Russ Bur" )
customer2 = Customer(username="Mikle", email="python@derkunov.ru", password='ttt', address=" Russ Bur" )
admin1 = Admin(username="root", email="root@derkunov.ru", password='hhhh', admin_level=5)
admin2 = Admin(username="root1", email="root1@derkunov.ru", password='1hhhh', admin_level=5)

customer1.get_details()
customer2.get_details()
admin1.get_details()
admin2.get_details()

Admin.list_users()
Admin.delete_user()
Admin.list_users()
"""password = "ttt"
def hash_password(password):
        md5_hash = hashlib.new('md5')
        md5_hash.update(password.encode('utf-8'))
        return md5_hash.hexdigest(), password
    
print(hash_password(password))"""