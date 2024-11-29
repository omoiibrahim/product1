from flask import Flask, jsonify, request, make_response

app = Flask(__name__)

products = []

@app.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()
    if not all(key in data for key in ("name", "description", "price")):
        return make_response(jsonify({"error": "Invalid input"}), 400)
    product = {
        "id": len(products) + 1,
        "name": data['name'],
        "description": data['description'],
        "price": data['price']
    }
    products.append(product)
    return make_response(jsonify(product), 201)

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)

if __name__ == '__main__':
    app.run(debug=True)
