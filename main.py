
import random
import os

class WordBank:
    def __init__(self):
        self.slowa = ["komputer", "programowanie", "informatyka", "akademia", "student"]

    def wylosuj_slowo(self):
        return random.choice(self.slowa).lower()

class Player:
    def __init__(self):
        self.licznik_bledow = 0
        self.odgadniete_litery = []

    def sprawdz_litere(self, litera):
        if litera not in self.odgadniete_litery:
            self.odgadniete_litery.append(litera)
            return True
        return False

class Game:
    MAKSYMALNE_BLEDOW = 5

    def __init__(self, gracz):
        self.gracz = gracz
        wordbank = WordBank()
        self.slowo_do_odgadniecia = wordbank.wylosuj_slowo()

    def koniec_gry(self):
        return self.gracz.licznik_bledow >= self.MAKSYMALNE_BLEDOW or '_' not in self.zamaskowane_slowo()

    def wygrana(self):
        return '_' not in self.zamaskowane_slowo()

    def zamaskowane_slowo(self):
        return ''.join(litera if litera in self.gracz.odgadniete_litery else '_' 
                      for litera in self.slowo_do_odgadniecia)

    def sprawdz_strzal(self, litera):
        if self.gracz.sprawdz_litere(litera):
            if litera not in self.slowo_do_odgadniecia:
                self.gracz.licznik_bledow += 1
                return False
            return True
        print("\nUżyłeś/aś już tej litery!")
        input()
        return False

def main():
    print("Witaj w grze Wisielec!")

    gracz = Player()
    gra = Game(gracz)

    while not gra.koniec_gry():
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Liczba błędów: {gracz.licznik_bledow}/{Game.MAKSYMALNE_BLEDOW}")
        print(f"Słowo: {gra.zamaskowane_slowo()}")
        print(f"Użyte litery: {', '.join(gracz.odgadniete_litery)}")

        user_input = input("\nPodaj literę: ").lower()

        if not user_input:
            continue

        strzal = user_input[0]
        if not strzal.isalpha():
            print("\nPodany znak nie jest literą!")
            input()
            continue

        gra.sprawdz_strzal(strzal)

    os.system('cls' if os.name == 'nt' else 'clear')
    if gra.wygrana():
        print("Gratulacje! Wygrałeś/aś!")
    else:
        print("Przegrałeś/aś!")

if __name__ == "__main__":
    main()
