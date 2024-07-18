#!/usr/bin/python3

from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)


def read_json_file(filename):
    with open(filename) as f:
        return json.load(f)


def read_csv_file(filename):
    products = []
    with open(filename) as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
    return products


def read_sqlite_db():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, name, category, price FROM Products')
    products = [
        {"id": row[0], "name": row[1], "category": row[2], "price": row[3]}
        for row in cursor.fetchall()
    ]
    conn.close()
    return products


@app.route('/products')
def display_products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    products = []
    error = None

    if source == 'json':
        products = read_json_file('products.json')
    elif source == 'csv':
        products = read_csv_file('products.csv')
    elif source == 'sql':
        products = read_sqlite_db()
    else:
        error = "Wrong source"

    if product_id:
        try:
            product_id = int(product_id)
            products = [product for product in products if product['id'] ==
                        product_id]
            if not products:
                error = "Product not found"
        except ValueError:
            error = "Invalid product id"

    return render_template('product_display.html', products=products,
                           error=error)


if __name__ == '__main__':
    app.run(debug=True, port=5000)