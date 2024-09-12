#1) while loop ის გამოყენებით დაწერეთ I Love You ათსჯერ ისე რომ თითოეული ხაზი იწყებოდეს რიცხვით 

counter = 1

while counter < 101: 
    print(str(counter) +  ". I LOVE YOU")  
    counter = counter + 1

#2) 2) მომხმარებელს შემოატანინეთ რიცხვი შემდეგ while loop ის გამოყენებით 1-დან მომხმარების შემოტანილ რიცხვამდე დაბეჭდეთ ყველა რიცხვი და თან გვერძე მიუწერეთ ლუწია თუ კენტი

num = int(input("enter: "))
i = 0
while i < num:
    i = i + 1
    if i % 2 == 0:
        print ("is even")
    else:
        print ("odd")

#3) მომხმარებელს შემოატანინეთ რიცხვი შემდეგ while loop ის გამოყენებით 1-დან მომხმარების შემოტანილ რიცხვამდე დაბეჭდეთ მხოლოდ ხუთის ჯერადი რიცხვები

user_input = int(input("Enter a number: "))
num = 1
while num <= user_input:
    num = num + 1
    if num % 5 == 0:
      print(num)


#4) მომხამრებელს შევეკითხოთ სახელი და იქამდე არ შემოვუშვათ სახლში სანამ ის არიტყვის რომ ქვია სვარჩიკა მაყვალა
name = input("enter your name dude: ")
while name != " სვარჩიკა მაყვალა":
    print("შენ არ ხარ სვარჩიკაა წადი რა")
    name = input( " enter your name: ")
    print("გამარჯობა უფროსო სვარჩიჯა მაყვალა" )


#5) მომხმარებელს შეეკითხეთ ექაუნთძე შესასვლელი პაროლი, სანამ ის არ შემოიტანს სწორ პაროლს მას ხელახლა გაუმეორეთ რომ შემოიტანოს პაროლი თუ სწორად შემოიტანს დაბეჭდოს რომ ექაუნთზე შევიდა
enter_password = int(input("Enter your password: "))
correct_password = enter_password


while True:
    user_password = input("Enter the password to access the account: ")
    
    if user_password == correct_password:
        print("Access to the account!")
        break
    else:
        print("Incorrect password. Please try again.")



