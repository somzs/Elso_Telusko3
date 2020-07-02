''''data = {1:'Navin', 2:'Kiran',4:'Harsh'}
print(data)
print(data[4])
print(data.get(1))
print(data.get(3))
print(data.get(3,'Not found'))
keys = ['Navin', 'Kiran','Harsh']
values = ['Python','Java','JS']
data = dict(zip(keys,values))
print(data)
data['Monika'] = 'CS'
print(data['Monika'])
del data['Harsh']
x = data.keys()
print(x)
a = 10
print(id(a))
print(id(10))
k = 10
print(id(23)'''

4
x = input("Enter a value: ")
print(x)