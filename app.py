from flask import Flask, render_template, request, send_file
from os import path
from time import sleep

import requests
import json
import wget


#Main Program starts here

app = Flask(__name__)

#Default Route
@app.route('/') 
def main():
    title = ['a','b','c']
    author = ['d','e','f']
    link = ['g','h','i']
    return render_template('index.html', title=title, author=author, link=link)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)