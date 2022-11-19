
import datetime


def podaj_liczbe_z_zakresu(a: int, b: int) -> int:
    while True:
        odp = input(f'Podaj liczbe z zakresu od {a} do {b} ')
        liczba = int(odp)
        if liczba >= a and liczba <= b:
            return liczba


def stworz_date(rok, miesiac, dzien):
    return datetime.date(year=rok, month=miesiac, day=dzien)


def podaj_date(**kwargs) -> datetime.date:
    print('podano kwargs: ', kwargs)
    if 'dzien' in kwargs:
        print('mam dzien', kwargs['dzien'])
    else:
        kwargs['dzien'] = podaj_liczbe_z_zakresu(1, 31)
    if 'miesiac' in kwargs:
        print('mam podany miesiac', kwargs['miesiac'])
    else:
        kwargs['miesiac'] = podaj_liczbe_z_zakresu(1, 12)
    if 'rok' in kwargs:
        print('mam podany rok', kwargs['rok'])
    else:
        kwargs['rok']=int(input('podaj rok '))
    print('mam podane ', kwargs)
    return stworz_date(**kwargs)



data = podaj_date(dzien=19, miesiac=11)
print(data)
data = podaj_date(rok=2022)
print(data)

