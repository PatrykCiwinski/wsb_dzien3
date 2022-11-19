def czy_da_sie_mieszkac(metraz: float, wiek: int, typ_budynku: str)->bool:
    if metraz<200:
        return False
    if wiek>100:
        return False
    if typ_budynku == 'rudera':
        return False
    return True

def ladne_wypisanie_czy_da_sie_mieszkac(czy_do_zamieszkania):
    def czy_do_zamieszkania(metraz, wiek, typ_budynku):
        if metraz < 200:
            return False
        if wiek > 100:
            return False
        if typ_budynku == 'rudera':
            return False
