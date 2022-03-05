import requests
from bs4 import BeautifulSoup

url="https://motorsportstats.com/series/motogp/calendar/2022"
input=requests.get(url).text

soup=BeautifulSoup(input,"html.parser")

#print(soup.table.tbody.tr.td[1])

table=soup.find_all("table")

races=[]
racesdic={}
for tb in table:
   tbody=tb.findAll("tbody")[0]
   rows=tbody.findAll("tr")
   for row in rows:
       racetime=row.findAll("td")[1].text
       #print(racetime, end=" ")
       racenametd=row.findAll("td")[2]
       for child in racenametd:
           rname=child.findAll("a")[0].text
           #print(rname)
           racesdic[racetime]=rname
           #print("--------------------------------")
print(racesdic)
#print(races)
