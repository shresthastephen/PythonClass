from bs4 import BeautifulSoup
import requests

document =requests.get('https://www.sharesansar.com/company/MLBBL#')

# with open ('in.html','r') as file:
#     content = file.read() 
#     soup=BeautifulSoup(content,'html.parser' )

#     table_data=soup.findAll('td')
#     print(table_data)