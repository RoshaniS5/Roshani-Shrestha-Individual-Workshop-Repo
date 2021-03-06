# The Red Imposter | Daniel Sooknanan (Sussy), Roshani Shrestha (Pete), Shadman Rakib (Ducky)
# SoftDev
# K12: ...or The Only Constant is Change? - app.py in 12_flask-jinja, serves a templated page
# 2021-10-08

from flask import Flask, render_template #Q0: What happens if you remove render_template from this line?
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "No hablo queso!"

coll = [0,1,1,2,3,5,8]

@app.route("/my_foist_template") #Q1: Can all of your teammates confidently predict the URL to use to load this page?
def test_tmplt():
    return render_template( 'model_tmplt.html', foo="fooooo", collection=coll) #Q2: What is the significance of each argument?

if __name__ == "__main__":
    app.debug = True
    app.run()
