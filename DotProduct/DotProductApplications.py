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

# iterating through csv file to create vectors for every fruit (each component is a different nutritional value)
nutritionalVectors = []
for index, row, in fruits.iterrows():
    energy = row['energy (kcal/kJ)'] # the first component is energy content
    newEnergy = energy.split("/")
    energy = float(newEnergy[1])
    water = float(row['water (g)']) # the second component is water content, etc...
    protein = float(row['protein (g)'])
    totalFat = float(row['total fat (g)'])
    carbs = float(row['carbohydrates (g)'])
    calcium = float(row['calcium (mg)'])
    iron = float(row['iron (mg)'])
    phosphorus = float(row['phosphorus (mg)'])
    vitaminC = float(row['vitamin C (mg)'])
    # creating the vector based on the above components
    nutritionalVector = np.array([energy, water, protein, totalFat, carbs, calcium, iron, phosphorus, vitaminC])
    nutritionalVectors.append(nutritionalVector) # adding the vector to list of all vectors
print(nutritionalVectors)
