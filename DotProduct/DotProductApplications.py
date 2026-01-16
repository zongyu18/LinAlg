# import statements
import numpy as np
import pandas as pd
import csv
import itertools

# reading the csv file
fruits = pd.read_csv('fruits.csv')

# iterating through csv file to instantiate the array of fruit names
fruit_names = []
for index, row in fruits.iterrows():
    current_fruit = row['name']
    if " nutrition" in current_fruit: # cleaning the names up for consistency
        new_current_fruit = current_fruit.split(" nutrition")
        current_fruit = new_current_fruit[0]
    fruit_names.append(current_fruit)
print(fruit_names)
