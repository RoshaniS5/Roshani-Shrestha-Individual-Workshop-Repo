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

# Predictions: 
# It should be the same as previous app.py files, but with a couple print statements that print when 
# the localhost site (127.0.0.1:5000/ is accessed). It first prints the string "about to print __name__..." and then prints "__main__"
# when app is run via python.exe or "app" when run via "flask run."

# Results: 
# It worked as predicted.