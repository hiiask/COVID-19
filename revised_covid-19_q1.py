import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv
import matplotlib.pyplot  as plt
import os

def HIGH_RISK_TRAVEL_AREA(m):
    
    url="https://github.com/datasets/covid-19/blob/master/data/countries-aggregated.csv"
    r=requests.get(url)

    soup = BeautifulSoup(r.content, 'html5lib')
    file="covid_global.csv"
  
    with open(file, 'w') as f:
        writer = csv.writer(f,delimiter=',',quoting=csv.QUOTE_NONE, escapechar=' ' )
        for mytable in soup.find_all('table'):
            for trs in mytable.find_all('tr'):
            
                tds = trs.find_all('td')
                row = [elem.text.strip() for elem in tds]
                
                writer.writerow(row)
   
    c=1
    df=pd.read_csv('covid_global.csv',delimiter=",",sep='\t',error_bad_lines=False,index_col=0)
    
    print(df)
    
    path="offline.csv"
    mf=pd.read_csv(path,error_bad_lines=False)
    dead=int(input("Enter the death rate you want to select as a parameter "))
    
    print("Top 30 countries of given death rate ")
    
    newdf=mf.loc[mf['death']/mf['confirm']>(dead/100)]    
    print(newdf.country.drop_duplicates().head(30))
    print("The graph of COVID-19 for places you would like to study. \n")
# for parsing  the whole data i think
    lis=["Israel ","US ","France ","Italy ","Ukraine ","Indonesia ","India ","China "]
    for co in lis:
        mdf=df.loc[df['Country ']==co]
        fig = plt.figure(figsize = (150,5))
        plt.plot(mdf['Date '],mdf['Deaths'])
        plt.xlabel('Time(date)')
        plt.ylabel('deaths')
        plt.show()
        print("Graph of death rate :",co,"\n")
        
        
        
        
        
"""" Driver Code"""  
print("Death data for COVID-19")
os.chdir("D:\\COVID 19 Hackthon")
print("This code may take some time to run due to online connectivity")
HIGH_RISK_TRAVEL_AREA(1)








