# Dictionaries

# Create
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 20
}
person2 = dict(first_name='Sara', last_name='Williams')

print(person, type(person))
print(person2)

# Get value
print(person['first_name'])
print(person.get('last_name'))

# Add
person['phone'] = '555-555-55'
print(person)

# Get keys
print(person.keys())

# Get items
print(person.items())

# Copy
person2 = person.copy()

person2['city'] = 'Boston'
print(person2)

# Remove
del(person['age'])
person.pop('phone')

# Clear
person.clear()

# Get length
print(len(person2))

print(person)

# List of dicts
people = [{'name': 'Martha', 'age': 30}, {'name': 'Kevin', 'age': 25}]
print(people)
print(people[0]['name'])
