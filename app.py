from flask import Flask, request, jsonify
import yfinance as yf
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allows frontend to communicate with backend

# Investment Strategy API
@app.route('/investment_strategy', methods=['POST'])
def investment_strategy():
    data = request.json
    risk_tolerance = data.get('risk_tolerance', 'medium')

    # Simple portfolio allocation
    strategy = {
        "stocks": 70 if risk_tolerance == "high" else 50,
        "bonds": 20 if risk_tolerance == "high" else 40,
        "crypto": 10 if risk_tolerance == "high" else 5
    }
    return jsonify(strategy)

# Stock Data API
@app.route('/stock_data', methods=['GET'])
def stock_data():
    stock = request.args.get('symbol', 'AAPL')
    data = yf.Ticker(stock).history(period="1mo")
    return jsonify(data.to_dict())

# Run the Flask App
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000)

