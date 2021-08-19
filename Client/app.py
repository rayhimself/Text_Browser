import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST', 'GET'])
def rsult():
    head = request.args['head']
    par = request.args['par']
    error = request.args['error']
    return render_template('result.html', head=head, par=par, error=error)

if __name__ == '__main__':
    app.run(host="0.0.0.0")