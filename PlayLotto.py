#MQ



import random

#------------Variable Dictionary--------------
age=18          #age of the user
lotto=0         #0=false 1=true 
week=3224       #Weeks in 62 years if you stop playing at 80years old
numbers=[]      #List holding the user chosen numbers
powerball=0     #User chosen powerball number
wNumbers=[]     #List holds the Winning numbers
price=0         #How much money spent on playing the powerball
#------------Functions------------------------
def intro():
    print('You are 18 years old')
    print('If you played the Powerball every week,\n\twould you be able to win?')
    print('\nTo make life easy choose your lucky numbers now.')
    print('You can only choose a number between 1-69')
    numbers.append(int(input('1. :')))
    numbers.append(int(input('2. :')))
    numbers.append(int(input('3. :')))
    numbers.append(int(input('4. :')))
    numbers.append(int(input('5. :')))
    return numbers

def menu():
    print('1.) Can I win the Powerball in my lifetime')
    print('2.) How long would it take to win?')
    choice=0
    while choice!=1 and choice!=2:
        choice=int(input('\n1 or 2 :'))
    return choice

def winningNumbers():
    wNumbers.append(random.randint(1,69))
    wNumbers.append(random.randint(1,69))
    wNumbers.append(random.randint(1,69))
    wNumbers.append(random.randint(1,69))
    wNumbers.append(random.randint(1,69))
    wNumbers.append(random.randint(1,26))
    return wNumbers
#------------Program Begins-------------------

numbers=intro()
print('Dope')
print(f'Your numbers are {numbers[0]} {numbers[1]} {numbers[2]} {numbers[3]} {numbers[4]}')
print('\nNow pick a powerball 1-26')
powerball=input('\nPowerball:')
choice=menu()
if choice==1:

    input('Hit "enter" to start the simulation')
    while week>0 and lotto==0:
        week-=1
        wNumbers=winningNumbers()
        price+=2
        win=0
        for i in range(0,5):
            if numbers[i]==wNumbers[i]:
                win+=1
        if win==5:
            lotto=1
    if lotto==1:
        if powerball==wNumbers[5]:
            age=round(18+((3224-weeks)/52))
            print(f'You Won the grand prize of $345 Million')
            print(f'It took you {age}years and ${price}Dollars')
    else:
        print(f'After playing 3,224 games and spending ${price} you never won the lottery......')
else:
    week=0
    while lotto==0:
        win=0
        week+=1
        price+=2
        wNumbers=winningNumbers()
        for i in range(0,5):
            if numbers[i]==wNumbers[i]:
                win+=1
        if win==5:
            lotto=1
    if lotto==1:
        if powerball==wNumbers[5]:
            age=float(18+(weeks/52))
            print(f'You Won the grand prize of $345 Million')
            print(f'It took you {age:.2}years and ${price}Dollars')