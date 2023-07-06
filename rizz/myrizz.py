import random
rizz_quotes = [
    "I'm lost, can you help me? I'm looking for your number"
    "Can you help me with something? I found this girl that I want to take out but I'm not sure to where... any suggestions? [...] Cool, what time am I picking you up?",
    "Rock, paper, scissors. If I win I get your number, if you win you get mine",
    "“Excuse me. I know this is kind of weird and I'm super shy…but I was just wondering…what pick up lines work best with you?”",
    "“I don't normally do this, but you look really upset standing over here on your phone and I thought I’d offer some support…did your stocks just crash or something?” ",
    "Can you help me? There's something wrong with my phone, it doesn't have your number in it",
    "Ask for directions, 'I'm Kenny but you can call me tonight''",
    "“Do I know you from somewhere? And wow…you’re even more adorable up close.”"
]

choice = random.choice(rizz_quotes)
test = input("Would you like to be rizzed? ")

insult_list = [
    "I hope that both sides of your pillow are warm tonight",
    "Are you a beaver cuz DANG you ugly",
    "You're mid anway"
]
stuff = random.choice(insult_list)

if test.lower() != 'no':
    print(choice)
else:
    print(stuff)


cheap_date_ideas = [
    "Bowling + Soda",
    "Mini golf + boba",
    "Painting + kiwi loco",
    "Table games + jamba juice",
    "R mountain + tropical smoothie",
    "Farmers market + yogurt",
    "Bake",
    "park walk + gelato",
    "stargazing",
    "thrift stuff + stuff"  
]

artsy_dates = [
    "painting + kiwi loco",
    "Bake",
    "stargazing",
    "thrift stuff + stuff"
]

active_dates = [
    "R mountain + tropical smoothie"
]



cheap_final = random.choice(cheap_date_ideas)

expensive_list = [
    "heber hatchets",
    "Twin falls water fall",
    "picnic + hammocking",
    "aquarium"
]

expensive_final = random.choice(expensive_list)

if test.lower() != 'no':
    ask = input("Do you need any date ideas? ")
    if ask.lower() != 'no':
        again = input("Expensive or Cheap date? ")
        if 'expensive' in again.lower():
            print(expensive_final)
        elif 'cheap' in again.lower():
            print(cheap_final)
        else:
            print("that's a typo, try again")
    else:
        print("You're mid anyway")
else:
    print("You're mid anyway")
