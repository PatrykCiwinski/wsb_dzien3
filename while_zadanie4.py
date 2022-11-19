import sys


def wymus_zgode_na_warunki():
    while True:
        odp=input('czy zgadzasz sie na warunki? (tak/nie/exit) ').lower()
        if odp=="tak":
            return
        if odp =='nie':
            print('wymagane jest zaakceptowanie do dzialania')
            continue
        if odp=='exit':
            sys.exit(0)

wymus_zgode_na_warunki()