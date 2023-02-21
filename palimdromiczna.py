Czy palimdromiczna
a = input("wpisz")
a = int(a)
y = 0
e = a
while (a > 0):
    x = a % 10
    y = (y * 10) + x
    a = a // 10
kkuuuruw
if e == y:
    print("liczba jest palimdromiczna")
else:print("liczba nie jest palimdromiczna")
