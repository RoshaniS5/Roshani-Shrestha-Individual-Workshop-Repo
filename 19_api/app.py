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
def hello_world():
    url = "https://api.nasa.gov/planetary/apod?api_key=xuaebIrYBsJiXZtewQGeUCuPn3sJaCcSFDyBZrjX"
    data = urllib.request.urlopen(url)
    print("***DIAG: data.geturl() ***") 
    print(data.geturl())
    print(__name__)
    return "No hablo queso!"

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()