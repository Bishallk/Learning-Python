
#------------------DESERIALIZATION--------|
#* Process of converting json to python data type

#*Eg. Conveting json to Dict
import json

with open('FileHandling/dict.json','r') as f:
    d=json.load(f)
    print(d)  #{'name': 'bishal', 'age': '23', 'gender': 'male'}
    print(type(d)) #dict