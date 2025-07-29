import requests 
import json



def getsportdata():
    url = 'https://www.thesportsdb.com/api/v1/json/3/searchteams.php?t=Arsenal'

    response = requests.get(url)

    if response.status_code == 200:
        print(response.json())
        
        
    else:
        print("Error")
    
getsportdata() 