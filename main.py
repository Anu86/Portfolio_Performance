from distutils.log import debug
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from agent import run
import glob
import os

app = Flask("__main__")


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        body = request.get_json()
        tickers = body["tickers"]
        # start_date = body["start_date"]
        # # risk_factor = request.form["risk"]
        # tail = start_date[4 : len(start_date)]
        # end_date = int(start_date[0:4]) + 2
        # end_date_str = str(end_date) + tail
        market_data = run(tickers=tickers, budget=1000000)
        list_of_files = glob.glob(
            "/resources"
        )  # * means all if need specific format then *.csv
        latest_file = max(list_of_files, key=os.path.getctime)
        print(latest_file)
        # print(market_data)
        # return market_data

    return render_template("index.html")


app.run(debug=True)
