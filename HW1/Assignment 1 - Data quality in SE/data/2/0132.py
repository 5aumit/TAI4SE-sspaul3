from flask import Flask, render_template,json,jsonify,request,current_app as app
from datetime import date
import requests
import os

app = Flask(__name__)

@app.route('/')
def index():
    name = 'Abdul Q'
    friends =['joe','bob','robert','bobby']
   
    return render_template('index.html',greeting = name,friends =friends)
@app.route('/about')
def about():
    return '<h1>about</h1><p>some other content</p>'





@app.route('/nasa')
def show_nasa_pic():#go to nasa endpoint run code below
    today = str(date.today())
    response = requests.get('https://api.nasa.gov/planetary/apod?api_key=wjlnR0Xw9B5Sh3WEIJa9kmVd368hNMiUVIGahGPi&date='+today)
    data = response.json()
    return render_template('nasa.html',data=data)

"""@app.route('/album', methods=['GET'])
def album_json():   
    album_info = os.path.join(app.static_folder, 'data','album.json')
    with open(album_info, 'r') as json_data:
        json_info = json.load(json_data)
        return jsonify(json_info)"""

@app.route('/movies', methods=['GET'])
def movies_json():
    movies_info = os.path.join(app.static_folder,'data','movies.json')
    with open(movies_info, 'r') as json_data:
        json_info = json.load(json_data)
        return jsonify(json_info)

@app.route('/movies/search_title',methods=['GET'])#parameters 
def movies_search_title():
    movies_info = os.path.join(app.static_folder,'data','movies.json')
    with open(movies_info, 'r') as json_data:
        json_info = json.load(json_data)
    results = []
    if 'title' in request.args:
        #stores the results of the title the user put into the url
        title=request.args['title']
        # goes through the moves.json files and searchs for the movie
        for movie in json_info:# if it equals the movies title then it appends the information off the title
            if title in movie['title']:   
                results.append(movie)
    if len(results) < 1:
        return "no results found"
    return render_template("movies.html",results=results)



    

if __name__ == '__main__':
    app.run(debug=True, host='192.168.1.213')
