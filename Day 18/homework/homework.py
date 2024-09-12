#1) შექმენით ბანკის სისტემა სადაც იქნება ძალიან ბევრი პირობები და გამოიყენებთ if, elif და else -ს, გამოიყენებთ ასევე განვლილ მასალასაც

print("1. balance: ")
print("2. Credit to someone's account:  ")
print("3. Credit to your account:"  )
print("Hello, please choose number you want:" )
num = int(input(" number: "))

#ბალანსი

if num == 1:
    print(" Now you have 10.00 Gel ")

elif num == 2:
    id = int(input("enter your id: "))
    if len(str(id))== 5:
        ask = int(input("How much money do you need in your account?" ))
        print(" Now you have {ask:.2} Gel")
    else:
        ask = input ("Are you Human? yes or no:") 
        if ask == "yes":
            print("Enter correct id..")
        elif ask == "no":
            print("go fuck your self")
        else:
            print("ERROR")