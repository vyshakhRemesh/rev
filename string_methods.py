course='Python for Beginners'
print(len(course))
#len and print are genral purpose functions
#because they are not only used for strings but other types also
print(course.upper()) #this doesnot modify original string, it returns a new string

#when a function is specific to somekind of object we reffer to them as methods
#here upper is a method specific to strings
print(course)

print(course.lower())

print(course.find('P')) #return index of capital p
print(course.find('for')) #return starting index of for
print(course.find('m')) #will return -1 because there is no m
print(course.replace('Beginners','Pros')) #will replace both
#find and replace are case sensitive

print('Python' in course) #produces a boolean value