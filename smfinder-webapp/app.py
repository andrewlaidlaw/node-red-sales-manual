from flask import Flask, request
from urllib.request import urlopen
from bs4 import BeautifulSoup
import json
# import sys

app = Flask(__name__)

@app.route('/')
def index():
    if request.args.get('mtm'):
        mtm = request.args.get('mtm')
        Search_url = "https://www-01.ibm.com/common/ssi/FetchJSON.wss?ctype=DD%3ADDSM&ctry=EUR%3AGB&lang=&MPPEFFTR=DOCNO&MPPEFSCH="
        Search_url += mtm
        Search_url += "&MPPEFFDR=&MPPEFTDR=&MPPEFSRT=2&hitsperpage=20&resultpage=1"

        html = urlopen(Search_url)
        soup = BeautifulSoup(html, 'html.parser')
        # soup.content
        json_string = soup.text
        parsed_json = json.loads(json_string)
        results = parsed_json['totalhitscount']

        if results == 0:
            response = "Missing"
        else:
            response = "https://www-01.ibm.com"
            response += parsed_json['hitList'][0]['url']

    else:
        response = "Missing"
    return response

@app.route('/healthz')
def healthz():
    return "ok"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)