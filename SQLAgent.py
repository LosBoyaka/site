import sqlite3

class SQLAgent:
    def __init__(self, db_path):
        self.db_path = db_path
        self.connection = sqlite3.connect(self.db_path, check_same_thread=False)
        self.connection.row_factory = sqlite3.Row
        self.cursor = self.connection.cursor()

    def create_tables(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Cars (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                model TEXT NOT NULL,
                price INTEGER NOT NULL,
                description TEXT,
                image TEXT
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Orders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                customer_name TEXT NOT NULL,
                car_id INTEGER,
                FOREIGN KEY(car_id) REFERENCES Cars(id)
            )
        """)
        self.connection.commit()

    def seed_cars(self):
        self.cursor.execute("SELECT COUNT(*) FROM Cars")
        if self.cursor.fetchone()[0] == 0:
            cars = [
                (
                    "Mercedes-Benz S 580 W223",
                    5200000,
                    "Розкішний седан бізнес-класу з інноваційними технологіями та максимальним комфортом.",
                    "/static/images/s_580_w223.jpg"
                ),
                (
                    "Mercedes-Benz GLE 450 W167",
                    3600000,
                    "Стильний і потужний кросовер з сучасними системами безпеки.",
                    "/static/images/gle_450_w167.jpg"
                ),
                (
                    "Mercedes-Benz A 200 W177",
                    1600000,
                    "Компактний і економічний автомобіль для міських поїздок.",
                    "/static/images/a_200_w177.jpg"
                ),
                (
                    "Mercedes-Benz E 63s W213",
                    4500000,
                    "Динамічний седан з преміальним інтер'єром і спортивною потужністю.",
                    "/static/images/e_63s_w213.jpg"
                ),
                (
                    "Mercedes-Benz G 63 W463",
                    6700000,
                    "Легендарний позашляховик із високою прохідністю та статусом.",
                    "/static/images/g_63_w463.jpg"
                ),
                (
                    "Mercedes-Benz CLA 250 C118",
                    2100000,
                    "Спортивний купеобразний седан із сучасним дизайном та технологіями.",
                    "/static/images/cla_250_c118.jpg"
                )
            ]
            self.cursor.executemany(
                "INSERT INTO Cars (model, price, description, image) VALUES (?, ?, ?, ?)",
                cars
            )
            self.connection.commit()

    def get_all_cars(self):
        self.cursor.execute("SELECT * FROM Cars")
        return self.cursor.fetchall()

    def add_order(self, customer_name, car_id):
        self.cursor.execute(
            "INSERT INTO Orders (customer_name, car_id) VALUES (?, ?)",
            (customer_name, car_id)
        )
        self.connection.commit()

    def get_orders(self):
        self.cursor.execute("""
            SELECT Orders.id, customer_name, model, price
            FROM Orders
            JOIN Cars ON Orders.car_id = Cars.id
        """)
        return self.cursor.fetchall()

    def close(self):
        self.connection.close()


if __name__ == "__main__":
    db = SQLAgent('cars.db')
    db.create_tables()
    db.seed_cars()

    print("Автомобілі у базі:")
    cars = db.get_all_cars()
    for car in cars:
        print(f"{car['id']}: {car['model']} — {car['price']} грн")
        print(f"Опис: {car['description']}")
        print(f"Зображення: {car['image']}\n")

    db.add_order("Іван Іванов", 1)

    print("Замовлення:")
    orders = db.get_orders()
    for order in orders:
        print(f"Замовлення #{order['id']} — Клієнт: {order['customer_name']}, Авто: {order['model']} ({order['price']} грн)")

    db.close()