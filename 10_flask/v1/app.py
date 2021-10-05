# Clyde 'Thluffy' Sinclair
# SoftDev
# Oct 2021

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    return "No hablo queso!" 

app.run()

# Predictions: 
# It should produce the same results as v0 app.py, except it doesn't print anything into the terminal.

# Results: 
# It worked as expected. 
