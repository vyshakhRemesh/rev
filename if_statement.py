is_hot = False
is_cold = True

if is_hot:
    print("It's a hot day")
    print("print plenty of water")
elif is_cold:
    print("it's a cold day")
    print("wear warm cloths")
else:
    print("it's a lovely day")
print('enjoy your day')


price=1000000
has_good_credit=True
if has_good_credit:
    down_payment=0.1*price
else:
    down_payment=0.2*price
print(f"downpayment is ${down_payment}")