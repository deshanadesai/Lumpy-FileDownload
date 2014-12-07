import requests
import re
from bs4 import BeautifulSoup
import urllib

url = raw_input("\nHI. Please paste your url here.\n\n")

format = raw_input("\n\nThe format of files you'd like to download: ")
print '\n\n'
req = requests.get(url)


html_doc = req.text.encode("utf-8")
soup = BeautifulSoup(html_doc)

pattern = "\."+format+"$"
links = soup.findAll(href=re.compile(pattern))

for link in links:
	filename = link.get_text()
        try:
                urllib.urlretrieve(url+filename,filename)
                print "Downloaded file: "+filename
        except:
                print "File already in directory: "+filename
	

print '\n\nDOWNLOAD COMPLETE'

