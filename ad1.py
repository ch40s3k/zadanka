'''
Task #1
Implement a function in Python that receives a string as a parameter and returns the same
string with a capital letter at the beginning of each word.
'''

#!/usr/bin/env python
import re

def _capitalize(words):
	'''
	Return First Letter Capitalized 
	'''
	return ''.join(word[0].upper() + word[1:] for word in re.split('(\s+)', words) if len(word)>0)



words = "Taki tam tesCIOR \nco sprawdza czy dziAla"
print _capitalize(words)

empty = "   "
print _capitalize(empty)