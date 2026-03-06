# test pipeline

from flask import Flask, jsonify, request

app = Flask(__name__)

cart_items = [
    {"id": 1, "product": "Laptop", "quantity": 1},
    {"id": 2, "product": "Mouse", "quantity": 2}
]

@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "ok",
        "service": "cart-service"
    }), 200

@app.route("/cart", methods=["GET"])
def get_cart():
    return jsonify(cart_items), 200

@app.route("/cart", methods=["POST"])
def add_to_cart():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Request body is required"}), 400

    product = data.get("product")
    quantity = data.get("quantity")

    if not product or quantity is None:
        return jsonify({"error": "product and quantity are required"}), 400

    new_item = {
        "id": len(cart_items) + 1,
        "product": product,
        "quantity": quantity
    }

    cart_items.append(new_item)
    return jsonify(new_item), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
# trigger workflow again
