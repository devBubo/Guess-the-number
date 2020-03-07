from random import randint
n=randint(1,100)
tries=0
try:
    user_input = int(input('Enter your guess: '))
    while True:


        if user_input==n:
            print('You won')
            print('You took',tries,'tries')
            break
        elif user_input<n and tries<5 :
            print('You are too low')
            user_input = int(input('Enter your guess: '))
            tries+=1

        elif user_input>n and tries<5:
            print('You are too high')
            user_input = int(input('Enter your guess: '))
            tries+=1
        elif tries==5:
            print('You lost')
            break
except:
    pass
