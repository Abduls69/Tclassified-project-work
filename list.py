# List is a collection which is ordered and changeable. Allows duplicate

# Create list

ages = [2, 20, 6, 40, 50,89,3]

colours = ['red', 'yellow', 'blue', 'green', 'grey']

# Use a Constructor

ages2 = list ((10,20,35,40,50))

print(ages)
print(ages2)

# Get a value 
print(colours[2])

#Get length
print(len(colours))

# Append to list
colours.append('white')
colours.append('black')
print(colours)

#Remove from list
colours.remove('blue')
print(colours)

# Insert into a position
colours.insert(3, 'blue')
print(colours)

#Change a value 
colours[1] = 'pink'
print(colours)

#Remove with pop
colours.pop(2)
print(colours)

#Reverse List
colours.reverse()
print(colours)

#Sort List
colours.sort()
print(colours)
ages.sort()

print(ages)

# Reverse Sort
ages.sort(reverse=True)
print(ages) 

