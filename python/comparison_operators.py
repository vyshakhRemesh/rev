temperature=30
humidity=50
day='yes'

if temperature>30:
    print('it is a hot day')
else:
    print("it is not a hot day")

if humidity==20:
    print("low humidity")
elif humidity<=50:
    print("medium humidity")
else:
    print('high humidity')

if day!='yes':
    print('night')
else:
    print("day")
