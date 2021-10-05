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
   
app.debug = True
app.run()

# Predictions: 
# It should be the same as the prior file (v2 app.py). 

# Results: 
# It is like v2 app.py in the sense that the two print statements act the same, 
# but there are differences. First of all, a Debugger is active and there is a Debugger PIN. 
# Second of all, when the file is changed, the change is detected and the localhost site 
# is updated (but you have to refresh to see this change). 
# Something of note is that when using flask run, debug mode isn't active despite setting the value to True.
