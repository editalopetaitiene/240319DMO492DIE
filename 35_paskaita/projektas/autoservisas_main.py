from autoservisas import Autoservisas

def main():

    autoservisas = Autoservisas()
    while True:
        print('\npasirinkite veiksmą: ')
        print('1 - baigti darba')
        print('2 - prideti mechaniką')
        print('3 - prideti klientą')
        print('4 - prideti kliento automobilį')
        print('5 - prideti remontą')
        print('6 - peržiūrėti duomenis')
        print('7 - kliento mokėjimai')
        print('8 – kliento konkretaus automobilio mokėjimai')
        print('9 – konkretaus mechaniko uždarbis')

        pasirinkimas = input('Iveskite pasirinkimo numeri: ')
        if pasirinkimas == '1':
            print('Programos pabaiga')
            break
        elif pasirinkimas == '2':
            print('Iveskite mechaniko informacija')
            vardas = input('Vardas: ')
            pavarde = input('Pavarde: ')
            el_pastas = input('el_pastas: ')
            valandinis_atlyginimas = input('valandinis atlyginimas: ')
            specializacija = input('Specializacija elektra/važiuoklė/variklis/kėbulai: ')
            mechanikas = autoservisas.prideti_mechanika(vardas, pavarde, el_pastas, valandinis_atlyginimas, specializacija) 
            print(f"Mechanikas {mechanikas.vardas} buvo pridetas")
        elif pasirinkimas == '3':
            print('Iveskite kliento informacija')
            vardas = input('Vardas: ')
            pavarde = input('Pavarde: ')
            el_pastas = input('el_pastas: ')
            klientas = autoservisas.prideti_klienta(vardas, pavarde, el_pastas) 
            print(f"Klientas {klientas.vardas} buvo pridetas")
        elif pasirinkimas == '4':
            print('Iveskite kliento automobilo informacija')
            valstybinis_numeris = input('valstybinis numeris: ')
            marke = input('marke: ')
            modelis = input('modelis: ')
            savininkas = input('savininko_id: ')
            automobilis = autoservisas.prideti_automobili(valstybinis_numeris, marke, modelis, savininkas) 
            print(f"Automobilis {automobilis.valstybinis_numeris} buvo pridetas")
        elif pasirinkimas == '5':
            print('Iveskite automobilo remonto informacija elektra/važiuoklė/variklis/kėbulai: ')
            kliento_id = int(input('kliento_id: '))
            mechaniko_id = int(input('mechaniko_id: '))
            darbo_pradzia = input('darbo pradzia: ')
            darbo_pabaiga = input('darbo pabaiga: ')
            remonto_kategorija = input('darbo kategorija: ')
            if autoservisas.ar_laisvas_mechanikas(darbo_pradzia, darbo_pabaiga, mechaniko_id):
                remontas = autoservisas.prideti_remonta(kliento_id, mechaniko_id, darbo_pradzia, darbo_pabaiga, remonto_kategorija) 
                print(f"kliento Nr. {remontas.kliento_id} remontas buvo užregistruotas sėkmingai mechanikui Nr. {remontas.mechaniko_id}")
            else:
                print(f'Nepavyko pridėti remonto, nėra laisvo mechaniko')
        elif pasirinkimas == '6':
            ats_lentele = input('Iveskits lenteles pavadinima mechanikai/klientai/automobiliai/remontai: ')
            while ats_lentele not in ['mechanikai','klientai', 'automobiliai', 'remontai']:
                ats_lentele = input('Iveskits lenteles pavadinima mechanikai/klientai/automobiliai/remontai: ')
            autoservisas.perziureti_irasus(ats_lentele)
        elif pasirinkimas == '7':
            print('Iveskite kliento_id, kurio mokėjimus norite patikrinti: ')
            kliento_id = int(input('kliento_id: '))
            

        # elif pasirinkimas == '8':

        # elif pasirinkimas == '9':

        else:
            print('Pasirinkimas neteisingas, bandykite dar karta')


if __name__ == '__main__':
    main()