#MQ



import random

#------------Variable Dictionary--------------
age=18          #age of the user
lotto=0         #0=false 1=true 
week=3224       #Weeks in 62 years if you stop playing at 80years old
numbers=[0,0,0,0,0,0]      #List holding the user chosen numbers
wNumbers=[0,0,0,0,0,0]     #List holds the Winning numbers
price=0         #How much money spent on playing the powerball
match=0         #counts how many numbers match to win lotto
highestMatch=0    #counts the closest to 5 matches achieved
amtHighest=0    #counts the amount of times user hit the highestMatch
x=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64','65','66','67','68','69']
n=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26']
#------------Functions------------------------
def intro():
    print('\t ________________________________________________ ')
    print('\t|                                                |')
    print('\t|                                                |')
    print('\t|            Lottery Simulator                   |')
    print('\t|                                                |')
    print('\t|  By MQ                                         |')
    print('\t|                                                |')
    print('\t|________________________________________________|')
    input('Press "enter" to continue...')
    print('\n\tHave you ever seen someone win the lottery and think,"Well if I only bought ticket..."')
    print('\n\tThis simulator will let you virtually buy one ticket a week with your lucky numbers.')
    input('\nPress "enter" to continue...')
    print('\n\n\tThis simulator uses real Powerball rules.\n\tYou can not repeat numbers,')
    print('\tYou choose 5 numbers between 1-69. Then you choose the powerball number 1-26.')
    print('\tYou can not repeat any of the 5 regular numbers. The powerball number can match one of your 5 regular numbers.')
    print('\n\n\tEach ticket costs $2.00\n\tIf you match all five numbers you win $1 Million, If you also match the powerball number you win $324Million.\n')
    input('\nPress "enter" to pick your lucky numbers...')

def chosenNumbers():
    while numbers[0] not in x:#this checks the manually created list of numbers in string form to make sure the number chosen is within range
        numbers[0]=input('1. :')
    
    while numbers[1] not in x:
        numbers[1]=input('2. :')
        while numbers[1]==numbers[0]:#this second part will check that the user has not repeated any numbers
            numbers[1]=input('2. :')
    
    while numbers[2] not in x:
        numbers[2]=input('3. :')
        while numbers[2]==numbers[1] or numbers[2]==numbers[1]:
            numbers[2]=input('3. :')
    
    while numbers[3] not in x:
        numbers[3]=input('4. :')
        while numbers[3]==numbers[2] or numbers[3]==numbers[1] or numbers[3]==numbers[0]:
            numbers[3]=input('4. :')
    
    while numbers[4] not in x:
        numbers[4]=input('5. :')
        while numbers[4]==numbers[3] or numbers[4]==numbers[2] or numbers[4]==numbers[1] or numbers[4]==numbers[0]:
            numbers[4]=input('5. :')
    
    print('\nNow pick a powerball 1-26\n')
    while numbers[5] not in n:
        numbers[5]=input('Powerball. :')
    numbers[0]=int(numbers[0])
    numbers[1]=int(numbers[1])
    numbers[2]=int(numbers[2])
    numbers[3]=int(numbers[3])
    numbers[4]=int(numbers[4])
    numbers[5]=int(numbers[5])
    return numbers

def menu():
    print('1.) Can I win the Powerball in my lifetime')
    print('\t\tYou are 18 years old')
    print('\t\tIf you played the Powerball once every week until you were 80,\n\t\twould you be able to win?\n')
    print('2.) How long would it take to win? **Warning**This may take 2+ hours')
    print('\t\tSimulation ends when you win the lottery\n\t\tInfo displayed: Years spent, Money Spent, Amount of tickets purchased, and closest chance to winning')
    choice=0
    while choice!=1 and choice!=2:
        choice=int(input('\n1 or 2 :'))
    return choice

def winningNumbers():
    wNumbers[0]=(random.randint(1,69))
    wNumbers[1]=(random.randint(1,69))
    while wNumbers[1]==wNumbers[0]:
        wNumbers[1]=(random.randint(1,69))
    wNumbers[2]=(random.randint(1,69))
    while wNumbers[2]==wNumbers[1] or wNumbers[2]==wNumbers[0]:
        wNumbers[2]=(random.randint(1,69))
    wNumbers[3]=(random.randint(1,69))
    while wNumbers[3]==wNumbers[2] or wNumbers[3]==wNumbers[1] or wNumbers[3]==wNumbers[0]:
        wNumbers[3]=(random.randint(1,69))
    wNumbers[4]=(random.randint(1,69))
    while wNumbers[4]==wNumbers[3] or wNumbers[4]==wNumbers[2] or wNumbers[4]==wNumbers[1] or wNumbers[4]==wNumbers[0]:
        wNumbers[4]=(random.randint(1,69))
    wNumbers[5]=(random.randint(1,26))
    return wNumbers
#------------Program Begins-------------------

intro()
numbers=chosenNumbers()
print('Dope')
print(f'Your numbers are {numbers[0]} {numbers[1]} {numbers[2]} {numbers[3]} {numbers[4]} Powerball:{numbers[5]}')
choice=menu()
if choice==1:

    input('Hit "enter" to start the simulation...')
    while week>0 and lotto==0:
        week-=1
        wNumbers=winningNumbers()
        print(wNumbers)
        price+=2
        match=0
        for i in range(0,5):
            if numbers[i]==wNumbers[i]:
                match+=1
        if match==5:
            lotto=1
        else:
            if match>highestMatch:
                highestMatch=match
                amtHighest=1
            elif match==highestMatch:
                amtHighest+=1

    if lotto==1:
        if numbers[5]==wNumbers[5]:
            age=round(18+((3224-weeks)/52))
            print(f'You Won the grand prize of $345 Million')
            print(f'It took you {age}years and ${price}Dollars')
        else:
            print('You won but not the powerball...')
            print(f'You get 1 Million dollars and it only cost you {age} years and ${price} dollars')
    else:
        print(f'After playing 3,224 games and spending ${price} you never won the lottery......')
        print(f'The closest you came was {match}/5 on {amtHighest} tickets.')
else:
    week=0
    input('Hit "enter" to start the simulation...')
    while lotto!=1:
        match=0
        week+=1
        age=(18+(week/52))
        print(f'Year: {age:.2f}\tMoney Spent: ${price}\tClosest To Winning: {highestMatch}/5 on {amtHighest} out of {week} tickets purchased')
        price+=2
        wNumbers=winningNumbers()
        for i in range(0,5):
            if numbers[i]==wNumbers[i]:
                match+=1

        if match==5:
            lotto=1
        else:
            lotto=0
            if match>highestMatch:
                highestMatch=match
                amtHighest=1
            elif match==highestMatch:
                amtHighest+=1


    if lotto==1:
        if numbers[5]==wNumbers[5]:
            age=(18+(week/52))
            print(f'You won the grand prize of $345 Million')
            print(f'It took you {age}years and ${price}Dollars')
        else:
            print('You won 1 Million in the lottery')
            print(f'It took you, \nYears:{age}\nGames Played{week}\nMoney Spent:${price}')