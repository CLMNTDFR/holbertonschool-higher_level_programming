#!/usr/bin/python3

from flask import Flask, render_template, request
import json
import csv

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
    else:
        error = "Wrong source"

    if product_id:
        try:
            product_id = int(product_id)
            products = [product for product in products if
                        product['id'] == product_id]
            if not products:
                error = "Product not found"
        except ValueError:
            error = "Invalid product id"

    return render_template('product_display.html', products=products,
                           error=error)


if __name__ == '__main__':
    app.run(debug=True, port=5000)