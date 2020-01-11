import json
import nltk, re, random
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


def word_report(text):

	word_tokens = word_tokenize(text)

	stop_words = set(stopwords.words('english'))

	filtered_sentence = [w for w in word_tokens if not w in stop_words]
    stop_words_present = [w for w in word_tokens if w in stopwords]


    filteredSentDict = {}

    for token in filtered_sentence:
    	if token in filteredSentDict.keys():
    		filteredSentDict[token] += 1
    	else:
    		filteredSentDict[token] = 1


    stopWordsSentDict = {}

    for token in stop_words_present:
    	if token in stopWordsSentDict.keys():
    		stopWordsSentDict[token] += 1
    	else:
    		stopWordsSentDict[token] = 1


    word_report_dict = {}

    word_report_dict['Tokens'] = filteredSentDict
    word_report_dict['Stop Words'] = stopWordsSentDict

    word_report_json = json.dumps(word_report, indent=4, sort_keys=True)

    return word_report_json

string = input("Input string: ")

print(word_report(string))





