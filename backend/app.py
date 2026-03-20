from flask import Flask
from flask_cors import CORS
from routes.products import products_bp   # ✅ IMPORTANT
from routes.orders import orders_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(products_bp)       # ✅ IMPORTANT


@app.route('/')
def home():
    return {"message": "Dry Fruit Store API Running 🚀"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)