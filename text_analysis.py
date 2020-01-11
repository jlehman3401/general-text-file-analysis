from collections import OrderedDict
import json
# import nltk
import pandas as pd
import sys

'''
This is for evaluating all the characters within in a string

how many alphabetical characters

how many and which numeric characters

how many and which special characters

'''
def char_report(input_string):

	string = ''

	for char in input_string:
		if char.isalpha():
			string = string + char.lower()
		else:
			string = string + char


	# ordering characters by alphabetical first, numeric, then special?
	char_dict = dict()

	alpha_dict = dict()
	num_dict = dict()
	special_dict = dict()

	for i in string:
		if i.isalpha():
			if i in alpha_dict.keys():
				alpha_dict[i] += 1
			else:
				alpha_dict[i] = 1

		elif i.isnumeric():
			if i in num_dict.keys():
				num_dict[i] += 1
			else:
				num_dict[i] = 1

		else:
			if i in special_dict.keys():
				special_dict[i] += 1
			else:
				special_dict[i] = 1


		char_dict["Alphabetical Chars"] = alpha_dict	
		char_dict["Numeric Chars"] = num_dict
		char_dict["Special Chars"] = special_dict	

	json_output = json.dumps(char_dict, indent=4, sort_keys=True)

	return json_output


string = input("Input string: ")

print(char_report(string))




