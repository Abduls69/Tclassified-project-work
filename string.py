# srings are collections of letters and numbers enclosed in a single or double qoute

name = 'Onimisi'

my_school = 'the name of my school is university of abuja'
print(my_school.capitalize())
print(my_school.lower())

my_name = 'Hussaini Abdulhaleem'
print(my_name.upper())
print(my_name.lower())
print(my_name.capitalize())

# concatination

print(my_school+my_name)

# string formatting

print(f' Hello, my name is (my_name)')

#swap case
print(my_name.swapcase())

#Get Length
print(len(my_name))

#Replace
print(my_name.replace('Hussaini','suleiman'))

#count
sub = 'a'
print(my_name.count(sub))

#Starts with
print(my_name.startswith('hussaini'))

#Ends with
print(my_name.endswith('m'))

#Split into list
print(my_name.split())

#Find position
print(name.find('n'))

# Is all alphanumeric
print(name.isalnum())

# Is all alphabetic
print(name.isalpha())

# Is all numeric
print(name.isnumeric())