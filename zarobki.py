kursy_walut_do_PLN = {'EUR' : 4.6, 'USD' : 4.5, 'BTC' : 1000000}

zarobki=['5001PLN', '972EUR', '1043USD', '1897PLN', '694EUR', '790USD']
zarobki_w_netto=[]

for z in zarobki:
    kwota=int(z[:-3])
    waluta=z[-3:]

    # print(waluta)
    # print(kwota)
    if waluta == 'PLN':
        kwota_w_pln= kwota
    else:
        kwota_w_pln=round(kwota*kursy_walut_do_PLN[waluta],3)
        print(z, "->", f'{kwota_w_pln}PLN')

#     if waluta == 'PLN':
#         kwota_w_pln= kwota
#     elif waluta == 'EUR':
#         kwota_w_pln=kwota*4.7067
#     elif waluta == 'USD':
#         kwota_w_pln=kwota*4.55
#     else:
#         print(f'nie ma takiej waluty{waluta}')
#     podatek = 0
#     if kwota > 3000:
#         podatek=kwota_w_pln*0.1
#     elif kwota> 5000:
#         podatek=kwota_w_pln*0.2
#     else:
#         podatek=0
#
#     netto=round(float(kwota_w_pln)-podatek,2)
#
#     zarobki_w_netto.append(netto)
#
# print(f'zarobki to {zarobki_w_netto}')
#
