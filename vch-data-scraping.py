import requests
from bs4 import BeautifulSoup

URL = 'http://www.vch.ca/covid-19/public-exposures'
page = requests.get(URL)
x=1
soup = BeautifulSoup(page.content,'html.parser')

recent_results = soup.find(id = '9184')
archive_results = soup.find(id = '5998')

print(recent_results.prettify())
print(archive_results.prettify())

filtered_recent_results = recent_results.find_all(text = True)
filtered_archive_results = archive_results.find_all(text=True)

"""
for result in filtered_recent_results:
    print(result)
"""

recentDiv = soup.find('div',id = 9184)
archiveDiv = soup.find('div',id = 5998)


recentSpan = recentDiv.find_all('span')
archiveSpan = archiveDiv.find_all('span')

"""
for span in mySpan:
    if (len(span.text)) != 0:
        print(span.text)
        print(x)
        x += 1
"""

for span in recentSpan:
    if 'color:#843275' in span['style']:
        print(span.text)
    if "Address:" in span.text:
        print(span.text)

        

        
# For archive list but for some reason an error appears
"""
for span in archiveSpan:
    if 'color:#843275' in span['style']:
        if (len(span.text)) != 0:
            print(span.text)
            print(x)
            x += 1
"""


    
  


