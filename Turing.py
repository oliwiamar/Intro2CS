age = 24
if age < 12:
    print("Child ticket")
else:
    print("Adult ticket")

is_student = True
if is_student == True:
    print("Student discount")

day = "Wed"
if day == "Sat":
    print("Weekend price")
else:
    print("Weekday price")


language = "Latin"
if language == "English":
    print("hello")
elif language == "Spanish":
    print("hola")
elif language == "Polish":
    print("cześć")
elif language == "German":
    print("halo")
elif language == "French":
    print("salut")
else:
    print("I do not know this language yet")

word = "pastry"

irregulars = {"child" : "children",
     "foot": "feet",
     "mouse": "mice"}

vowels = ("a", "e", "i", "o", "u")

if word in irregulars:
    plural = irregulars[word]
elif word[-1] in ("s","x", "z"):
    plural = word + "es"
elif word[-1] == "y" and word [-2] not in vowels:
    plural = word[:-1] + "ies"
else:
    plural = word + "s"
print(word, "->", plural)
