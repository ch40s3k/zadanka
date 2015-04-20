#!/usr/bin/env python
import re

def _capitalize(words):
	'''
	Return First Letter Capitalized 
	'''
	return ''.join(word[0].upper() + word[1:] for word in re.split('(\s+)', words))



words = "Taki tam tesCIOR \nco sprawdza czy dziAla"
print _capitalize(words)

