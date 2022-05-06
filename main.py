from distutils.log import debug
from flask import Flask, render_template, request
from helper_functions import retrieve_Market_data
from flask_sqlalchemy import SQLAlchemy

app = Flask("__main__")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
db = SQLAlchemy(app)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        body = request.get_json()
        tickers = body['tickers']
        start_date = body['start_date']
        # risk_factor = request.form["risk"]
        tail = start_date[4 : len(start_date)]
        end_date = int(start_date[0:4]) + 2
        end_date_str = str(end_date) + tail
        market_data = retrieve_Market_data(tickers[0], "1", start_date, end_date_str)
        print(market_data)
        return market_data
    return render_template("index.html")


app.run(debug=True)
