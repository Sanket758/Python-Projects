#import necessary libraries
import json
from difflib import get_close_matches 

#load json file
data = json.load(open('data.json'))


# Creating a function to get meaning of the given word from our dictionary
def get_meaning(word):
	# Scenario 1: word is in our dictionary
	if word in data:
		return data[word]
	# Scenario 2: There is typo in users input, check for closest matching word
	elif len(get_close_matches(word, data.keys(), cutoff=.8)) > 0:
		match = get_close_matches(word, data.keys(), cutoff=.8)[0]
		check = input("Did you mean %s, instead? Enter Y if yes, otherwise N: " %match)
		if check.lower() == 'y':
			return data[match]
		elif check.lower() == 'n':
			return "Word doesn't exist"
		else:
			return "Invalid choice"
	# if word is not not at all available in our vocabulary
	else:
		return "The Word Doesn't exist in the dictionary, sorry!"

while True:
	#get a word from user
	word = input('Enter a word you want to know the meaning of: ')
	if word == "quit":
		break
	#print the output
	output = get_meaning(word.lower())

	# If certain word has more than one meaning then iterate over them
	if type(output) == list:
		for item in output:
			print(item)
	else:
		print(output)

