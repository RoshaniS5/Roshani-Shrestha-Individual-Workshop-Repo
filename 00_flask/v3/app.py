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

# Predictions: It should be the same as the prior file. 
# Results: A debugger is present. There is a debugger PIN. When the file is changed, the debugger detects the change and prints it into the terminal. Then it reloads. The message that is displayed is "Detected change in '/Users/roshanishrestha/Roshani-Shrestha-Individual-Workshop-Repo/00_flask/v3/app.py', reloading". 
# Then, you can refresh the page to see the changes on the page.
