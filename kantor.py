import json
import requests

print("Witaj w kantorze walut.\n")
def welcome():


    x = input("Wpisz \"1\", jeśli chcesz sprzedać.\n"
              "Wpisz \"2\", jeśli chcesz kupić.\n"
              "Wpisz \"3\", jeśli chcesz zobaczyć aktualny kurs najpopularniejszych walut.\n"
              "Wpisz \"q\", aby zakończyć.\n"
              "Co chcesz zrobić?: "
              )
    if x == "1":
        pass

    elif x == "2":
        pass

    elif x == "3":


    elif x == "q":
        pass

    else: print("Nieznana operacja. Spróbuj ponownie: \n"), welcome()

welcome()