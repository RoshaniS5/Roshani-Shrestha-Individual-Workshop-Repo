# SUMMARY OF TRIO DISCUSSION
# We discussed the lists of names and how we had to change each element. We also discussed which methods were more concise and picked that to use. We combined using random.choice with the method of using a function. We also discussed adding input so that the user can choose a class if they want. We also talked about how to access different dictionary values.
# DISCOVERIES
# We each discovered other ways to pick and print a name at random. There was randrange, random.choice, and even random.randint. We also discovered a way to use dictionaries instead of lists, which wasn't too different from using lists.
# QUESTIONS
# There were no questions.
# COMMENTS
# It was insightful to collaborate with other people and gain new ideas for this python program. It was interesting to make this program have user input.

import random

# Dictionary for people in periods 1 and 2
KREWES = {
    'orpheus': ['Alejandro Alonso', 'Aryaman Goenka', 'Christopher Liu', 'Deven Maheshwari', 'Emma Buller', 'Ella Krechmer', 'Gavin McGinley',
           'Haotian Gan', 'Ivan Lam', 'Ishraq Mahid', 'Ivan Mijacika', 'Julia Nelson', 'Lucas Lee', 'Lucas Tom wong',
           'Michelle Lo', 'Oscar Wang', 'Owen Yaggy', 'Rayat Roy', 'Reng geng Zheng', 'Shriya Anand', 'Shyne Choi', 'Sadid Ethun',
           'Tomas Acuna', 'Theodore Fahey', 'Tina Nguyen', 'Tami Takada', 'William Chen', 'Yusef Elsharawy', 'Zhao yu Lin'],
    'endymion': ['Alif Abdullah', 'Andrew Juang', 'Andy Lin', 'Austin Ngan', 'Annabel Zhang', 'Cameron Nelson', 'David Chong',
            'Daniel Sooknanan', 'Eric Guo', 'Eliza Knapp', 'Hebe Huang', 'Han Zhang', 'Yoonah Chang', 'Joshua Kloepfer',
            'Josephine Lee', 'Jonathan Wu', 'Jesse Xie', 'Justin Zou', 'Kevin Cao', 'Liesel Wong', 'Michael Borczuk',
            'Noakai Aronesty', 'Patrick Ging', 'Qina Liu', 'Roshani Shrestha', 'Rachel Xiao', 'Raymond Yeung', 'Sophie Liu',
            'Shadman Rakib', 'Thomas Yu', 'Wen hao Dong', 'Yaying Liang li', 'Yuqing Wu']
}

def random_student():
    val = input('Which class? class1 or class2\n') # user can input a class
    if (val == 'class1'):
        print(random.choice(KREWES['orpheus'])) # chooses and prints a name from the 'orpheus' list
    elif (val == 'class2'):
        print(random.choice(KREWES['endymion'])) # chooses and prints a name from the 'endymion' list
    else:
        random_class = random.choice([KREWES['orpheus'], KREWES['endymion']]) # chooses one of the lists at random
        print(random.choice(random_class)) # chooses and prints a name from that list

random_student() # calls the function
