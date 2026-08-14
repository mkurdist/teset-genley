# app.py - Incomplete and Vulnerable Project Example
from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# BUG: No OAuth2 Authentication implemented for any route!
# BUG: No Rate Limiting (vulnerable to DoS attacks)!

@app.route('/api/products', methods=['GET'])
def get_products():
    # BUG: No Input Sanitization - direct SQL Injection vulnerability!
    search_term = request.args.get('q', '')
    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM products WHERE name LIKE '%{search_term}%'"
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return jsonify(results)

@app.route('/api/admin/data', methods=['POST'])
def save_sensitive_data():
    # BUG: Plaintext storage - No AES-256 Encryption applied to sensitive data!
    data = request.json.get('secret_info')
    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO secrets (data) VALUES (?)", (data,))
    conn.commit()
    conn.close()
    return jsonify({"status": "saved without encryption"})

if __name__ == '__main__':
    app.run(debug=True)
