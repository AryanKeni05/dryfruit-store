from flask import Blueprint, request, jsonify
from database import get_db_connection

orders_bp = Blueprint('orders', __name__)

@orders_bp.route('/orders', methods=['POST'])
def create_order():
    data = request.json
    user_id = 1  # temporary
    address = data['address']
    items = data['items']

    conn = get_db_connection()
    cursor = conn.cursor()

    # calculate total
    total = sum(item['price'] for item in items)

    # insert order
    cursor.execute(
        "INSERT INTO orders (user_id, total, address, status) VALUES (%s, %s, %s, %s)",
        (user_id, total, address, "Placed")
    )
    order_id = cursor.lastrowid

    # insert items
    for item in items:
        cursor.execute(
            "INSERT INTO order_items (order_id, product_id, quantity) VALUES (%s, %s, %s)",
            (order_id, item['id'], 1)
        )

    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": "Order placed successfully"})