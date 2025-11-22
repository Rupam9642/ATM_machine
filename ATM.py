
#Atm machine
import time

print("welcome")

print("please insert your card:")
time.sleep(2)

password=int(input("enter your atm pin:"))

balance=5000

if password==1234:
    
        print("1==balance amount")
        print("2==withdraw balance")
        print("3==deposit balance")
        print("4==exit")
while True:
    try:
        option=int(input("please enter your choice:"))
        break

    except:
        print("please enter valid option:")
        print("===============================================")

        ##check current balance amount
    
if option ==1:
                print(f"your current balance is {balance}")
                print("===============================================")

##check withdrawal amount
                
elif option ==2:
        withdraw_amount=int(input("please enter your withdraw_amount"))
        balance=balance-withdraw_amount
        print(f"{withdraw_amount} is debited from your account")
        print(f"your current balance is {balance}")
        print("===============================================")

        print(f"your current balance is{balance}")
#check the deposit amount

elif option ==3:
        deposit_amount=int(input("please enter your deposit_amount"))
        balance=balance+deposit_amount
        print(f"{deposit_amount} is credited to your account")
        print(f"your current balance is {balance}")
        print("===============================================")


elif option ==4:

        print("exit")
        print("===============================================")

        print("thank you:")
        print("===============================================")

else:
        print("invalid option")
        print("===============================================")
          
                
        print("wrong pin please try again")




