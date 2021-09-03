import pandas as pd
import numpy as np
import csv
import os

def formatter(path):
    # get tsv file and store it in a list
    data = np.loadtxt(path, dtype=str, delimiter="\t", encoding="utf-8") #reading data from tsv 
    data = data.tolist()
    
    # variables
    languagesData = {}
    languages = []
    languagesSelection = []

    # switch the languages around to the right order
    for row in data:
        if row[0] == "English":
            row[0], row[1] = row[1], row[0]
            row[2], row[3] = row[3], row[2]
    
    # Get all existing languages in the spreadsheet, store it on "languages" list
    for row in data:
        # row[0] represents the language of the row
        if not row[0] in languagesData:
            languagesData[row[0]] = []
        # store the row on the dictionary
        languagesData[row[0]].append(row[2:4]) # get only the translation
    

    # ---Exporting process---
    
    # Ask user which language to output
    print("select languages (seperated by spaces) to output as csv: ", end="")
    for key,val in languagesData.items(): languages.append(key)
    for i in range(len(languages) - 1):
        print(languages[i])
    print(languages[-1])
    languagesSelection = input("\n").split(' ')

    # Get folder of the path
    destination_path = os.path.dirname(path)
    if destination_path: # C:\Users\seanw\Downloads\ -> Downloads/
        destination_path += "\\"

    # Export based on language selection
    exportCount = 0
    if languagesSelection[0].lower() == "all":
        languagesSelection = languages
    print(languagesSelection)
    for languageSelection in languagesSelection:
        with open(destination_path + languageSelection + ".csv", "w+", newline="", encoding="utf-8") as f: #writes it in the right path 
            writer = csv.writer(f)
            writer.writerows(languagesData[languageSelection])
        exportCount += 1
    
    print("Successfully exported", exportCount, "file(s)!")
    print("Have a good day")

x = input("type in the path of the your tsv file to organize\n" +
            "type \"this\" for local directory\n")
            
if x == "this":
    formatter(input("type in file name: "))
else:
    formatter(x)


# Find a way to combine "Chinese" and "Chinese (Simplified)"
# See if commas cause problems to the csv when reading from Anki and Quizlet
# Sort dictionary if possible
# Perhaps save it as a tsv