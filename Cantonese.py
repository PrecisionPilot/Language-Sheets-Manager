import pandas as pd
import numpy as np
import csv
from xpinyin import Pinyin
import chinese_converter
from translate import translate
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

def formatter(data: list):

    for i in range(len(data)):
        if not data[i]:
            break

        # 2nd deck front: Simplified (pinyin)
        data[i] = [f"{chinese_converter.to_simplified(data[i])} ({pinyin(data[i])})", chinese_converter.to_traditional(data[i])]
        
        # Print progress
        progress = round((i + 1) * 100 / len(data))
        print(f"Cantonese2.tsv: {progress}%", end="\r")
    print("Cantonese2.tsv: 100%")

    # Export Cantonese.tsv
    with open("Cantonese.tsv", "w+", newline="", encoding="utf-8") as f: # Writes it in the right path 
        writer = csv.writer(f, delimiter="\t")
        writer.writerows(data)


# ---End of formatter()

# introduction
print("Welcome to TSV Flashcard Organizer for Cantonese!")

# x = input("Type in the path of the your tsv file to organize (you may also type in a relative directory): ")
print("Paste in the copied speadsheet")
userInput = inputMultiline()
print("Loading...")

# Convert to list
userInput = userInput.split("\n")

formatter(userInput)

# Add feature to automatically detect the desktop location