print("Kalkulator BMI")

wiek = float(input("Wpisz wiek: "))

if wiek < 18:
    print("Dla osób poniżej 18 roku życia nie oblicza się wskaźnika BMI.")
    exit()
wzrost = float(input("Wpisz wzrost: "))
waga = float(input("Wpisz wagę: "))

wzrost /= 100
bmi = waga / (wzrost)**2
bmi = round(bmi, 2)

print("Twoje BMI wynosi " + format(bmi))

if bmi < 18.5:
    print("Niedowaga")
elif 18.5 <= bmi < 24.9:
    print("Waga prawidłowa")
elif 25 <= bmi < 29.9:
    print("Nadwaga")
elif 30 <= bmi < 34.9:
    print("Nadwaga I stopnia")
elif 35 <= bmi < 39.9:
    print("Nadwaga II stopnia")
else:
    print("Nadwaga III stopnia")

