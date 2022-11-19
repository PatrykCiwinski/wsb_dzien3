
while True:
    pesel = input("podaj pesel")
    suma_cyfr=0
    for znak in pesel:
        suma_cyfr+=int(znak)
    if suma_cyfr%3 == 0 or suma_cyfr%4 ==0:
        print('pesel prawidłowy')
        break
    print('pesel nie poprawny')