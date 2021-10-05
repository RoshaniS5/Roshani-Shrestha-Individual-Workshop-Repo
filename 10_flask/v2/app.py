# Clyde 'Thluffy' Sinclair
# SoftDev
# Oct 2021

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    print("about to print __name__...")
    print(__name__)   #where will this go?
    return "No hablo queso!"

app.run()

# Predictions: first prints the string "about to print __name__..." and then prints `__main__`. Then, "No hablo queso!" prints onto the webpage after opening the link.
# It worked as predicted.