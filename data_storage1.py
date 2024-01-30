# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 20:27:51 2024

@author: Francisca Thimothy
"""

# Storing data
B1 = 30
B2 = 44
B3 = 90
B4 = 100
B5 = 120

print (B1)
print (B2)

# using list
age = [30, 44, 90, 100, 120, 22, 49, 50, 10]
print (age)

# Lists indexes start at 0 which has the value of 30
print(age[0])
print(age[1])

age = [30, 44, 90, 100, 120, 22, 49, 50, 10]

# Basic Stats
age = [30, 44, 90, 100, 120, 22, 49, 50, 10]
print(min(age))
print(max(age))
print(len(age))
print(sum(age))
average = sum(age)/len(age)
print(average)

# storing text




C2 = "M"
C3 = "M"
C4 = "F"
print(C2)
print(C3)
print(C4)

# gender list
gender = ["M","M", "F", "M", "F", "M", "M", "F"]
print (gender[0])
print (gender[1])
print (gender[2])
print (gender [-1]) 


# country list
country = ["Nigeria", "botswana", "Niger", "Togo", "Cape_verd", "South_Africa" ]
print (country)
print (country[0])
print (country[5])

# Data storage with list
my_list = [49, 50, 44, 2000, -199, "tau", "node"]
print (my_list)
print (my_list[:])
my_list.append("pi")
print(my_list)

my_list.append("zaneta")
print(my_list)
my_list.insert(1,"pi2")
print(my_list)
my_list.insert(8,"Timothy")
print(my_list)
my_list.remove("pi")
print(my_list)
my_list.remove("zaneta")
print(my_list)
my_list.remove("pi2")
print(my_list)

print(len(my_list))
# View a certain range of items:
    
print(my_list[0:3])

person = {'name': 'John Doe', 'age': 30, 'address': '123 Main St.'}
print(person['name']) 
print(person.get('age')) 
print(person.get('address')) 

import pandas as pd
# Creating a DataFrame
data = {"age":[30, 44, 90, 100, 120, 22, 49, 50],
"gender" :["M","M", "F", "M", "F", "M", "M", "F"],
"country":["Nigeria", "botswana", "Niger", "Togo", "Cape_verd", "South_Africa", "Carmeroun", "Benin"]}
#df = data frame
df = pd.DataFrame(data)
print(df)

# Basic statistics
print(df['age'].min())
print(df['age'].max())
print(df['age'].mean())

# Filtering data
print(df[df['age'] > 30])

# Slicing rows and columns
print(df[1:4])  # Select rows 1 to 3 and all columns

# Adding a new column
df['new_column'] = [1, 2, 3, 4, 5, 6, 7, 8,]
print(df)

# Removing a column
df.drop(columns=['new_column'], inplace=True)
print(df)




        
