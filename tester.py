from random import shuffle, choice

class Tester:
    def __init__(self, data_file: str, to_learn_file: str, artikeln = None):
        self.data_file = data_file
        self.to_learn_file = to_learn_file
        self.artikeln = artikeln
        self.has_articles = self.artikeln is not None

    def ask_new_session() -> bool:
        return input( "Möchtest du neue Sitzung anfangen? [j/N]: ").lower() in ["j", "ja", "yes", "y"]

    def get_data(self):
        data_file = self.data_file if Tester.ask_new_session() else self.to_learn_file

        with open(data_file, "r") as file:
            data = file.readlines()

        if len(data) == 0:
            print("Du hast nichts zu lernen")
            print("(Next time try answering \"j\" when you run the program)")
            print("((Yes, I am too lazy to write it in german))")
            exit(0)

        shuffle(data)

        self.data = data


    def test(self):
        self.get_data()

        wrongs = ""
        wrongs_n = 0

        artikel = ["", ""] 

        for line in self.data:
            print()

            # Load question
            words = line.strip().rsplit(" ", 1)
            if len(words) < 2:
                print("Zu wennig Elemente:", line)
                continue
            if self.has_articles:
                artikel = choice(self.artikeln)

            # Read input
            while True:
                print(words[0] + " ... " + artikel[0])
                antwort = input("=> ").strip()
                if not len(antwort.split()) == 2:
                    print("Schreib 2 Wörter (Präposition + Artikel)")
                    continue
                break

            # Check the answer
            if not words[1] + (" " + artikel[1] if self.has_articles else "") == antwort:
                wrongs += line
                wrongs_n += 1
                print("Nein!!! Richige antwort ist:", words[1] + " " + artikel[1])

        with open(self.to_learn_file, "w") as to_learn:
            to_learn.write(wrongs)

        print("Du hast", wrongs_n, "Fehler gemacht")
