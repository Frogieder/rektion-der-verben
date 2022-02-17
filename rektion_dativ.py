from random import shuffle, choice

"""
Can only at this point in time - but who cares?
"""

pronouns = [
    ["ich", "mir"], 
    ["du", "dir"], 
    ["er", "ihm"], 
    ["es", "ihm"], 
    ["sie", "ihm"], 
    ["wir", "uns"], 
    ["ihr", "euch"], 
    ["Sie", "ihnen"],
]

artikeln = [
    ["(ich)", "mir"], 
    ["(du)", "dir"], 
    ["(er)", "ihm"], 
    ["(es)", "ihm"], 
    ["(sie)", "ihm"], 
    ["(wir)", "uns"], 
    ["(ihr)", "euch"], 
    ["(Sie)", "ihnen"],
    ["(der) Man", "dem"],
    ["(die) Frau", "der"],
    ["(das) Kind", "dem"],
    ["(die) Leute", "den"]
]

new_session = input("Möchtest du neue Sitzung anfangen? [j/N]: ")

filename = "data.txt" if new_session in ["j", "ja", "yes", "y"] else "to_learn.txt"


with open(filename, "r") as file:
    data = file.readlines()

if len(data) == 0:
    print("Du hast nichts zu lernen")
    print("(Next time try answering \"j\" when you run the program)")
    print("((Yes, I am too lazy to write it in german))")
    exit(0)

shuffle(data)

wrongs = ""
wrongs_n = 0

for line in data:
    print()

    # Load question
    words = line.strip().rsplit(" ", 1)
    if len(words) < 2:
        print("Zu wennig Elemente:", line)
        continue
    artikel = choice(artikeln)

    # Read input
    while True:
        print(words[0] + " ... " + artikel[0])
        antwort = input("=> ").strip()
        if not len(antwort.split()) == 2:
            print("Schreib 2 Wörter (Präposition + Artikel)")
            continue
        break

    # Check the answer
    if not words[1] + " " + artikel[1] == antwort:
        wrongs += line
        wrongs_n += 1
        print("Nein!!! Richige antwort ist:", words[1] + " " + artikel[1])


with open("to_learn.txt", "w") as to_learn:
    to_learn.write(wrongs)

print("Du hast", wrongs_n, "Fehler gemacht")
