# If/Else conditions are used to decide something based on a condition being true or false

age_casmir = 17
age_abdul = 16

# Comparism operators(==, |=, >, <, >=, <=) - Used to compare values

# Simple if

if age_casmir > age_abdul:
    print(f'{age_casmir} is greater than {age_abdul}')

# If/Else

if age_casmir > age_abdul:
   print(f'{age_casmir} is greater than {age_abdul}')
else:
    print(f'{age_abdul} is geater than {age_casmir}')

# elif

if age_casmir > age_abdul:
    print(f'{age_casmir} is greater than {age_abdul}')
elif age_casmir == age_abdul:
    print(f'{age_casmir}is equal to {age_abdul}')
else:
    print(f'{age_abdul} is greater than {age_casmir}')

 # Nested if

if age_casmir >= 10:
      if age_casmir <= 20:
         print(f'{age_casmir} is greater than 10 and less than or equl to 20')

#logical operators ( and, or,not) - uesd to combine conditional statements

# and
if age_casmir > 10 and age_casmir <= 20:
    print(f'{age_casmir} is greater than 10 and less than or equl to 20')

# Or 
if age_casmir > 10 and age_casmir <= 20:
    print(f'{age_casmir} is greater than 10 or less than or equl to 20')

# not
if not(age_casmir == age_abdul):
    print(f'{age_casmir} is not equal to {age_abdul}')

# Membership Operators( not, not in) =Membership operators are used to test if a sequence is present in an object

ages = [19, 20, 20, 18, 19, 20]

# in
if age_casmir in ages:
    print(age_casmir in ages)

#not in
if age_casmir not in ages:
    print(age_casmir not in ages)

# idenity operators (is, is not) - compare the objects, not if they are equal, but if they are equally the same type of object,with the same memory location

# is 
if age_casmir is age_abdul:
    print(age_casmir is age_abdul)

# is not
if age_casmir is not age_abdul:
    print(age_casmir is not age_abdul) 


