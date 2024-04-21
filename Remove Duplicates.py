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


# x = input("Type in the path of the your tsv file to organize (you may also type in a relative directory): ")
print("Show duplicates based on first column with this script. Paste in the copied spreadsheet.")
userInput = inputMultiline()
print("Loading...")

# Convert to 2d list
userInput = userInput.split("\n")
for i, inp in enumerate(userInput):
    userInput[i] = inp.split("\t")

# Show duplicates based on first column and their count
words = set()
duplicates = {}
for i in userInput:
    if i[0] in words:
        duplicates[i[0]] = duplicates.get(i[0], 0) + 1
    else:
        words.add(i[0])

if duplicates:
    print("Duplicates:")
    for key, value in duplicates.items():
        print(key, value)
else:
    print("No duplicates found.")