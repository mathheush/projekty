print("Program który liczy ilość słów w tekscie.")
text = input("Wpisz tekst: ")

text = text.replace(",","").replace(".","").replace("?","").replace("!","").replace("-","")

new = text.split()

print(len(new))
