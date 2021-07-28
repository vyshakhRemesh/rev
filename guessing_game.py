secret_no=5
i=0
guess_limit=3
while i<guess_limit:
    guess=int(input('guess:'))
    i+=1
    if guess==secret_no:
        print('you won')
        break #immediately terminate the loop
    
else:  #in python we can have a else part for the while loop which will execute it the while loop is completed successfully
    print('gameover')