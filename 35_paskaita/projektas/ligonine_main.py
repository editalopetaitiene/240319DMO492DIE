from ligonine import Ligonine

def main():

    ligonine = Ligonine() 
    while True:
        print('\npasirinkite veiksmą: ')
        print('1 - baigti darba')
        print('2 - prideti gydytoja')
        print('3 - prideti pacienta')
        print('4 - prideti susitikima')
        print('5 - peržiūrėti duomenis')

        pasirinkimas = input('Iveskite pasirinkimo numeri: ')

        if pasirinkimas == '1':
            print('Programos pabaiga')
            break
        elif pasirinkimas == '2':
            print('Iveskite gydytojo informacija')
            vardas = input('Vardas: ')
            pavarde = input('Pavarde: ')
            specializacija = input('Specializacija: ')
            el_pastas = input('el_pastas: ')
            gydytojas = ligonine.prideti_gydytoja(vardas, pavarde, specializacija, el_pastas) 
            print(f"Gydytojas {gydytojas.vardas} buvo pridetas")
        elif pasirinkimas == '3':
            print('Iveskite paciento informacija:')
            vardas = input('Vardas: ')
            pavarde = input('Pavarde: ')
            gimimo_data = input('Gimimo data: ')
            lytis = input('Lytis: ')
            el_pastas = input('el_pastas: ')
            gydytojo_id = int(input('gydytojo_id: '))
            pacientas = ligonine.prideti_pacienta(vardas, pavarde, gimimo_data, lytis, el_pastas, gydytojo_id)
            print(f"Pacientas {pacientas.vardas} buvo pridetas")
        elif pasirinkimas == '4':
            print('Iveskite susitikimo informacija:')
            paciento_id = int(input('paciento_id: '))
            gydytojo_id = int(input('gydytojo_id: '))
            susitikimo_data = input('vizito data: ')
            paskirtis = input('paskirtis: ')
            komentarai = input('Komentarai: ')
            susitikimo_id = ligonine.prideti_susitikima(paciento_id, gydytojo_id, susitikimo_data, paskirtis, komentarai)
            susitikimas = ligonine.gauti_susitikimo_info_pagal_id(int(susitikimo_id))
            print(susitikimas)
            p_vardas, g_vardas, data = susitikimas #unpacinam
            print(f"Paciento {p_vardas} susitikimas su gydytoju {g_vardas} buvo pridetas. Vizito data {data}")
            # print(f"Susitikimas {susitikimas} buvo pridetas")
        elif pasirinkimas == '5':
            lentele = input('Iveskits lenteles pavadinima gydytojai/pacientai/susitikimai: ')
            while lentele not in ['gydytojai','pacientai', 'susitikimai']:
                lentele = input('Iveskits lenteles pavadinima gydytojai/pacientai/susitikimai: ')
            ligonine.perziureti_irasus(lentele)
        else:
            print('Pasirinkimas neteisingas, bandykite dar karta')


if __name__ == '__main__':
    main()