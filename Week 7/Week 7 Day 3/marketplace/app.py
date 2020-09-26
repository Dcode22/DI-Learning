from flask import Flask, request, render_template, url_for, flash, redirect
import secrets
import psycopg2

app = Flask(__name__)
key = secrets.token_urlsafe(100)
app.secret_key = key

HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = '922933'
DATABASE = 'store'

@app.route("/", methods=['GET', 'POST'])
def add_product():
    if request.method == 'GET':

        # # read from pretend database
        # with open('db.txt', 'r') as f:
        # 	students = f.readlines()

        connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)
        cursor = connection.cursor()
        query = "SELECT * FROM products;"
        cursor.execute(query)
        products = cursor.fetchall();
        connection.close()

        if not products:
            flash("No products yet", "red")

        return render_template('add_products.html', products=products)

    if request.method == 'POST':
        name = request.form.get('name')
        price = request.form.get('price')
        category = request.form.get('category')
        stock = request.form.get('stock')

        # # write to pretend database
        # with open('db.txt', 'a') as f:
        # 	f.write(f"{first_name} {last_name}\n")

        connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)
        cursor = connection.cursor()
        query = f"INSERT INTO products (name, price, category, stock) VALUES ('{name}', '{price}', '{category}', '{stock}')"
        cursor.execute(query)
        connection.commit()

        flash(f"New product Added: {name} {price}", "green")
        return redirect(url_for('add_product'))

if __name__ == "__main__":
	app.run(debug= True)