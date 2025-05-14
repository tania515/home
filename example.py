from user import Customer, Admin


# Создаем пользователей
customer = Customer(username="Mikhail", email="python@derkunov.ru", password='hhhh', address="033 Russ Bur" )
admin = Admin(username="root", email="root@derkunov.ru", password='hhhh', admin_level=5)

customer.get_details()
admin.get_details()
