import requests
import re

def checkLink(link):
    try:
        res = requests.get(link).status_code
        if(res==200):
            return True
        else:
            return False
    except:
        return False
    
def findlinks(data):
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex,data)      
    return [x[0] for x in url]

def checkDeadLinks(url):
    data = requests.get(url).text
    links = findlinks(data)
    linksCount = len(links)
    
    deadLinks = []
    for link in links:
        currentIndex = links.index(link)
        status = checkLink(link)
        if(status==False):
            deadLinks.append(link)
        
    return {"deadLinks":deadLinks, "links":links}

"""Flask App Project."""

from flask import Flask, jsonify, request
app = Flask(__name__)


@app.route('/')
def index():
    """Return homepage."""
    json_data = {'Page': 'Home'}
    return jsonify(json_data)

@app.route('/deadlink',methods = ['POST', "GET"])
def deadlink():
    json_data = {}
    if request.method == 'POST':
        url = request.form['url']
        
        res = checkDeadLinks(url)
        json_data = res
    
    return jsonify(json_data)


if __name__ == '__main__':
    app.run()        
