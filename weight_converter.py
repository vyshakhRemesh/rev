weight=int(input('enter the weight'))
unit=input('enter L(bs) or K(g)')
u=unit.lower()
if u=='l':
    print(f'your weight is{round(weight/2.205)} Kilos')
elif u=='k':
    print(f'your weight is{round(weight*2.205)} Pounds')
else:
    print('invalid input')