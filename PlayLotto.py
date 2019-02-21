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
#------------Program Begins-------------------
print('You are 18 years old')
print('If you played the Powerball every week,\n\twould you be able to win?')
print('\nTo make life easy choose your lucky numbers now.')
print('You can only choose a number between 1-69')
numbers.append(int(input('1. :')))
numbers.append(int(input('2. :')))
numbers.append(int(input('3. :')))
numbers.append(int(input('4. :')))
numbers.append(int(input('5. :')))
print('Dope')
print(f'Your numbers are {numbers[0]} {numbers[1]} {numbers[2]} {numbers[3]} {numbers[4]}')
print('\nNow pick a powerball 1-26')
powerball=input('\nPowerball:')
input('Hit "enter" to start the simulation')
while week>0 and lotto==0:
    week-=1
    wNumbers.append(random.randint(1,69))
    wNumbers.append(random.randint(1,69))
    wNumbers.append(random.randint(1,69))
    wNumbers.append(random.randint(1,69))
    wNumbers.append(random.randint(1,69))
    wNumbers.append(random.randint(1,26))
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
        print(f'It took you {age}years and *variable*Dollars')
else:
    print('After playing 3,224 games and spending $6,448 you never won the lottery......')