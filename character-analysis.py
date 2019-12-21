# charater analysis
import pandas as pd
import re
import sys

file = sys.argv[1]

alpha = dict()
numeric = dict()

with open(file, 'r') as f:
	for line in file:
		for i in line:
			if i.lower() in [a-z]: alpha[i.lower()] += 1
				if i in [0-9]: numeric[i] += 1
				if i in [!@#$%^&*()<>?:"]

	else: chars[i] = 1


text_df = pd.DataFrame(chars, index=False)

text_df.to_json()

filename_analysis = file

filename = f'{filename_analysis}-analysis.txt'

with open(f'{file}file.txt') as f:
	json.dump(f, text_df)







