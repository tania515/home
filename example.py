from user import Customer, Admin


# Создаем пользователей
customer1 = Customer(username="Mikhail", email="python@derkunov.ru", password='hhhh', address="033 Russ Bur" )
customer2 = Customer(username="Mikle", email="python@derkunov.ru", password='ttt', address=" Russ Bur" )
admin = Admin(username="root", email="root@derkunov.ru", password='hhhh', admin_level=5)

customer1.get_details()
customer2.get_details()
admin.get_details()

admin.list_users()