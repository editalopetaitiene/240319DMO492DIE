import sqlite3
# sukurti klase baznycia (kunigo varda, ardesas, statybos metai)
#  sukurti klase Vykupija (viena propertį - bažnyčių sąrašas)
# sukurti vieną vyskupiją, kelias bažnyčias
# sukurti du metodus:
# istrinti baznycia, kuri leis istrinti baznycia pagal baznycios pavadinima, pavadinima turite pateikti kaip argumenta
# sukurti metoda, kuris leis atnaujinti informacija vienai baznyciai, naudokite input
class Baznycia():
    def __init__(self, kunigo_vardas, adresas, statybos_metai, vyskupijos_id):
        self.kunigo_vardas = kunigo_vardas
        self.adresas = adresas
        self.statybos_metai = statybos_metai
        self.vyskupijos_id = vyskupijos_id

    
class Vyskupija():
    def __init__(self):
        self.baznyciu_sarasas = []
        self.conn = sqlite3.connect('vyskupija.db') # sukuriame duomenų bazę
        self.cursor = self.conn.cursor()
        self.cursor.execute(""" CREATE TABLE IF NOT EXISTS vyskupija
                            (vyskuijos_id INTEGER PRIMARY KEY,
                            pavadinimas TEXT)
                            """)

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS baznycia
                            (baznycios_id INTEGER PRIMARY KEY,
                            kunigo_vardas VARCHAR(50) NOT NULL,
                            adresas TEXT,
                            statybos_metai TEXT, 
                            vyskupijos_id INTEGER,
                            FOREIGN KEY (vyskupijos_id) REFERENCES vyskupija(vyskupijos_id))
                             """)
        
        # self.cursor.execute("""INSERT INTO vyskupija (pavadinimas) VALUES ('Katedra')""")
       
        self.conn.commit()
   
    def prideti_baznycia(self, baznycia):
        self.cursor.execute('INSERT INTO baznycia (kunigo_vardas, adresas, statybos_metai, vyskupijos_id) VALUES (?,?,?,?)', (baznycia.kunigo_vardas, baznycia.adresas, baznycia.statybos_metai, baznycia.vyskupijos_id))
        self.baznyciu_sarasas.append(baznycia)
        self.conn.commit()
    def __del__ (self):
        self.conn.close()

    def spausdinti_baznycia(self):
        self.cursor.execute("SELECT* FROM baznycia")
        baznycios = self.cursor.fetchall()
        print('------bažnyčios------')
        for baznycia in baznycios:
            print(baznycia)

    def spausdinti_vyskupija(self):
        self.cursor.execute("SELECT* FROM vyskupija")
        vyskupijos = self.cursor.fetchall()
        print('------vyskupijos------')
        for vyskupija in vyskupijos:
            print(vyskupija)

    def istrinti_baznycia(self):
        self.cursor.execute("DELETE FROM baznycia WHERE adresas = ?", ('Kaunas',) )
        rezultatai = self.cursor.fetchall()
        print('--be ištrintų bažnyčių----')
    
    def atnaujinti_baznycia(self):
        self.cursor.execute("UPDATE baznycia ")
    



vyskupija = Vyskupija()

baznycia1 = Baznycia('Antanas', 'Kaunas', 1901, 1)
baznycia2 = Baznycia('Petras', 'Klaipėda', 1821, 1)
baznycia3 = Baznycia('Jonas', 'Šiauliai', 1859, 1)
# print(baznycia2.adresas)
# vyskupija = Vyskupija()

vyskupija.prideti_baznycia(baznycia1)
vyskupija.prideti_baznycia(baznycia2)
vyskupija.prideti_baznycia(baznycia3)


# print(vyskupija.baznyciu_sarasas[0].adresas)
# print(vyskupija.baznyciu_sarasas[2].adresas)
vyskupija.spausdinti_baznycia()
vyskupija.spausdinti_vyskupija()
vyskupija.istrinti_baznycia()
vyskupija.spausdinti_baznycia()

