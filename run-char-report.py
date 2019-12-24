from collections import OrderedDict
import json
import sys
from text_analysis import char_report
from datetime import datetime


string = sys.argv[1]

title = input("Desired name of file: ")

report = char_report(string)


currentTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

if len(title) < 1:
	title = '____'

filename = f'{title}-{currentTime}-report.txt' 

with open(filename, 'w') as outfile:
	json.dump(report, outfile, indent=4)




