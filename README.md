### Credit card transaction dataset containing legitimate and fraud transactions from the duration 1st Jan 2019 - 31st Dec 2020 : Fraud
## HNID Afef
M2 WEB HITEMA

## Machin Learning

 File : Project.ipynb
 

## Les routes
File : launch.py

path: "/prediction"
La route "/prediction" Apartir d'un ensemble de donnes on pourra prédir si on risque le fraud de notre card lors d'une transaction
  route='/prediction'
  url='http://127.0.0.1'+route
  param=params = {
    'input_amt': 24,
    'input_gender': 24,
    'input_state': 43,
    'input_city_pop':23,
    'input_numCardLength':15,
    'input_age':55
}
  r=requests.post(url,data=param)
  r.json()


## Docker
## build
 docker build -t fraud .
## container

 docker run -dit --name fraud_container -p 80:80 fraud
## pull

  docker pull nujabness/fraud:fakenews
  
## repository
  https://hub.docker.com/repository/docker/afefhnid/fraud
