plan = ["gym","work", "sleep", "read", "walk"]
print(plan)

print(plan[0])
print(plan[-1])

print(plan[1:4])
print(plan[::-1])

plan[1] = "shopping"
print(plan)

plan.append("shopping")
plan.insert(0, "cooking")
print(plan)

plan.remove("walk")

weekend = ["partying", "swimming"]
final_plan = plan + weekend
print(final_plan)


# tuple task
city = ("Poznań", "Poland", 52.41, 16.93)
print(city)
print(type(city))

print(city[1])
print(city[-1])

name, country, latitude, longitude = city
print(country)
print(longitude)


city_list = list(city)
city_list[1] = "Latvia"
city = tuple(city_list)
print(city)

#sets task

mine = {"chicken", "sushi", "pasta", "beetroot", "mozarella"}
friend = {"tofu", "sushi", "pizza", "tomatoes", "pasta"}

print(mine | friend)

print(mine & friend)

print(mine - friend)

print(mine ^ friend)

#dictionary task

words = {"book" : "książka", 
         "dog": "pies",
        "potato": "ziemniak", 
        "water": "woda"}

print(words["book"])
print(len(words))

words["window"] = "okno"
words["dog"] = "piesek"
print(words)

words.update({"phone": "telefon", 
              "table" : "stół"})
print(words)

print(list(words.keys()))
print(list(words.values()))
print(list(words.items()))