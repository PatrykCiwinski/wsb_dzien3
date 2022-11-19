
def odczytaj_stringi_z_list(nazwa_pliku):
    wynik=[]
    with open(nazwa_pliku, 'r') as plik:
        for linia in plik:
            wynik.append(linia)
    return wynik

def zapisz_do_pliku_linia_obok_lini(nazwa_pliku_do_zapisania, lista_lini):
    with open(nazwa_pliku_do_zapisania, 'w') as plik:
        for linia in lista_lini:
            plik.write(linia.rstrip())
            plik.write(' ')

print(odczytaj_stringi_z_list('plik.txt'))

zapisz_do_pliku_linia_obok_lini('plikwynikowy.txt', odczytaj_stringi_z_list('plik.txt'))

