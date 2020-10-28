import requests

BASE = "http://127.0.0.1:5000/"

data = [{"name": "koffiebonen", "price": '7.80'},
        {"name": "volle melk", "price": '1.52'},
        {"name": "suiker", "price": '0.98'},
        {"name": "chocolade", "price": '1.40'},
        {"name": "appels", "price": '1.20'},
        {"name": "brood", "price": '1.35'},
        {"name": "kipfilet", "price": '3.38'},
        {"name": "ijsberg sla", "price": '1.86'},
        {"name": "tomaten", "price": '1.56'}]

for i in range(len(data)):
    response = requests.put(BASE + "item/" + str(i), data[i])
    print(response.json())
input()
response = requests.delete(BASE + "item/5")
print(response)
input()


#response = requests.put(BASE + "item/1" , {"name": "koffiebonen", "price": 7})
response = requests.get(BASE + "item/6")
print(response.json())