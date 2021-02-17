def save_into_db(info):
    print("saved into databse")

def create_user():    
    username_input = input('Please enter your username: ')
    save_into_db(username_input)
    age_input = int(input('Please enter your birth year: '))
    age = 2020 - age_input
    print("You are",age, "years old.")