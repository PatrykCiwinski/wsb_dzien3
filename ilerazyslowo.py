from typing import List
def zlicz_slowa(lista_slow: List[str]):
    slownik_wystapien = {}
    for slowo in lista_slow:
        if slowo in slownik_wystapien:
            slownik_wystapien[slowo] = slownik_wystapien[slowo] + 1
        else:
            slownik_wystapien[slowo] = 1
    return slownik_wystapien
def wez_slowa_z_pliku(nazwa_pliku: str) ->  List[str]:
    lista_wszystkich_slow = []
    with open(nazwa_pliku, 'r', encoding='utf-8') as fp:
        for linia in fp:
            # slowa = linia.split(' ')
            # lista_wszystkich_slow += slowa
            for slowo in linia.split(' '):
                slowo = slowo.rstrip()
                if slowo:
                    lista_wszystkich_slow.append(slowo.lower())
    return lista_wszystkich_slow
print(zlicz_slowa(['ala', 'ma', 'kota', 'ala']))
wystapienia_slow = zlicz_slowa(wez_slowa_z_pliku('plik_do_liczenia_slow.txt'))
print(wystapienia_slow)
max_wartość=-1
max_klucz=''
for klucz, wartosc in wystapienia_slow.items():
    if wartosc>max_wartość:
        max_wartość=wartosc
        max_klucz=klucz
print(max_klucz, 'wystepuje', max_wartość, 'razy')

lista_klucz_wartosc=sorted(wystapienia_slow.items(), key=lambda x:x[1], reverse=True)
print(lista_klucz_wartosc[:4])