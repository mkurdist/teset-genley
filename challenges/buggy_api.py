from flask import Flask, jsonify, request

app = Flask(__name__)

# Service manages user account balance
balance = 100

@app.route('/checkout', methods=['POST'])
def checkout():
    """
    Challenge: Logical Vulnerability
    - Business Logic Flaw: Does not validate if 'amount' is positive.
    - Security Flaw: Allows balance to drop below zero, leading to negative assets.
    """
    data = request.json
    amount = data.get('amount', 0)
    
    global balance
    # Logic Error: Insufficient funds check is missing.
    balance -= amount
    
    return jsonify({"new_balance": balance, "status": "processed"})

if __name__ == '__main__':
    app.run()
