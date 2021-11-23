# Crashing Waves: Jonathan Wu (Loki), Roshani Shrestha (Pete)
# SoftDev pd0
# K19: A RESTful Journey Skyward
# 2021-11-24t
# time spent:  hours

from flask import Flask, render_template
import json
import urllib.request

app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def api():
    f = open("key_nasa.txt", "r")
    api_key = f.read()
    print("***DIAG: api_key ***") 
    print(api_key)

    url = "https://api.nasa.gov/planetary/apod?api_key=" + api_key
    data = urllib.request.urlopen(url)

    print("***DIAG: data.geturl() ***") 
    print(data.geturl())
    print("***DIAG: data.read() ***") 
    print(data.read())

    d = data.read().loads() 
    return render_template("main.html", pic=d['url'])

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()