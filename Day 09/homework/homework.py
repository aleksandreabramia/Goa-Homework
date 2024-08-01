#დროში მოგზაურობის პროგრამა


print("Welcome to the Time Travel Program!")
    
# Prompt user for current age
current_age = int(input("Please enter your current age: "))
    
# Prompt user for current year
current_year = int(input("Please enter the current year: "))
    
# Prompt user for number of years to travel
travel_years = int(input("How many years would you like to travel into the future? "))
    
 # Calculate new year and new age
new_year = current_year + travel_years
new_age = current_age + travel_years
    
 # Print the results
print(f"After traveling {travel_years} years into the future, it will be the year {new_year}.")
print(f"You will be {new_age} years old.")


