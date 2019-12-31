from flask import Flask, render_template, request, send_file
from os import path
from time import sleep

import requests
import json
import wget

#Global Vars

#Functions
def get_news():
    linux_alist = []
    android_alist = []
    os_alist = []

    linux_tlist = []
    android_tlist = []
    os_tlist = []

    linux_linlist = []
    android_linlist = []
    os_linlist = []

    linux = requests.get("https://newsapi.org/v2/everything?q=Linux&apiKey=fa240576ba8e4d3f9435ec13a026c0ef&sortBy=publishedAt&sources=google-news")
    android = requests.get("https://newsapi.org/v2/everything?q=Android&apiKey=fa240576ba8e4d3f9435ec13a026c0ef&sortBy=publishedAt&sources=google-news")
    os = requests.get("https://newsapi.org/v2/everything?q=Open-Source&apiKey=fa240576ba8e4d3f9435ec13a026c0ef&sortBy=publishedAt&sources=google-news")

    linux_articles = json.loads(linux.text)['articles']
    android_articles = json.loads(android.text)['articles']
    os_articles = json.loads(os.text)['articles']

    for i in linux_articles:
        linux_alist.append(i['author'])
        linux_tlist.append(i['title'])
        linux_linlist.append(i['url'])

    for i in android_articles:
        android_alist.append(i['author'])
        android_tlist.append(i['title'])
        android_linlist.append(i['url'])
    
    for i in os_articles:
        os_alist.append(i['author'])
        os_tlist.append(i['title'])
        os_linlist.append(i['url'])

    return (linux_alist, linux_tlist, linux_linlist, android_alist, android_tlist, android_linlist, os_alist, os_tlist, os_linlist)

#Main Program starts here
app = Flask(__name__)

#Default Route
@app.route('/') 
def main():
    news = get_news()
    return render_template('abc.html', titlelinux=news[1], authorlinux=news[0], linklinux=news[2], titleos=news[7], authoros=news[6], linkos=news[8], titleandroid=news[4], authorandroid=news[3], linkandroid=news[5])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)