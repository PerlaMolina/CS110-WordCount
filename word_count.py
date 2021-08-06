
import string

file = open("Gettysburg_Address.txt", "r")

text = file.read()
text = text.lower().split()

wordCount = {}

for item in text:
    wordCount[item] = text.count(item)

for key, value in wordCount.items() :
    print(key, ":", value)

word = True
while word:
	wordInput = str(input("Enter a word: "))
	if wordInput == "":
		print("Goodbye!")
		word = False
	elif (wordInput in wordCount) == True:
		print("The word '", wordInput, "' is found ", wordCount.get(wordInput), "times")
		#word = False
	else:
		print("That word isn't in the file.")

file.close()
