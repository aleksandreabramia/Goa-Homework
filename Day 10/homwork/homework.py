#შევქმნათ ბანკი
print("creat new bank account")
name=print(input("Enter your new bank account name:"))
password=input("Enter your new bank account password:")

if input("Reenter your password:") ==  password :
    print("New bank created")
else:
    if input("Try again !:") == password :
        print("New  bank account created")
    else :
        input("Try  again !") == password 
        if input("paswork is incorrect, Try again !:") == password :
            print("New bank account created")
        else :
            print("you cant have another try!")

initial_balance = float(input("Enter initial deposit amount: "))
print ( " your balance is ", initial_balance)


initial_balance = "deposit"
gamotana = "withdraw"
anserw = input ("do you want to deposit or withdraw? : ")
if anserw == "deposit" :
    input ("enter the amount: ")
if anserw == "withdraw" :
    input ("enter the amount: ")
