import json
from difflib import get_close_matches

data = json.load(open('data.json'))


def definition(w):
	best_matches = get_close_matches(w, data.keys())
	w = w.lower()
	if w in data:
		return data[w]
	elif len(best_matches) > 0:
		yn = input('Did you mean %s instead? (Y/N): ' % best_matches[0])
		if yn == 'Y':
			return data[best_matches[0]]
		elif yn == 'N':
			return 'No other matches, please try again'	
		else:
			return "We didn't understand your query"	
	else:
		return 'No such record in the data'	


word = input('Enter word of choice: ')

output = definition(word)

if type(output) == list:
	for item in output:
		print(item)
else:
	print(output)		

