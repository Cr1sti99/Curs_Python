from decimal import Decimal
name='Cristi'
print(name)

if name=='Cris  ti':
    print("da")
else:
    print("Nu")

names=['Ana', 'Maria', 'Cristi', 'dddd']

keyword='Elena'

if keyword not in names:
    print(f'{keyword} was not found')

if not(4<2):
    print('Salut')



d1={1:'Salut'}
d2=d1

print((d1 is d2))

print(chr(97))
print(ord('A'))

print('Salut \nCristi')

print(r'Salut \n Cristi ')
price=Decimal(49)
print(f'for only{price:.2f}dollars! {name} have a nice day')

print(name)

# strings are immutable!!
name='CCCC'
print(name)

my_list= list()
my_list_2=[]

print(len(names))
print(names[2])
names[1]='Dan'
print(names)


print(names[-3:])
print(names[-3])
print(names[:-1])
#names.sort()
print(sorted(names))
print(names)


names=['Ana', 'Maria', 'Cristi', 'dddd', 'Ana']
print(names)
set_names=set(names)
print(set_names)
print(names)

new_names=['dddd','Ana']
set_new_names=set(new_names)
print(set_new_names.issubset(set_names))

new_list=list(set_new_names)
print(new_list)

unique_list=[]
for name in names:
    if name not in unique_list:
        unique_list.append(name)
print(unique_list)

print(list(set(names)))

all_words={
    'vacanta':['www.ggg.ro', 'www.rrr.ro'],
    'grecia':['www.rrr.ro', 'www.grecia.ro']
}

person={'first_name':'Dan',
        'last_name':'BBB',
        'age': 25}


print(person['age'])
print(person.get('ages'))

days_of_week=('Luni', 'Marti')
print(days_of_week)

child_age=3
print(id(child_age))

d1={1:'Salut'}
d2=d1

print((d1))