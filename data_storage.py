# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 14:40:48 2024

@author: Francisca Thimothy
"""

"""'sto'ring data in python
1. List
2. Dictionaries
3. Data frames - specific to pandas
"""

import pandas

file = pandas.read_csv ("country_data.csv")

print(file)

g1 = "M"
g2 =  "F"
g3 = "M"

Gender = ["M", "F", "F"]

c1 = "South Africa"
c2 = "Lesotho"
age = [30, 25, 29, 46, 22]
"""
[30, 25, 29, 46, 22]
"""

age.append (100)

print(age)

"""
[30, 25, 46, 22, 100]

"""
#Dictionaries _ Key : Value pairs


"""
cat : "a cute animal"
"""

mammals = {"cat" : "a cute animal", "Lion": "King of the jungle", "Elephant": "a gigantic herbivore"}

print (mammals["cat"])

"""
Data frames
"""

fruits = ["apple", "banana", "orange", "grape", "kiwi"]

size_nm = [9.8, 10.1, 13.2, 8.7, 20.5]

fruit_size = {
    'fruits': fruits,
    'sizes' : size_nm
    
    }
"""
df = dataframe
"""


import pandas as pd
df = pd.DataFrame(fruit_size)
print(df)

#df = data frame

# Displaying the DataFrame
print(df)
import pandas as pd

# Creating a DataFrame
data = {
    'age': [30, 40, 30, 49, 22, 35, 22, 46, 29, 25, 39],
    'gender': ["M", "M", "F", "M", "F", "F", "F", "M", "M", "F", "M"],
    'country': ["South Africa", "Botswana", "South Africa", "South Africa", "Kenya", "Mozambique", "Lesotho", "Kenya", "Kenya", "Egypt", "Sudan"]
}

#df = data frame
df = pd.DataFrame(data)

# Displaying the DataFrame
print(df)




