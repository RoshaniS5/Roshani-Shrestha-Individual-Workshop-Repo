# The Red Imposter - Daniel Sooknanan, Shadman Rakib, and Roshani Shrestha
# SoftDev
# K10: Putting Little Pieces Together - Sends the output of our occupation-chooser to a webpage
# 2021-10-05

from flask import Flask
from csv import DictReader
from random import choices

app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    result = '<h1>The Red Imposter - Daniel Sooknanan, Shadman Rakib, and Roshani Shrestha</h1><br/><br/><b>List of Occupations:</b><br/>'
    occ_dict = {} # Create a dictionary to be filled in
    filename = 'occupations.csv' # Specifies the target .csv file

    try:
        with open(filename) as csvfile:
            reader = DictReader(csvfile)
            for row in reader: 
                # Fill in the dictionary with Job Classes as keys & Percentages as values
                occ_dict[row['Job Class']] = float(row['Percentage']) 

            if 'Total' in occ_dict.keys(): 
                occ_dict.pop('Total') # Remove the Total at the end of the .csv file if it exists
            
            for k in occ_dict.keys():
                result += k + '<br/>'
            result += '<br/>'
            
            # Get the first item in a list that is length k (in this case 1)
            # The randomness of a key appearing is weighted based on its respective value
            occ = choices(list(occ_dict.keys()), weights=occ_dict.values(), k=1)[0]
            result += '<b>Selected Occupation:</b> ' + occ 
            return result
    
    except FileNotFoundError: 
        return 'File "%s" does not exist' % (filename)

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()