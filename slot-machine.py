import random
import sys

# The keys below act as multiplier as well as keys with the help of which we displat the given alphabets
slot_options={
    2:"W",
    3:"X",
    4:"Y",
    5:"Z"
}

# It's a 3x3 slot-machine
slots=[
    [0,0,0], [0,0,0], [0,0,0]
]

def isWantingToQuit(balance):
    res=input(f"Enter 'exit' to quit. Your balance is {balance}.\n")
    if res=='exit': sys.exit('Game Over')

def checkBalance(linesAmount, balance):
    if(linesAmount>balance): sys.exit('Insufficient Balance:( Play Again!')

def takeDeposit():
    while True:
        try:
            amount=int(input('Enter the amount you want to deposit before playing: '))
            if amount<=0: print('Enter a positive amount!')
            else: break;
        except:
             print("Please enter a valid amount!")
    
    return amount;
    


def fill_slots(slots):
    for row in slots:
        j=0
        for i in range(3):
            value=random.randint(min(slot_options.keys()),max(slot_options.keys()))
            row[i]=slot_options[value];


def takeLines(balance):
    while True:
        try:
            amount=int(input(f'Enter the amount you want to bet per line. Your balance is {balance}: '))
            if amount>balance or amount<1: 
                print(f"Enter a valid amount. Your balance is {balance}")
                continue;

            global lines
            lines=0
            while lines<1 or lines>3: 
                lines=int(input('Enter the number of lines you want to bet on (1-3): '))
                if lines<1 or lines>3: print('Enter a number in the range of 1 to 3!')
            break;

        except:
            print("Please enter a valid number!")
        
        finally:
            if(lines*amount>balance): sys.exit('Insufficient Balance:( Play Again!')   
            print(f"You are betting {amount} on {lines} lines. Total amount at stake is: {amount*lines}") 
    
    return amount*lines;

def findMultiplier(slot_options,ele):
    key_list = list(slot_options.keys())
    val_list = list(slot_options.values())

    position = val_list.index(ele)
    return(key_list[position])
            
    

def checkIfEqual(slots):
    ans=list([])
    line_no=1
    for lst in slots:
        ele=lst[0]
        chk = True
        
        # Comparing each element with first item 
        for num,item in enumerate(lst):
            if ele != item:
                chk = False
                break;
                
        if (chk == True): 
            ans.append((line_no,findMultiplier(slot_options,ele)))
            
        line_no+=1;
    
    return ans;

def finalResult(linesAmount, balance, data):
    amount_per_line=linesAmount/lines
    linesWon=list([])
    multiplier=list([])
    winnings=0

    if not len(data):
        print('You won 0')
        balance-=linesAmount
        print(f"Current balance: {balance}")
    else:
        for tup in data:
            linesWon.append(str(tup[0]))
            multiplier.append(tup[1])
        
        for el in multiplier:
            winnings+=(el*amount_per_line)
        
        balance=balance-linesAmount+winnings

        print('You won on line number: ', ",".join(linesWon))
        print('You won: ', winnings)
        print(f"Current balance: {balance}")


    if not balance : 
        if(linesAmount>balance): 
            sys.exit('Insufficient Balance:( Play Again!') 
    
    return balance;


def printSlots(slots):
    for i in range(len(slots)):
        for j in range(len(slots[0])):            
            if j != len(slots) - 1:
                print(slots[i][j], end=" | ")
            else:
                print(slots[i][j], end="")

        print()


# Beginning of the program:
balance=takeDeposit()
while True:
    isWantingToQuit(balance)
    linesAmount=takeLines(balance)
    fill_slots(slots)
    data=checkIfEqual(slots);
    printSlots(slots);
    # print(slots)
    balance=finalResult(linesAmount, balance, data)
