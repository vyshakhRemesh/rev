#tuple

thistuple = ("apple", "banana", "cherry")
print(thistuple)

#access

thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

#update

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

#join

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

#unpack

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)
