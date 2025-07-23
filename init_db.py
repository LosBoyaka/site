import sqlite3

conn = sqlite3.connect('cars.db')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Cars')

cur.execute('''
    CREATE TABLE Cars (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        details TEXT NOT NULL,
        image TEXT NOT NULL,
        year INTEGER,
        engine TEXT,
        power TEXT,
        acceleration TEXT,
        transmission TEXT,
        drive TEXT,
        price TEXT
    )
''')

cars = [
    (
        "Mercedes-AMG E63s W213",
        "Потужний седан з агресивним стилем, комфортом бізнес-класу та динамікою спорткара.",
        "e63s_w213.png",
        2021,
        "4.0L V8 Biturbo",
        "612 к.с.",
        "3.4 с",
        "9-ступенева автоматична",
        "Повний привід 4MATIC+",
        "6 500 000 ₴"
    ),
    (
        "Mercedes-Benz S-Class W223",
        "Флагман розкоші з преміальним інтер’єром, інтелектуальними системами та гібридним двигуном.",
        "s_class_w223.png",
        2023,
        "3.0L I6 Mild Hybrid",
        "435 к.с.",
        "4.9 с",
        "9G-TRONIC",
        "Повний привід 4MATIC",
        "7 800 000 ₴"
    ),
    (
        "Mercedes-Benz G-Class G63 AMG",
        "Ікона позашляховиків з надпотужним двигуном, розкішним салоном і брутальним виглядом.",
        "g_class_g63.png",
        2022,
        "4.0L V8 Biturbo",
        "585 к.с.",
        "4.5 с",
        "9-ступенева автоматична",
        "Повний привід",
        "9 200 000 ₴"
    ),
    (
        "Mercedes-Benz A-Class W177",
        "Компактний та стильний хетчбек з високим рівнем технологій та економічністю.",
        "a_class_w177.png",
        2022,
        "1.3L I4 Turbo",
        "163 к.с.",
        "8.0 с",
        "7G-DCT",
        "Передній привід",
        "1 200 000 ₴"
    ),
    (
        "Mercedes-Benz CLA Shooting Brake",
        "Спортивний універсал з елегантним дизайном, динамікою та практичністю.",
        "cla_shooting.png",
        2022,
        "2.0L I4 Turbo",
        "224 к.с.",
        "6.8 с",
        "7G-DCT",
        "Повний привід 4MATIC",
        "1 800 000 ₴"
    ),
    (
        "Mercedes-Benz EQS",
        "Електричний флагман з футуристичним дизайном, безшумною їздою і запасом ходу до 770 км.",
        "eqs.png",
        2023,
        "Електродвигун",
        "523 к.с.",
        "4.3 с",
        "Одноступенева автоматична",
        "Повний привід",
        "5 400 000 ₴"
    )
]

cur.executemany('''
INSERT INTO Cars (name, details, image, year, engine, power, acceleration, transmission, drive, price)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
''', cars)

conn.commit()
conn.close()