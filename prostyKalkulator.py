while True:
    operation = input("Wybierz operację (+, -, *, /), lub wpisz 'q' aby zakończyć: ")

    if operation == 'q':


    num1 = float(input("Podaj pierwszą liczbę: "))
    num2 = float(input("Podaj drugą liczbę: "))


    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        result = num1 / num2
    else:
        print("Nieznana operacja.")
        continue

    print("Wynik:", result)