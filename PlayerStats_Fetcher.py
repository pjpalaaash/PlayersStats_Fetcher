from os import link
import pandas
from pandas.io import html
import requests
import pandas as pd
from bs4 import BeautifulSoup
import html5lib
import os

player = input("Enter Player Name: ").split()
format = input("Enter Format Name: ")
p = "+".join(player)

i = 0
if format == 'ipl':
    format = "twenty20"


f = format.upper()

if f == 'TEST':
    f = 'Test'
      


url = "http://www.cricmetric.com/playerstats.py?player="+p+"&role=all&format="+f+"&groupby=year&start_date=2002-01-01&end_date=2021-05-17&start_over=0&end_over=9999"
print(url)

htmls = requests.get(url).content

df_list = pd.read_html(htmls)
try:
    df = df_list[i]
    print(df)
    
    df.to_csv("Stats.csv")
    


except IndexError:
    print(f"{format} Record Not available")    



