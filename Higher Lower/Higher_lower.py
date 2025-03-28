from art import logo , vs
from Game_data import data
import random
from replit import clear
print(logo)
score = 0
person_2 = random.choice(data)
def person():
    return random.choice(data)

def comparison(follower_1 , follower_2 , user_choice):
    if follower_1> follower_2: 
        return user_choice == 'a'
    else:
        return user_choice == 'b'

def printer(person_1 , person_2):
    print(f"Compare A: {person_1['name']} , {person_1['description']}, {person_1['country']}")
    print(vs)
    print(f"Against B: {person_2['name']} , {person_2['description']}, {person_2['country']}")
    followers_1 = person_1['follower_count']
    followers_2 = person_2['follower_count']
    user_choice = input("Who has more followers? 'A' and 'B': ").lower()
    return comparison(followers_1 , followers_2, user_choice)


while True:
    person_1 = person_2
    person_2 = person()
    while person_1['name'] == person_2['name']:
        person_2 = person()
    game = printer(person_1 , person_2)
    if game == True:
        clear()
        print(logo)
        score += 1
        print(f"You're Wright! Your score: {score}")
    else:
        clear()
        print(logo)
        print(f"Sorry you're wrong. Youyr score: {score}")
        break