#set
thisset = {"apple", "banana", "cherry"}
print(thisset)

#access

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

#remove

thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)

#boolean

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
