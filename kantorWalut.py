import requests
import json

def akcja():

    print("Kantor")

    x = input("Wpisz \"1\", jeśli chcesz sprzedać.\nWpisz \"2\", jeśli chcesz kupić.\nWpisz \"q\", aby zakończyć.\n")

    if x == "1":
        global do
        do = "sprzedać"
        kasa()
        currency()
        print(bid)

    elif x == "2":
        do = "kupić"
        kasa()
        currency()
        print(ask)

    elif x == "q":
        pass

    else: print("Nieznana operacja."), akcja()

def currency():
    global waluta
    global link
    global y
    global kurs
    global o
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
akcja()

