# -*- coding: utf-8 -*-
"""
Written by: Artur Arakelyan and Patrick Bowden

We came up with this version after the first attempt to better match what the assignment wanted done, and to improve speed.
"""
#imports
import os.path
import bs4 as BS     
import urllib.request as rq
import csv
import sys
import pickle
import urllib.parse as parse
import re

#home url
home='https://www.cia.gov/Library/publications/the-world-factbook/the-world-factbook'

#checking or creating the data directory
if not os.path.exists('data'):
    os.mkdir('data')
else:
    pass

#opening reading and pickling the website
if not os.path.isfile('data/site.pickle'):
    try:
        with rq.urlopen('https://www.cia.gov/library/publications/the-world-factbook/print/textversion.html') as page:
            html= page.read()
            pickle.dump(html,open("data/site.pickle","wb"))   
            
    except:
        print("Something went wrong with pickling.")
        sys.exit(1) 
        
else:
    html = pickle.load(open('data/site.pickle','rb'))

#creating initial csv file
with open('data/cia.csv','w') as fileout:
    writer = csv.writer(fileout,delimiter=',',quotechar='"')
    writer.writerow(['CountryCode', 'Area(sq km)', 'GDP(USD)', 'Roads(km)', 'Railways(km)'])

#function to grab data from sites (work in progress)
def grab(k):
    #print(k)
    with rq.urlopen(k) as page:
        page=page.read()
        broth=BS.BeautifulSoup(page,'lxml')
        temp=broth.get_text()
        
        #Area
        a1 = temp.find("Area:")
        if a1 == -1:
            af=0
            pass
        else:
            a2 = temp.find("sq km")
            a3 = temp[a1+13:a2]
            af = re.sub('[^0-9,.]', '', a3)
        
        #GPD
        g1 = temp.find("GDP - per capita (PPP):")
        if g1 == -1:
            gf =0
            pass
        else:
            g2 = temp[g1+25:g1+32]
            gf = re.sub('[^0-9,.]', '', g2)

        #Roadways
        rw1 = temp.find("Roadways:")
        if rw1 == -1:
            rwf = 0
            pass
        else:    
            rw2 =temp[rw1+17:rw1+27]
            rwf = re.sub('[^0-9,.]', '', rw2)

        #Railroads
        rr1 = temp.find("Railways:")
        if rr1 == -1:
            rrf = 0
            pass
        else:
            rr2 = temp[rr1+17:rr1+27]
            rrf = re.sub('[^0-9,.]', '', rr2)
        
        
    with open('data/cia.csv','a') as fileout:
        writer = csv.writer(fileout,delimiter=',',quotechar='"')
        writer.writerow([k[-7:-5],af,gf,rwf,rrf])
    

#gathering links
soup=BS.BeautifulSoup(html,'lxml')
links = soup.find('div',{'id':'demo'})

for a in links.find_all('a',href=True):
    mergedUrl=parse.urljoin(home+'/the-world-factbook',a['href'],allow_fragments=True)
    grab(mergedUrl)

  
print('Done')