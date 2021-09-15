import pandas as pd
import numpy as np
import csv
import os
from os import path

def formatter(fileName):
    # get tsv file and store it in a list
    if path.exists(fileName):
        data = np.loadtxt(fileName, dtype=str, delimiter="\t", encoding="utf-8") #reading data from tsv 
        data = data.tolist()
    else:
        print("file name doesn't exist, please try again")
        return
    
    # variables
    languagesData = {}
    languages = []
    languagesSelection = []

    # switch the languages around to the right order
    for i in range(len(data)):
        # data[i][0] represents the language in each row
        if data[i][0] == "English":
            data[i][0], data[i][1] = data[i][1], data[i][0]
            data[i][2], data[i][3] = data[i][3], data[i][2]
        if data[i][0] == "Chinese (Simplified)": # Make sure all is "Chinese" not "Chinese (Simplified)"
            data[i][0] = "Chinese"
    
    # Get all existing languages in the spreadsheet, store it in "languagesData" list
    for row in data:
        if not row[0] in languagesData:
            languagesData[row[0]] = []
        # store the row on the dictionary
        languagesData[row[0]].append(row[2:4]) # get only the translation

    # ---Exporting process---
    
    # Ask user which language to output to csv
    print("\nSelect languages (seperated by spaces) to output as tsv (tip: type \"all\" to use all options)\n" +
            "Here are your options (", end="")
    for key,val in languagesData.items(): languages.append(key)
    languages.sort()
    for i in range(len(languages) - 1): # print the language options available
        print(languages[i], end=", ")
    print(languages[-1] + "): ", end="")
    languagesSelection = input().split(' ') # store user's selection(s)
    for i in range(len(languagesSelection)): # anti case sensitive code
        languagesSelection[i] = languagesSelection[i][0].upper() + languagesSelection[i][1:].lower()

    # Get folder of the path
    destination_path = os.path.dirname(fileName)
    if destination_path: # C:\Users\seanw\Downloads\ -> Downloads\
        destination_path += "\\"


    # Export based on language selection
    exportCount = 0
    if languagesSelection[0].lower() == "all": # type "all" to export all the languages there is
        languagesSelection = languages
    for i in range(len(languagesSelection)): # Fail-safe mechanism: Make sure selection languages exist
        if not languagesSelection[i] in languages:
            del languagesSelection[i] # remove elemend of the languages selection that doesn't exist

    # Export
    for languageSelection in languagesSelection:
        with open(destination_path + languageSelection + ".tsv", "w+", newline="", encoding="utf-8") as f: #writes it in the right path 
            writer = csv.writer(f, delimiter="\t")
            writer.writerows(languagesData[languageSelection])
        exportCount += 1
    
    # Message for whether the export succeeded or not
    if exportCount > 0:
        print("\nSuccessfully exported", exportCount, "file(s)!")
        for selection in languagesSelection:
            print(selection + ".tsv")
        print("\nHave a good day!")
    else:
        print("No files exported, check if you spelled your options right")
# ---End of formatter()

# introduction
print("Welcome to TSV Flashcard Organizer!")
print("This is a fail-safe python script where you will feed the spreadsheet exported from Google Translate saved translations to be "
        + "organized and optimized for exporting to your favorite flashcard app\n")
print("What this app will do:")
print("- All translations will be sorted from the language you're learning (eg. Chinese to English)")
print("- Different languages will be sorted into their own spreadsheet file (tsv) you'll have the option which ones you want to export")

# Fail-safe script
# Google translate spreadsheet to sort it and export it into different spreadsheat files of your choosing
# Output files optimized to be imported to Anki or Quizlet flashcards

x = input("Type in the path of the your tsv file to organize (tip: type \"this\" for local directory): ")

if x.lower() == "this":
    formatter(input("Type in file name: "))
else:
    formatter(x)


# Make 100% fail-safe