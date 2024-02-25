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
        if data[i][0]:
            # 1st main column: Jyutping, English - Chinese (pinyin)
            translation = translate(data[i][0])
            data[i][1] = f"{translation[0]}  -  {translation[1]} ({pinyin(translation[1])})"
        if data[i][2]:
            # Add Jyutping (2nd main column)
            data[i].append(f"{get_jyutping(data[i][2])}  -  {chinese_converter.to_simplified(data[i][2])} ({pinyin(data[i][2])})")

        progress = round((i + 1) * 100 / len(data))
        print(f"{progress}%", end="\r")
    print()

    # Export based on language selection
    with open("Cantonese.tsv", "w+", newline="", encoding="utf-8") as f: # Writes it in the right path 
        writer = csv.writer(f, delimiter="\t")
        writer.writerows(data)
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