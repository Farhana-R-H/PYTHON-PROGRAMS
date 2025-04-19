#EXPENSE TRACKER
exptracker={}
wallet=1000
while(True):
    print("menu")
    print("1.Add expense \n 2.Add balance \n 3.View balance \n 4.Exit")
    option=int(input("enter the option"))
    if option==1:
        expname=input("enter the expense name:")
        if expname in exptracker:
         amount1=int(input("enter the amount1:"))
         amount=exptracker[amount]+amount1
         exptracker.update({expname:amount1})
         wallet=wallet-amount1
         print(wallet)
         print(exptracker)
        else:
            amount=int(input("enter the amount"))
            if amount>wallet:
               print("unsufficient balance")
               print("current balance",wallet)
            else:
               exptracker.update({expname:amount})
               wallet=wallet-amount
               print(exptracker)
               print("balance is:",wallet)
    elif option==2:
            newbalance=int(input("enter new balance"))
            wallet=wallet+newbalance
            print(wallet)
    elif option==3:
        print("total expenses:",exptracker)
    else:
       exit()    
                                 




