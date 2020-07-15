import json
from difflib import get_close_matches


def checkmore():
	"""Keeps the application running until the user wants to quit
	"""
	more = input('Search for more words? [y/n]: ')

	if str.lower(more) == 'y':
		prompt()
	elif str.lower(more) == 'n':
		print('Goodbye!')
	else:
		print('Please enter Y or N')
		checkmore()


def suggest(word):
	"""Suggest most similar alternative to `word` from the dictionary
	"""
	alt_word = get_close_matches(word, data.keys(), n=1, cutoff=0)[0]
	yn = input(f"'{word}' not found. Did you mean '{alt_word}' instead? [y/n]: ")
	if str.lower(yn) == 'y':
		return search(alt_word)
	elif str.lower(yn) == 'n':
		return f"'{word}' not found"
	else:
		print('Please enter Y or N')
		suggest(word)


def search(word):
	"""Searches for the `word` in the keys of the data dictionary and returns the meaning.
	If no match is found, calls the suggest() function
	"""
	if word in data:
		return data[word]
	elif word.upper() in data:
		return data[word.upper()]
	elif word.title() in data:
		return data[word.title()]
	elif word.lower() in data:
		return data[word.lower()]
	elif len(get_close_matches(word, data.keys(), n=1, cutoff=0)) > 0:
		return suggest(word)
	else:
		return f"{word} not found"


def prompt():
	"""Gets the input from the user, displays the result, and checks if more words are to be searched for
	"""

	word = input("Enter a word: ")
	output = search(word)

	if type(output) == list:
		for item in output:
			print(item)
	else:
		print(output)

	checkmore()


data = json.load(open('data.json'))

prompt()