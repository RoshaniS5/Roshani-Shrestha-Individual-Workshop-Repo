# The Red Imposter - Daniel Sooknanan, Shadman Rakib, and Roshani Shrestha
# SoftDev
# K10: Putting Little Pieces Together - Details our predictions and results in the form of comments for this file
# 2021-10-05

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    print("the __name__ of this module is... ")
    print(__name__)
    return "No hablo queso!"

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()

# Predictions: 
# It should have the same behavior as v3 app.py as long as it is confirmed that this
# file is the file being run with python.exe and not via "flask run." If the file is run 
# using the former method it will be in debug mode. If it's run via "flask run" it won't be, 
# but it also won't show the warning that goes along the lines of "silently ignoring app.run()..."

# Results: 
# It is the same as predicted.  