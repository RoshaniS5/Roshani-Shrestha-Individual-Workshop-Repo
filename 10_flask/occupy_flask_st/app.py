# The Red Imposter - Daniel Sooknanan, Shadman Rakib, and Roshani Shrestha
# SoftDev
# K10: Putting Little Pieces Together - Sends the output of our occupation-chooser to a webpage
# 2021-10-06

from flask import Flask
from csv import DictReader
from random import choices

app = Flask(__name__) #create instance of class Flask

# Create a dictionary given the filename
def makeDict(filename):
    dict = {} 

    try:
        with open(filename) as csvfile:
            reader = DictReader(csvfile)
            for row in reader: 
                dict[row['Job Class']] = float(row['Percentage']) 

            if 'Total' in dict.keys(): 
                dict.pop('Total') 
    
    except FileNotFoundError: 
        print('File "%s" does not exist' % (filename))

    return dict

# Return a random key given the frequency at which it should appear (second column of csv)
def getRandomKey(dictionary):
    if (len(dictionary) > 0):
        result = choices(list((dictionary).keys()), weights=dictionary.values(), k=1)[0]
        return '<h3>Selected: %s</h3>' % result
    else:
        return '<h3>Selected: None (no occupations to select from)</h3>'

# Return a string of all the keys in the given dictionary
def listKeys(dictionary):
    key_list = '<div>Occupations: '
    for key in dictionary.keys():
        key_list += '<div>%s</div>' % (key)
    return key_list + '</div>'

@app.route("/")       #assign fxn to route

def main():
    filename = 'occupations.csv' 
    occ_dict = makeDict(filename)
    header = '<h3>The Red Imposter | Daniel Sooknanan, Roshani Shrestha, Shadman Rakib</h3>'
    return header + getRandomKey(occ_dict) + listKeys(occ_dict)


if __name__ == "__main__":  # true if this file NOT imported
    app.run()