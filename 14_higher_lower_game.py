import random
from game_data import data
from art5 import vs, logo

print(logo)

user_score = 0
is_game_end = False

current_player = random.choice(data)

while not is_game_end:
    random_item2 = random.choice(data)

    formatted_output = f"Compare A: {current_player['name']}, a {current_player['description']}, from {current_player['country']}"
    print(formatted_output)

    print(vs)

    formatted_output2 = f"Against B: {random_item2['name']}, a {random_item2['description']}, from {random_item2['country']}"
    print(formatted_output2)

    user_answer = input("Who has more followers? Type 'A' or 'B': ").capitalize()
    correct_answer = "A" if current_player["follower_count"] > random_item2["follower_count"] else "B"

    if user_answer == correct_answer:
        user_score += 1
        print("\n" * 50)
        print(logo)
        print(f"You are right! Current score: {user_score}.")

        if correct_answer == "A":
            current_player = current_player
        else:
            current_player = random_item2
    else:
        is_game_end = True
        print("\n" * 50)
        print(logo)
        print(f"Sorry that's wrong. Final score: {user_score}")
