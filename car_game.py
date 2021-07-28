started=False
v=""
while True:
    v=input('>').lower()
    if v=='help':
        print('''
start - to start the car
stop - to stop the car
quit - to exit
        ''')
    elif v=='start':
        
        if started:
            print('the car already started ')
            
        else:
            print('the car started')
            started=True

    elif v=='stop':
        if not started:
            print('the car has already stopped')
            
        else:
            print('the car stopped')
            started=False
        
    elif v=='quit':
        break
    else:
        print('I dont understand')