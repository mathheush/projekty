import requests
import json

def akcja():
    print("Kantor")
    x = input("Wpisz \"1\", jeśli chcesz sprzedać.\nWpisz \"2\", jeśli chcesz kupić.\nWpisz \"q\", aby zakończyć.\n")
    if x == "1":
        currency()

    elif x == "2":
        pass
    elif x == "q":
        pass
    else: print("Nieznana operacja."), akcja()

def currency():
    global waluta
    global link
    global y
    global kurs
    waluta = input("Podaj walutę:\n")
    link = requests.get(f'http://api.nbp.pl/api/exchangerates/rates/c/{waluta}/2023-02-24/?format=json')
    kurs = link.json()

akcja()

#response = requests.get(link)
#print(response.json())
