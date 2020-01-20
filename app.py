print("Command Line Banking App")
press1=print("press 1 to create new account")
press2=print("press 2 for transaction")
option=int(input("do you want to open new account or carry out a transaction:"))
if option==1:
    print("create_account")
elif option==2:
    print("transaction")
else:
    print("")
if option==1:
    print("Create your bank account")
elif option==2:
    print("carryout your transaction")
else:
    print("")
    new_user = {'email':user_email.lower(), 'password':user_password, 'balance': 0.0}
    users.append(new_user)
email=str(input("Enter email address:"))
password=str(input("Enter your password:"))
phone_number=str(input("Enter your phone number:"))
print("successful")
login=print("login")
email=str(input("enter your email address:"))
password=(input("enter your password:"))
print('Welcome', email)
if password==password:
    print("successful login")
else:
    print("unsuccessful")    
transaction=int(input("Check_balance or Deposit_cash or Withdraw_cash:"))
if transaction==1:
    print("Check_balance")
elif transaction==2:
    print("Deposit_cash")
elif transaction==3:
    print("Withdraw_cash")
elif transaction==4:
    print("Transfer")       
else:
    print("") 

print("Deposit_cash")      
balance=0.00
deposit=int(input("Enter amount:"))
sum=int(balance+deposit)
print("sum is", sum)

print("Withdraw_cash")
amount=int(input("Enter amount:"))
sum=int(balance+deposit)
new_balance=int(sum-amount)
print("new_balance is", new_balance)

print("Check Balance")
balance=print("new_balance is",new_balance)

print("transfer")
amount = int(input('please enter the amount you want to transfer\n'))
move=int(new_balance-amount)
print("Sucessfully transfered", amount)