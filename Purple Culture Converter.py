import csv
import os

# def inputMultiline() -> str:
#     userInput = ""
#     while True:
#         i = input()
#         if i == "":
#             # Remove the last newline
#             userInput = userInput[0:-1]
#             break
#         userInput += i + "\n"
#     return userInput

# print("Paste in the copied speadsheet")
# userInput = inputMultiline()
# print("Loading...")

# # Convert to 2d list
# userInput = userInput.split("\n")
# for i, inp in enumerate(userInput):
#     userInput[i] = inp.split("\t")

# Read csv file and store it in a list
file_name = "My Words  Purple Culture, Online Chinese Bookstore for Chinese Language Learning, Culture Studying, Statistics  Yearbooks and More.csv"
path = os.path.expanduser(f"~\\Downloads\\{file_name}")
with open(path, "r", encoding="utf-8") as f: # Reads it in the right path
    reader = csv.reader(f)
    userInput = list(reader)

# Only keep the second and fifth columns
data = []
for i in range(len(userInput)):
    data.append([userInput[i][1], userInput[i][4]])

# Export the data
with open("Chinese.tsv", "w+", newline="", encoding="utf-8") as f: # Writes it in the right path 
    writer = csv.writer(f, delimiter="\t")
    writer.writerows(data)
print("\nSuccessfully exported!")