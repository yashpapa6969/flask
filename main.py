from flask import Flask,jsonify
import os


@app.route('/')
def index():
    return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})
    return jsonify({'predictions': predictions1.tolist()})
if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
