import requests
import json

def main():

    print("Witaj w kantorze walut.\n")

    x = input("Wpisz \"1\", jeśli chcesz sprzedać.\n"
              "Wpisz \"2\", jeśli chcesz kupić.\n"
              "Wpisz \"3\", jeśli chcesz zobaczyć aktualny kurs najpopularniejszych walut.\n"
              "Wpisz \"q\", aby zakończyć.\n"
              )

    if x == "1": #tutaj jest bid
        global do
        do = "sprzedać"

    elif x == "2":
        do = "kupić"
        kasa()
        currency()
        print(ask)

    elif x == "3":
        pass

    elif x == "q":
        pass

    else: print("Nieznana operacja."), akcja()

def currency():
    global waluta
    global link
    global bid
    global ask
    waluta = input("Podaj walutę:\n")
    link = requests.get(f'http://api.nbp.pl/api/exchangerates/rates/c/{waluta}/2023-02-24/?format=json')
    link = link.json()
    link = (link["rates"])
    link = (link[0])
    bid = (link["bid"])
    ask = (link["ask"])

def kasa():
    global money
    money = input(f"Ile chcesz {do}?: ")

main()

