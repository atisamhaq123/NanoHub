import requests
import time
import flask




print("Starting Microservices now....\n")
time.sleep(1)
###


from fastapi import FastAPI
import yaml

app = FastAPI()  # creating instance of FastAPI

# list of data (i.e cars)
#cars = [
  #  {
   #     "car_id": 1,
    #    "name": "mango",
     #   "color": "Red",
     #   "description": "High speed vehicle" 
   # },
    #{
     #   "car_id": 2,
      #  "name": "Tesla",
      #  "color": "Blue",
       # "description": 'Self driving car'}]

with open(r'swagger.yaml') as file:
    cars=yaml.load(file,Loader=yaml.FullLoader)
    

 
 
@app.get("/")
def welcome():
    return {"Welcome To": "Cars Microservice "}


# returns all Car list
@app.get("/cars")
def all_cars():
    return {"Cars": cars}


# finds fruit by car_id
@app.get("/find/car/{car_id}")
def find_fruit(car_id: int):
    queried_car_id = car_id
    for car in cars:
        exist_car_id = car.get('car_id')
        if exist_car_id == queried_car_id:
            return {"Result": car}
    return {"Result": "Car is Not Available"}







def version1():
    payload={'username':'corey','password':'testing'}
    #Api link Address
    r=requests.post('https://httpbin.org/post',data=payload)
    
    z=r.json()
    print("Url: ",z['url'])
    print("Ip address is: ",z['origin'])
    i=z['form']
    print("<<Username>>: ",i['username'])
    print("<<Password>>: ",i['password'])
    print("Version: 1.0","\n")

def version2():
    #Api link Address
    url = 'https://jsonplaceholder.typicode.com/todos/1' 
    response = requests.get(url)        # To execute get request 
    # To print http response code  
    z=response.json()
    print("<<Userid>>: ",z["userId"])
    print("<<title>>: ",z["title"])
    print("<<Id>>: ",z["id"])
    print("<<status>>",z["completed"])
    print("Version: 2.0","\n")
    
def onnet():
    print("Accessing post on: https://httpbin.org/post ....\n...")
    time.sleep(2)
    version1()
    time.sleep(2)
    print("Accessing post on: https://jsonplaceholder.typicode.com/todos/1 ....\n...")
    version2()


def main():
    print("Accessing post on: http://127.0.0.1:8000/cars ....\n...")    
    url='http://127.0.0.1:8000/cars'
    response=requests.get(url)
    z=response.json()
    #print(z)
    item=z['Cars']
    print(item[1])
    count=0
    for i in item:
        data=item[count]
        id=data["car_id"]
        name=data['name']
        print(id," ",name)
        count+=1


    



















