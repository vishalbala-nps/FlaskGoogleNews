from flask import Flask, render_template, request, send_file
from os import path
from time import sleep

import requests
import json

#Global Vars
API_KEY = "fa240576ba8e4d3f9435ec13a026c0ef"
#Functions
def get_news():
    linux = requests.get("https://newsapi.org/v2/everything?q=Linux&apiKey="+API_KEY+"&sortBy=publishedAt&sources=google-news")
    android = requests.get("https://newsapi.org/v2/everything?q=Android&apiKey="+API_KEY+"&sortBy=publishedAt&sources=google-news")
    os = requests.get("https://newsapi.org/v2/everything?q=Open-Source&apiKey="+API_KEY+"&sortBy=publishedAt&sources=google-news")

    linux_articles = json.loads(linux.text)['articles']
    android_articles = json.loads(android.text)['articles']
    os_articles = json.loads(os.text)['articles']

    return (linux_articles, android_articles, os_articles)

#Main Program starts here
app = Flask(__name__)

#Default Route
@app.route('/') 
def main():
    news = get_news()
    return render_template('index.html', linux=news[0], android=news[1], os=news[2])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)