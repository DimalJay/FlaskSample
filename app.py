from flask import Flask, request
import requests
import urllib
from twilio.twiml.messaging_response import MessagingResponse
import pytube
import re

app = Flask(__name__)


@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '')
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    if urllib.parse.urlparse(incoming_msg).netloc in ['www.youtube.com','youtu.be', 'youtube.com']:
        # Youtube
        print(incoming_msg)
        yt = pytube.YouTube(incoming_msg)
        video= yt.streams[0]
        msg.body(video.url)
        
        responded = True
        print("Sent")
        
    elif urllib.parse.urlparse(incoming_msg).netloc in ['www.facebook.com','fb.com', 'fb.watch', 'facebook.com']:
        # Facebook
        print(incoming_msg)
        html = requests.get(incoming_msg, stream=True)
        try:
            sdvideo_url = re.search('hd_src:"(.+?)"', html.text)[1]
            msg.body(sdvideo_url)
            
        except:
            sdvideo_url = re.search('sd_src:"(.+?)"', html.text)[1]
            msg.body(sdvideo_url)
            
        responded = True

    return str(resp)    


if __name__ == '__main__':
    app.run()
