from flask import Flask, render_template, url_for, request
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('cars.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/order/<int:model_id>', methods=['GET', 'POST'])
def order_form(model_id):
    conn = get_db_connection()
    car = conn.execute('SELECT * FROM cars WHERE id = ?', (model_id,)).fetchone()
    conn.close()

    if car is None:
        return "Авто не знайдено", 404

    if request.method == 'POST':
        customer_name = request.form.get('customer_name', '').strip()
        if not customer_name:
            return render_template('order_form.html', model=car, error='Введіть ім\'я!')
        return render_template('order_success.html', model=car, name=customer_name)

    return render_template('order_form.html', model=car)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/models')
def models():
    conn = get_db_connection()
    cars = conn.execute('SELECT * FROM Cars').fetchall()
    conn.close()
    return render_template('models.html', cars=cars)

@app.route('/models/<int:model_id>')
def model_details(model_id):
    conn = get_db_connection()
    model = conn.execute('SELECT * FROM Cars WHERE id = ?', (model_id,)).fetchone()
    conn.close()
    if model is None:
        return "Модель не знайдена", 404
    return render_template('model_detail.html', model=model)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
