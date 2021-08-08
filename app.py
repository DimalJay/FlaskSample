
"""Flask App Project."""

from flask import Flask, jsonify, request
app = Flask(__name__)
import requests

    
def findlinks(data):
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex,data)      
    return [x[0] for x in url]

@app.route('/')
def index():
    """Return homepage."""
    data = requests.get("https://ilabacademy.blogspot.com/").text
    return data

@app.route('/deadlink',methods = ['POST', "GET"])
def deadlink():
    json_data = {}
    if request.method == 'POST':
        url = request.form['url']
        
    
    return jsonify(json_data)


if __name__ == '__main__':
    app.run()        
