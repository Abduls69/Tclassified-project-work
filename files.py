# Python has functions for creating. reading, updating and deleting files 

# Open a file

hussainifile = open('abdul.txt', 'w')

# Get Information

print('Name: ', hussainifile.name)
print('Is closed: ', hussainifile.closed)
print("Opening Mode: ", hussainifile.mode)

# Write to file
hussainifile.write('onimisi is my igbira name')
hussainifile.write(' I am from Kogi')
hussainifile.close()

# Append to file
hussainifile = open('abdul.txt', 'a')
hussainifile.write("i also live in Abuja Nigeria and i love python")
hussainifile.close()

# Read from file

ekenefile = open('abdul.txt', 'r+')
text = ekenefile.read(100)
print(text)