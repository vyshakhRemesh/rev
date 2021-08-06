#numbers=[5,2,5,2,2]
#for i in numbers:
    #print('*'*i)

numbers=[5,2,5,2,2]
for i in numbers:
    output=''
    for j in range(i):
        output+='x'
    print(output)
print("")

num=[2,2,2,2,5]
for i in num:
    output=''
    for j in range(i):
        output+='x'
    print(output)


#total coast of all the items in the shopping cart

prices=[10,20,30]
total=0
for i in prices:
    total+=i
print(f"total:{total}")
