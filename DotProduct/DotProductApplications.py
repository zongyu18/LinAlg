# import statements
import numpy as np
import pandas as pd
import csv
import itertools
import matplotlib
import matplotlib.pyplot as plt

# reading the csv file
fruits = pd.read_csv('fruits.csv')

# iterating through csv file to instantiate the array of fruit names
fruit_names = []
for index, row in fruits.iterrows():
    current_fruit = row['name']
    if " nutrition" in current_fruit: # cleaning the names up for consistency
        new_current_fruit = current_fruit.split(" nutrition")
        current_fruit = new_current_fruit[0]
    elif "nutriion: " in current_fruit:
        new_current_fruit = current_fruit.split("nutriion: ")
        current_fruit = new_current_fruit[1]
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

# using the dot product to calculate similarity between two fruit vectors (by looking at the angle between them)
def similarityHelper(indexOne, indexTwo):
    # identify the two vectors
    v1 = nutritionalVectors[indexOne]
    v2 = nutritionalVectors[indexTwo]
    # dot the two vectors
    dotProduct = np.dot(v1, v2)
    magnitudeOne = np.linalg.norm(v1)
    magnitudeTwo = np.linalg.norm(v2)
    # divide the dot product by the magnitudes of the vectors to get the cosine of the angle
    return round(((np.pi / 2) - np.arccos((dotProduct / (magnitudeOne * magnitudeTwo)))) / (np.pi / 2) * 100, 4)

def similarity(index):
    # finding the similarity between one fruit vector and all other fruit vectors
    list = []
    for i in range(len(fruit_names)):
        if i != index:
            list.append([similarityHelper(index, i), fruit_names[i]])
    list.sort()
    list.reverse() # sorting the list by most similar fruits

    # code to create graph of best and worst substitutes, as well as making the graph look nicer
    bestFruits = np.array([list[0][1], list[1][1], list[2][1], list[len(list)-2][1], list[len(list)-1][1]])
    bestFruitsValues = np.array([list[0][0], list[1][0], list[2][0], list[len(list)-2][0], list[len(list)-1][0]])

    ###

    # this portion of the code was taken from
    # https://stackoverflow.com/questions/64068659/bar-chart-in-matplotlib-using-a-colormap
    my_cmap = plt.get_cmap("coolwarm")
    rescale = lambda bestFruitsValues: (bestFruitsValues - np.min(bestFruitsValues)) / (np.max(bestFruitsValues) - np.min(bestFruitsValues))

    ###

    plt.bar(bestFruits, bestFruitsValues, color=my_cmap(rescale(bestFruitsValues)))
    plt.xlabel("Fruits")
    plt.ylabel("Similarity (%)")
    plt.title("Best and Worst Nutritional Substitutes For " + fruit_names[index])

    ###

    # this portion of the code was taken from
    # https://www.youtube.com/watch?v=nKyZ8mgaeXQ
    for i, v in enumerate(bestFruitsValues):
        plt.text(i, v + 0.30, str(v), ha = "center", size = 8, weight="bold")

    ###

    plt.show()

# method that asks for user input and runs the helper methods
def main():
    try:
        print("")
        for i in range(len(fruit_names)):
            print("(" + str(i) +") " + fruit_names[i], end = '   ')
        print("")
        print("")
        index = int(input("Enter the index of a fruit you would like a nutritional substitute for: ")) # user input
        similarity(index) # helper method
    except:
        print("Your index is invalid!")
main()
