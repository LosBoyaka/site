import sqlite3

try:
    conn = sqlite3.connect('../cars.db')
    print("Підключення успішне!")
    conn.close()
except Exception as e:
    print("Помилка підключення:", e)


db = SQLAgent('cars.db')
db.create_tables()
db.seed_cars()

cars = db.get_all_cars()
for car in cars:
    print(car['model'], car['price'], car['description'], car['image'])

db.add_order("Іван Іванов", 2)

orders = db.get_orders()
for order in orders:
    print(order['id'], order['customer_name'], order['model'], order['price'])

db.close()