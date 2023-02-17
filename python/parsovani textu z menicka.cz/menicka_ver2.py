import requests
from bs4 import BeautifulSoup as soup
import os
import datetime
import json
import re

now = datetime.datetime.now()
date = now.strftime("%Y-%m-%d")
url = 'https://www.menicka.cz/4550-bufacek-na-ruzku.html'
menickaFinal = []

# Make the request to the website
response = requests.get(url)  ##print(response.text)

# Parse the HTML of the website
def parseHtml(input):
  return soup(input.text, "html.parser")

page = parseHtml(response)
menicka = page.select('.menicka')

# go through all items and build dictionary for each day
for menicko in menicka:  
  polevky = []
  jidla = []
  nadpis = menicko.select('.nadpis')[0].text
  tempObj = {}  

  for polevka in  menicko.select('.polevka .polozka'):
    polevkaFormatted = re.sub("^0,( )?[0-9]{1,2}l ", "", polevka.text)
    polevky.append(polevkaFormatted)

  for jidlo in menicko.select('.jidlo .polozka'):
    jidloFormatted = re.sub("[0-9]{2,3}g ", "", jidlo.text)
    jidla.append(jidloFormatted)
  
  if nadpis != '' and (len(polevky) > 0 or len(jidla) > 0):
    tempObj.update({'datum' : nadpis.split(' ')[1]})
    tempObj.update({'polevky' : polevky})
    tempObj.update({'jidla' : jidla})
    print(tempObj)
    menickaFinal.append(tempObj)

print('\n*** final list of dicts:')
print(menickaFinal) 

'''
print('\n*** search for second meal from 19.1.2023:')
search = next(item['jidla'][1] for item in menickaFinal if item['datum'] == '19.1.2023')
print(search)
'''

# Save result to file
folder = 'menicka.cz/Bufacek na ruzku'
fileName = date + '.txt'
os.makedirs(folder, exist_ok=True)
with open(folder + '/' + fileName, "w", encoding="utf-8") as file:
  file.write(str(menickaFinal))

print('\n*** final json:')
print(json.dumps(str(menickaFinal), ensure_ascii=False)) ## .replace('[','{',1).replace(']','}',-1)
