from flask import Flask, render_template, jsonify
import pandas as pd
import simplejson
from flask_cors import CORS

app = Flask(__name__, static_folder='build', static_url_path='/')
CORS(app)

@app.route("/")
def index():
    
    # print(df.groupby('Country').get_group('Austria'))
    
        # countries.get_group(country)
    # print(countryCollector)

    return app.send_static_file('index.html')


@app.route("/country", methods = ['POST', 'GET'])
def country():
    df = pd.read_csv('LifeExpectancyData.csv')
    countryCollector=[]
    countries=df.groupby('Country')
    for country in countries.groups.keys():
        new_dict=countries.get_group(country)[['Year','Life expectancy ']].to_dict('records')
        countryCollector.append({
            'id':country,
            'data':list(map(lambda x: {'y':x['Life expectancy '],'x':x['Year']},new_dict))})
    print('Nan' in simplejson.dumps(countryCollector, ignore_nan=True))
    return simplejson.dumps(countryCollector[-5:], ignore_nan=True)


@app.route("/countryBar", methods = ['POST', 'GET'])
def countryBar():
    df = pd.read_csv('LifeExpectancyData.csv')
    countryCollector=[]
    countries=df[df['Year']==2014]
    countries=countries[['infant deaths','Life expectancy ', 'Country']].to_dict('records')
    countries=simplejson.dumps({'data':countries[-2:], 'keys':['infant deaths','Life expectancy '], 'indexBy':'Country'}, ignore_nan=True)
    print(countries)
    return countries