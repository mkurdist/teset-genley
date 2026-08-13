from flask import Flask, jsonify, request

app = Flask(__name__)

# این سرویس قرار است موجودی را مدیریت کند
balance = 100

@app.route('/checkout', methods=['POST'])
def checkout():
    data = request.json
    amount = data.get('amount', 0)
    
    # باگ منطقی: در اینجا بررسی نمی‌شود که آیا مقدار amount منفی است یا خیر
    # و باگ پنهان: اگر کاربر موجودی کافی نداشته باشد، تعادل منفی می‌شود که باید Disputed شود
    global balance
    balance -= amount
    
    return jsonify({"new_balance": balance, "status": "processed"})

if __name__ == '__main__':
    app.run()
