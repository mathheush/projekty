print("Program, który sprawdzi czy Twoja liczba jest palimdromiczna.")

a = input("Wpisz liczbę: ")
a = int(a)
y = 0
e = a

while (a > 0):
    x = a % 10
    y = (y * 10) + x
    a = a // 10
if e == y:
    print("Liczba jest palimdromiczna.")
else:print("Liczba nie jest palimdromiczna.")