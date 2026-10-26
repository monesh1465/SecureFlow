from flask import Blueprint, jsonify

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return jsonify({
        "application": "SecureFlow",
        "message": "Automated DevSecOps Security Pipeline",
        "status": "running"
    }), 200

@main.route('/health')
def health():
    return jsonify({"status": "healthy"}), 200
