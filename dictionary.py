# A Dictionary is acollection which is unodered, changeable and it is indexed. No duplicate members.

# Create Dictionary

person_detail = {
    'first_name': 'Augustine',
    'last_name': 'Emeka',
    'age': 30
    }

    # Use of constructor

person_detail = dict(first_name='Husseini', last_name='Suleiman',)
print(person_detail)

    # Get a value
print(person_detail['first_name'])

    # Add ket/value
person_detail['phone_number'] = '+2347067162698'
print(person_detail)
    # Get dictionary keys
print(person_detail.keys())

    # Get dictionary items
print(person_detail.items())

    #Copy dictionary
person_information = person_detail.copy()
print(person_information)
    # Remove item
del (person_detail['last_name'])
person_detail.pop('phone_number')
print(person_detail)

    #clear
person_detail.clear()
print(person_detail)

    # Get lenghth
print(len(person_detail))

    # Make a list of dictionaries
persons = [
        {'name': 'Augustine', 'age': 35, 'phone_number': '+234706717162698'},
        {'name': 'Fortune', 'age': 21, 'phone_number': '+234708391552'},
        {'name': 'Ola', 'age': 30, 'phone_number': '+234708391552'},
]

print(persons)


