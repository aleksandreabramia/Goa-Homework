#2) შექმენით პროგრამა რომელსაც შეეძლება დიალოგი თქვენთან (აირჩიეთ ნებისმიერი თემა) input გამოყენებით


def greet():
    return "Hi there! Let's chat. What's your favorite hobby?"

def respond_to_hobby(hobby):
    if hobby in ['reading', 'sports', 'music', 'cooking', 'gaming', 'travel', 'art']:
        return f"That's cool! I also like {hobby}."
    else:
        return "Interesting! Tell me more about it."

def main():
    print(greet())
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() in['bye']:
            print("Goodbye! Have a great day!")
            break
        
        print("Bot:", respond_to_hobby(user_input.lower()))

if __name__ == "__main__":
    main()





