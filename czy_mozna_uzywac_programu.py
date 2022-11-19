
def czy_mozna_uzywac(nazwa_uzytkownika, nr_lic):
    if not nazwa_uzytkownika.endswith('@wsb.pl'):
        return False
    return nr_lic%3==0

print(f"{czy_mozna_uzywac('patryk@wsb.pl', 3)}")