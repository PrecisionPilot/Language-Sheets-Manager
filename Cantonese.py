import pandas as pd
import numpy as np
import csv
from xpinyin import Pinyin
from chinese_converter import to_simplified, to_traditional
from translate import translate, translate2Cantonese
from pyjyutping import jyutping
import jyutping as jytp

def get_jyutping(text: str) -> str:
    # If ping1 has a none, then sub element with ping2
    ping1 = jytp.get(text)
    ping2 = jyutping.convert(text).split(" ")
    return " ".join([ping1[i] if ping1[i] else ping2[i] for i in range(len(ping1))])

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

# 1st deck back: English  -  Simplified (pinyin)
def cantonese_parser(data: list) -> list:
    data1 = []
    # temporary storage to remove duplicate words
    words = set()
    for i in range(len(data)):
        if not data[i][0]:
            break
        
        # Prevent duplicates
        if data[i][0] in words:
            continue
        else:
            words.add(data[i][0])

        translation = translate(data[i][0])
        # If there's already the English def given
        if data[i][1]:
            arr = [data[i][0], f"{data[i][1]}  -  {translation[1]} ({pinyin(translation[1])})"]
        else:
            arr = [data[i][0], f"{translation[0].capitalize()}  -  {translation[1]} ({pinyin(translation[1])})"]
        data1.append(arr)
        
        # Print progress
        progress = round((i + 1) * 100 / len(data))
        print(f"Cantonese1.tsv: {progress}%", end="\r")
    print("Cantonese1.tsv: 100%")
    return data1

def mandarin_parser(data: list, index: int) -> list:
    data2 = []
    # temporary storage to remove duplicate words
    words2 = set()
    for i in range(len(data)):
        if not data[i][index]:
            break

        # Prevent duplicates
        if data[i][index] in words2:
            continue
        else:
            words2.add(data[i][index])

        # 2nd deck front: Simplified (pinyin)
        arr = [f"{to_simplified(data[i][index])} ({pinyin(data[i][index])})", to_traditional(data[i][index])]
        data2.append(arr)
        
        # Print progress
        progress = round((i + 1) * 100 / len(data))
        print(f"Cantonese2.tsv: {progress}%", end="\r")
    print("Cantonese2.tsv: 100%")
    return data2

# front: Cantonese; back: English  -  Simplified (pinyin)
def mandarin2cantonese_parser(data: list) -> list:
    data3 = []
    # temporary storage to remove duplicate words
    words3 = set()
    for i in range(len(data)):
        if not data[i][0]:
            break

        # Prevent duplicates
        if data[i][0] in words3:
            continue
        else:
            words3.add(data[i][0])

        translation = translate2Cantonese(data[i][0])
        arr = [translation[1], f"{translation[0].capitalize()}  -  {data[i][0]} ({pinyin(data[i][0])})"]
        data3.append(arr)
        
        # Print progress
        progress = round((i + 1) * 100 / len(data))
        print(f"Cantonese.tsv: {progress}%", end="\r")
    print("Cantonese.tsv: 100%")
    return data3

def formatter(data: list):
    data1 = []
    data2 = []
    data3 = []
    if len(data[0]) == 3:
        data1 = cantonese_parser(data)
        data2 = mandarin_parser(data, 2)
    elif len(data[0]) == 2:
        data1 = cantonese_parser(data)
    elif len(data[0]) == 1:
        data3 = mandarin2cantonese_parser(data)

    # Export Cantonese1.tsv
    if data1:
        with open("Cantonese1.tsv", "w+", newline="", encoding="utf-8") as f: # Writes it in the right path 
            writer = csv.writer(f, delimiter="\t")
            writer.writerows(data1)
    # Export Cantonese2.tsv
    if data2:
        with open("Cantonese2.tsv", "w+", newline="", encoding="utf-8") as f: # Writes it in the right path 
            writer = csv.writer(f, delimiter="\t")
            writer.writerows(data2)
        print("\nSuccessfully exported!")
    
    if data3:
        with open("Cantonese.tsv", "w+", newline="", encoding="utf-8") as f: # Writes it in the right path 
            writer = csv.writer(f, delimiter="\t")
            writer.writerows(data3)
        print("\nSuccessfully exported!")


# ---End of formatter()

# introduction
print("Welcome to TSV Flashcard Organizer for Cantonese!")

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