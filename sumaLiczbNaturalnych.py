n = int(input("Podaj liczbę naturalną n: "))
suma = 0

for i in range(1, n+1):
    suma += i

print("Suma liczb naturalnych od 1 do", n, "wynosi:", suma)
