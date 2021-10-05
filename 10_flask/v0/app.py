# The Red Imposter - Daniel Sooknanan, Shadman Rakib, and Roshani Shrestha
# SoftDev
# K10: Putting Little Pieces Together - Details our predictions and results in the form of comments for this file
# 2021-10-05

from flask import Flask
app = Flask(__name__) # Q0: Where have you seen similar syntax in other langs?

@app.route("/") # Q1: What points of reference do you have for meaning of '/'?
def hello_world():
    print(__name__) # Q2: Where will this print to? Q3: What will it print?
    return "No hablo queso!"  # Q3: Will this appear anywhere? How u know?

app.run()  # Q4: Where have you seen similar construcs in other languages?

# Predictions: 
# It should produce the same results as K09. It should print the "__name__" in the terminal after opening the link, which is "__main__". "No hablo queso!" will print on the browser.

# Results: 
# It worked as expected and as it did previously.

