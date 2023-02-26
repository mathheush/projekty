import json
import requests

print("Witaj w kantorze walut.\n")
def welcome():

    x = input("Wpisz \"1\", jeśli chcesz sprzedać PLN.\n"
              "Wpisz \"2\", jeśli chcesz kupić walutę.\n"
              "Wpisz \"3\", jeśli chcesz zobaczyć aktualny kurs najpopularniejszych walut.\n"
              "Wpisz \"q\", aby zakończyć.\n"
              "Co chcesz zrobić?: "
              )
    if x == "1":
        sell()

    elif x == "2":
        pass

    elif x == "3":
        currency()

    elif x == "q":
        pass

    else: print("Nieznana operacja. Spróbuj ponownie: \n"), welcome()

def currency():
    currency_all = ("EUR", "CHF", "USD", "GBP")
    print("\nOto aktualne kursy wybranych walut względem PLN:")
    print("Waluta    Sprzedaż    Kupno")
    for currency_id in currency_all:
        curr = requests.get(f'http://api.nbp.pl/api/exchangerates/rates/c/{currency_id}/2023-02-24/?format=json')
        curr = curr.json()
        curr = curr['rates']
        curr = curr[0]
        bid = curr.get('bid')
        ask = curr.get('ask')
        bid = float(round(bid, 2))
        ask = float(round(ask, 2))
        bid = str(bid)
        ask = str(ask)
        print(currency_id,"     ", bid,"      ",  ask )
    print("")
    welcome()

def sell():
    amount = input("Ile chcesz sprzedać PLN:")
    if amount == "q":
        welcome()
    else:
        try: int(amount)
        except: print("Podaj prawidłową ilość lub wpisz \"q\" aby wrócić."), sell()
        else: pass
    #tutaj skonczylem
welcome()
