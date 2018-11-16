import re 
from bs4 import BeautifulSoup
import requests
import pickle

def squidblacklist(srcURL,regPat):
	source = requests.get(srcURL).text
	soup = BeautifulSoup(source,'lxml')
	match = soup.p.text

	test_str = match
	
	matches = re.finditer(regPat, test_str, re.MULTILINE)
	for matchNum, match in enumerate(matches):
		matchNum = matchNum + 1
		
		line = re.sub(regPat, r"\1", match.group())
		print(line)

	with open('bruteforceblocker.pkl', 'wb') as f:
		pickle.dump(line, f)
	return  



def main():
	squidblacklist()
	#regex = r"^(\d[^\t]+)[^\n]+"