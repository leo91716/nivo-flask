from flask import Flask, render_template
import pandas as pd
app = Flask(__name__)
@app.route("/")
def hello():
    df = pd.read_csv('LifeExpectancyData.csv')
    print(df.columns)
    return render_template('index.html')