# Selective Soup | Justin Zou (Piggy), Wen Hao Dong (Jal Hordan), Roshani Shrestha (Pete)
# SoftDev 
# K15: Sessions Greetings - Uses session capabilities to allow a user to login and logout 
# 2021-10-18

from sys import argv
from flask import Flask, render_template, request

app = Flask(__name__)    


@app.route("/") #, methods=['GET', 'POST'])
def disp_loginpage(): 
   return render_template( 'login.html' ) 

@app.route("/auth") 
def authenticate():  
    if (request.args['username'] == 'Selective Soup' and request.args.get('Password')== 'hello'):
        return render_template('response.html', username=request.args['username'], password=request.args.get('Password'))
    else:
        return render_template('login.html')
   


    
if __name__ == "__main__": 
    app.debug = True 
    app.run()