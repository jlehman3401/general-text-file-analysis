from collections import OrderedDict
import json
import nltk
import pandas as pd

'''
This is for evaluating all the characters within in a string

how many alphabetical characters

how many and which numeric characters

how many and which special characters

'''
def char_report(string):

	# ordering characters by alphabetical first, numeric, then special?
	char_dict = dict()

	alpha_dict = dict()
	num_dict = dict()
	special_dict = dict()

	alpha_keys = list()
	num_keys = list()
	special_keys = list()

	# for letter in string
	if i.isalpha():
		if i in alpha_dict.keys():
			alpha_dict[i.lower()] += 1
		else:
			alpha_dict[i.lower()] = 1
			alpha_keys.append(i.lower())


	elif i.isnumeric():
		if i in num_dict.keys():
			num_dict[i] += 1
		else:
			num_dict[i] = 1
			num_keys.append(i)

	else:
		if i in special_dict.keys():
			special_dict[i] += 1
		else:
			special_dict[i] = 1
			special_keys.append(i)


	sortedAlpha = sorted(alpha_keys)
	sortedNum = sorted(num_keys)
	sortedSpecial = sorted(special_keys)


	alpha_Ordered = OrderedDict((key, alpha_dict[key]) for key in sortedAlpha)		

	num_Ordered = OrderedDict((key, num_dict[key]) for key in sortedNum)

	special_Ordered = OrderedDict((key, special_dict[key]) for key in sortedSpecial)


	char_dict["Alphabetical Chars"] = alpha_Ordered	
	char_dict["Numeric Chars"] = num_Ordered	
	char_dict["Special Chars"] = special_Ordered	

	return char_dict






