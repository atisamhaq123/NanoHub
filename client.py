import requests
import time
import flask
from fastapi import FastAPI
import yaml

def main():
    print("Accessing post on: http://127.0.0.1:8000/cars ....\n...")    
    url='http://127.0.0.1:8000/cars'
    response=requests.get(url)
    z=response.json()
    #print(z)
    item=z['Cars']
    print(item,"\n\nid   name  color\tdescription")
    count=0
    for i in item:
        data=item[count]
        id=data["car_id"]
        name=data['name']
        color=data['color']
        description=data['description']
        print(id," ",name," ",color," ",description)
        count+=1
main()
