# Clyde 'Thluffy' Sinclair
# SoftDev
# Oct 2021

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    return "No hablo queso!" 

app.run()

# Predictions: It should be the same as app.py from K09, except `__main__` doesn't print in terminal
# After: 
