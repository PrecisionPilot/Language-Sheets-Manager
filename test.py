# import numpy as np

# fileName = "test/translations.tsv"

# data = np.loadtxt(fileName, dtype=str, delimiter="\t", encoding="utf-8") #reading data from tsv 
# data = data.tolist()

def readTSV():
    myText = open(r'text.txt','w')
    myString = 'Type your string here'
    myText.write(myString)
    myText.close()

readTSV()