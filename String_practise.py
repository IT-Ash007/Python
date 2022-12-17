mystr="this is an example of String"
print("length is",len(mystr))
print(mystr[0:4])
print(mystr[2])
print(mystr[0:4:2]) #0 to 4 taken after gap of 2 char
print(mystr[::]) #print full string
print(mystr[::-1]) #print full string in reverse
#functions
print(mystr.isalnum()) 
print(mystr.isalpha()) 
print(mystr.isnumeric())
print(mystr.endswith("e"))
print(mystr.count("i"))
print(mystr.find("is"))
print(mystr.upper())
print(mystr.lower())
print(mystr.capitalize())
print(mystr.replace("is","are"))


