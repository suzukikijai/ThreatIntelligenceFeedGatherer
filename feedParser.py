import re 
from bs4 import BeautifulSoup
import requests
import pickle

def squidblacklist(srcURL,regPat,targetFile = 'output.pkl'):
	source = requests.get(srcURL).text
	soup = BeautifulSoup(source,'lxml')
	match = soup.p.text
	test_str = match

	matches = re.finditer(regPat, test_str, re.MULTILINE)

	for matchNum, match in enumerate(matches):
		matchNum = matchNum + 1
		line = re.sub(regPat, r"\1", match.group())
		print(line)
	with open(targetFile, 'wb') as f:
		pickle.dump(line, f)
	return  



def main():
	# VAR Declaration
	sourceCSV = "patterns_url.csv"
	URL_regex = "^[^,]+"
	pattern_regex = "[^,]+$"

	with open(sourceCSV) as collector:
		next(collector)
		for line in collector: 
			#print(line)
			URLMatches = re.findall(URL_regex,line)
			for URLMatched in URLMatches:
				url = URLMatched
				# print(url)
			patternMatches = re.findall(pattern_regex,line)
			for patternMatched in patternMatches:
				patternData = patternMatched
				# print(patternData)
			squidblacklist(url,patternData)
            

main()