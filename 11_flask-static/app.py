# Clyde 'Thluffy' Sinclair
# SoftDev
# Oct 2021 

# DEMO 
# basics of /static folder

from flask import Flask
from flask import send_file
app = Flask(__name__) 

@app.route("/")       
def hello_world():
    print("the __name__ of this module is... ")
    print(__name__)
    # return "No hablo queso!"
    return send_file('static/fixie.html')

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()
