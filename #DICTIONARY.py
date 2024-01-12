#DICTIONARY 
#Create dict
person={
    'first_name':'jhon',
    'last_name':'wick',
    'age'  : 30
} 
 
print(person,type(person)) 
#USE CONSTRUCTOR
person2=dict(first_name='Brad',last_name='pitt')
print(person2)
#GET VALUE
print(person2['first_name'])
print(person2.get('last_name'))
#ADD KEYVALUE
person['phone']='555-777-989'
print(person)
#GET DICTIONARY KEY ITEMS
print(person.keys())
#COPY DICT
person2=person.copy()
person2['city']='Boston'
print(person2)
#REMOVE ITEMS
del (person2['age'])
person2.pop('phone')
print(person2)
#CLEAR
# person.clear()
#GET LENGTH
print(len(person))
#LIST OF DICT
people=[
       {'name':'Martha','age': 35},
       {'name':'neo','age': 28}
]
print(people[0]['age'])