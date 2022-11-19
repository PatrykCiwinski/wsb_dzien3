import datetime

def czy_liczba_z_zakresu(a,b):
    while True:
        odp=input(f'podaj liczbe z zakresu{a}/{b} ')
        liczba=int(odp)
        if liczba>=a and liczba<=b:
            return liczba


def podaj_date():
    print('podaj dzien urodzenia')
    dzien= czy_liczba_z_zakresu(1, 31)
    print('podaj miesiac')
    miesiac= czy_liczba_z_zakresu(1,12)
    rok=int(input('podaj rok'))

    return datetime.date(year=rok, month=miesiac, day=dzien)

def wypisz_ile_czasu_minelo(od_kiedy: datetime.date):
    do_kiedy = datetime.date.today()
    roznica_w_czasie = do_kiedy - od_kiedy
    roznica_w_dniach = roznica_w_czasie.days
    print('od czasu uordzania ', od_kiedy, ' minęło ', roznica_w_dniach, ' dni')
    roznica_w_latach=roznica_w_dniach//365
    print(f'od czasu urodzenia {od_kiedy}, minelo {roznica_w_latach} lat i {roznica_w_dniach%365} dni')

data_urodzenia=podaj_date()

print(wypisz_ile_czasu_minelo(data_urodzenia))
