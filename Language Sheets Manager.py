import pandas as pd
import numpy as np
import csv
from xpinyin import Pinyin
from pathlib import Path

def pinyin(x: str) -> str:
    p = Pinyin()
    return p.get_pinyin(x, tone_marks="marks").replace("-", " ")

def inputMultiline() -> str:
    userInput = ""
    while True:
        i = input()
        if i == "":
            # Remove the last newline
            userInput = userInput[0:-1]
            break
        userInput += i + "\n"
    return userInput

def formatter(data: list):
    
    list = [[0, 1], [0, 2]]

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
        if data[i][0] == "Chinese" or data[i][0] == "Chinese (Traditional)": # Add pinyin to the English part if it's a Chinese translation
            data[i][3] = "(" + pinyin(data[i][2]) + ")  " + data[i][3]

    # Get all existing languages in the spreadsheet, store it in "languagesData" list
    for row in data:
        if not row[0] in languagesData:
            languagesData[row[0]] = []
        # store the row on the dictionary
        languagesData[row[0]].append(row[2:4]) # get only the translation


    # ---Exporting process---
    
    # Ask user which language to output to csv
    for key,val in languagesData.items():
        languages.append(key)
    languages.sort()
    languageOptions = ""
    for i, language in enumerate(languages):
        languageOptions += language + f" ({i}), "
    languageOptions = languageOptions[0:-2]
    # print the language options available
    print("\nSelect languages (seperated by a space) to output as tsv (tip: type \"all\" to use all options)\n" +
            f"Here are your options: {languageOptions}")
    
    # Get user language selection
    userInput = input()
    if userInput == "all": # type "all" to export all the languages there is
        languagesSelection = languages
    else:
        languagesSelection = [languages[int(i)] for i in userInput.split(' ')] # store user's selections as a number array

    # Get the downloads folder
    # destination_path = str(Path.home() / "Downloads")
    destination_path = ""
    if destination_path: # C:\Users\seanw\Downloads\ -> Downloads\
        destination_path += "\\"


    # Export based on language selection
    exportCount = 0
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
print("- Pinyin will be automatically added to translations in Chinese")

# Fail-safe script
# Automatically export when there's only one option for languages

# Option of pasting the tsv spreadsheat directly into the console
# Option of typing in the words directly and use a translate library

# x = input("Type in the path of the your tsv file to organize (you may also type in a relative directory): ")
print("Paste in the copied speadsheet")
userInput = inputMultiline()
print("Loading...")

# Convert to 2d list
userInput = userInput.split("\n")
for i, inp in enumerate(userInput):
    userInput[i] = inp.split("\t")

formatter(userInput)

# Add feature to automatically detect the desktop location