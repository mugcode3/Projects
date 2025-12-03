import random

play_again = "y"
words = [
    "banana",
    "computer",
    "python",
    "giraffe",
    "pencil",
    "apple",
    "orange",
    "keyboard",
    "monitor",
    "notebook",
    "elephant",
    "tiger",
    "lion",
    "house",
    "bottle",
    "chocolate",
    "sandwich",
    "backpack",
    "library",
    "window",
    "flower",
    "mountain",
    "river",
    "ocean",
    "guitar",
    "drum",
    "violin",
    "camera",
    "bicycle",
    "airplane",
    "pillow",
    "blanket",
    "candle",
    "painting",
    "basket",
    "rabbit",
    "monkey",
    "donkey",
    "penguin",
    "dolphin",
    "strawberry",
    "tomato",
    "carrot",
    "lettuce",
    "onion",
    "umbrella",
    "wallet",
    "glasses",
    "chair",
    "table",
    "keyboard",
    "notepad",
    "marker",
    "eraser",
    "chalk",
    "teacher",
    "student",
    "classroom",
    "school",
    "library",
    "planet",
    "star",
    "moon",
    "sun",
    "comet",
    "mountain",
    "valley",
    "forest",
    "desert",
    "beach",
    "river",
    "lake",
    "ocean",
    "waterfall",
    "cave",
    "soccer",
    "basketball",
    "tennis",
    "baseball",
    "volleyball",
    "guitar",
    "piano",
    "drum",
    "violin",
    "flute",
    "car",
    "bus",
    "train",
    "bicycle",
    "motorcycle",
    "phone",
    "tablet",
    "laptop",
    "camera",
    "television",
    "pizza",
    "burger",
    "sandwich",
    "noodles",
    "chocolate",
    "dog",
    "cat",
    "rabbit",
    "hamster",
    "parrot",
]
points = 0

while play_again == "y":
    points = 0
    random.shuffle(words)
    five_words = words[:5]

    for word in five_words:

        attempts = 0
        max_attempts = 2

        letters = list(word)
        random.shuffle(letters)
        scrambled = "".join(letters)

        while attempts < max_attempts:

            print(f"'{scrambled}'\nHint: The word starts with {word[0].upper()}")

            guess = input("what's the word?: ").strip().lower()

            if guess == word:
                print("Correct!")
                points += 1
                print(f"You've got {points} / 5 points!")
                break
            else:
                attempts += 1
                if attempts < max_attempts:
                    print("Wrong! Try again.")
                    print("-")

        if attempts == max_attempts and guess != word:
            print(f"The word was: {word}")
            print(f"You've got {points} / 5 points!")

        print("---")

    print(f"Game over! You scored {points} / 5 points.")

    play_again = input("Play again? (y/n)").strip().lower()
    while play_again not in ["y", "n"]:
        print("Invalid input! Please type 'y' or 'n'.")
        play_again = input("Play again? (y/n)").strip().lower()

    if play_again == "n":
        break
