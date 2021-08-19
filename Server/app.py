import os
import requests
from bs4 import BeautifulSoup
from flask import Flask, request, redirect

app = Flask(__name__)

remoute_server = os.getenv("TEXT-BROWSER-CLIENT-SERVICE_SERVICE_HOST")

def parsing(res):
    soup = BeautifulSoup(res.text, 'html.parser')
    head = soup.find("h1").text
    par = soup.find_all("p")
    par_new = ""
    for item in par:
        par_new = par_new + item.text
    return head, par_new

@app.route('/', methods=['POST', 'GET'])
def get_data():
    URL = request.args['URL']
    error = ''
    head = ''
    par_new = ''
    try:
        r = requests.get(URL)
        head, par_new = parsing(r)
    except requests.exceptions.MissingSchema:
        r = requests.get('https://' + URL)
        head, par_new = parsing(r)
    except requests.exceptions.ConnectionError:
        error = "Error: Host unreachable"
    return redirect(remoute_server+":5000/result?head={}&par={}&error={}".format(head, par_new, error))

if __name__ == '__main__':
    app.run(hohost="0.0.0.0")