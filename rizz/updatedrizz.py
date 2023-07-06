import random
import re

# Example data
names = ["John", "Jane", "Mike", "Mark", "Sarah"]

# Pattern to match names starting with "J"
pattern = r"^J.*"

# Filter names using the pattern
matched_names = [name for name in names if re.match(pattern, name)]

# Print the matched names
print(matched_names)

# FIX THIS STUFF

rizz_quotes = [
    "Do you have a map? Because I keep getting lost in your eyes.",
    "Is your name Google? Because you have everything I've been searching for.",
    "Are you a magician? Because whenever I look at you, everyone else disappears.",
    "Excuse me, but I think you dropped something: my jaw.",
    "Is your dad a baker? Because you're a cutie pie.",
    "Can you lend me a kiss? I promise I'll give it back.",
    "Is it hot in here, or is it just you?",
    "Do you have a name, or can I call you mine?",
    "If you were a vegetable, you'd be a 'cute-cumber'.",
    "Is your name Wi-Fi? Because I'm really feeling a connection.",
    "Do you believe in love at first sight, or should I walk by again?",
    "Do you have a Band-Aid? I just scraped my knee falling for you.",
    "I was looking for treasure and I think I found some",
    "This sunburn is hot but you're hotter"
]

insult_list = [
    "I hope that both sides of your pillow are warm tonight",
    "Are you a beaver cuz DANG you ugly",
    "You're mid anyway"
]

cheap_date_ideas = [
    "Bowling + Soda",
    "Mini golf + boba",
    "Painting + kiwi loco",
    "Table games + jamba juice",
    "R mountain + gelato",
    "Farmers market + yogurt",
    "Bake",
    "Park walk + gelato",
    "Stargazing",
    "Thrift stuff + stuff",
    "Movie night at the Hemming Village",
    "Visit Porter Park and have a picnic",
    "Explore Nature Park",
    "Go for a bike ride around town"
]

expensive_list = [
    "Heber Hatchets",
    "Twin Falls Waterfall",
    "Picnic + Hammocking",
    "Aquarium",
    "Escape room at Puzzle Effect",
    "Horseback riding at Dry Creek Ranch"
]

def get_random_quote():
    return random.choice(rizz_quotes)

def get_random_insult():
    return random.choice(insult_list)

def get_random_cheap_date_idea():
    return random.choice(cheap_date_ideas)

def get_random_expensive_date_idea():
    return random.choice(expensive_list)

def prompt_user(message):
    response = input(message)
    return response.lower()

def main():
    test = prompt_user("Would you like to be rizzed? ")
    if test != 'no':
        print(get_random_quote())
    else:
        print(get_random_insult())

    ask = prompt_user("Do you need any date ideas? ")
    if ask != 'no':
        again = prompt_user("Expensive or Cheap date? ")
        if again == 'expensive':
            print(get_random_expensive_date_idea())
        elif again == 'cheap':
            print(get_random_cheap_date_idea())
        else:
            print("That's a typo, try again")
    else:
        print("You're mid anyway")

if __name__ == '__main__':
    main()
