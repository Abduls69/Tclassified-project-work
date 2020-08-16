# A loop is used for iterating over a sequnce (that is either a list, a tuple, a dictionary, a set, or a string).

students = ['Fortune', 'Abdul', 'Odinaka', 'Amos', 'Ibrahim', 'Zainab']


# Simple for loop

for student in students:
    print(f'I am: {student}')

# Break

for student in students:
    if student == 'Odinaka':
        break
    print(f'the student is: {student}') 

# Continue

for student in students:
    if student == 'odinaka':
        continue
    print(f'the people included: {students}') 

# range

for person in range(len(students)):
    print(f'Number: {person}')

# custom range

for n in range(0, 12):
    print(f'Number: {n}')


# While loop execute a set of statements as long as a condition is true

count = 0
while count < 10:
    print(f'count: {count}')
    count += 1 

