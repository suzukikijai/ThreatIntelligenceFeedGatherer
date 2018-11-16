import re 
from bs4 import BeautifulSoup
import requests
import pickle

def squidblacklist():
	source = requests.get('http://danger.rulez.sk/projects/bruteforceblocker/blist.php').text
	soup = BeautifulSoup(source,'lxml')
	match = soup.p.text
	regex = r"^(\d[^\t]+)[^\n]+"

	test_str = match
	
	matches = re.finditer(regex, test_str, re.MULTILINE)
	for matchNum, match in enumerate(matches):
		matchNum = matchNum + 1
		
		line = re.sub(r"^(\d[^\t]+)[^\n]+", r"\1", match.group())
		print(line)

	with open('bruteforceblocker.pkl', 'wb') as f:
		pickle.dump(line, f)
	return  