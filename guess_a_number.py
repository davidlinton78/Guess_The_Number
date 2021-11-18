import random
print("Welcome to the guess game!")
def player(n):
    random_number = random.randint(1, n)
    player = 0
    while player != random_number:
        player = int(input(f"Guess a number between 1 and {n}! "))
        if player < random_number:
            print("Sorry to low guess a again! ")
        elif player > random_number:
            print("Sorry to high guess again! ") 
    print(f"Well done you have guessed number {random_number} correctly! ")           

player(30)        