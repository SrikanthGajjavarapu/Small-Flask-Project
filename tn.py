import pandas as pd
from flask import Flask,jsonify

app = Flask(__name__)

@app.route("/")
def home():
    data = pd.read_csv('EURJPY_M15_EMA10_RR5.csv')
    print(data.head())  # Print first few rows to terminal
    data_dict = data.to_dict(orient='records')
    return jsonify(data_dict)

if __name__ == "__main__":
    app.run()