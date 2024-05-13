import sqlite3 
import datetime
    # 1. Mechanikus:
        # 1. vardas
        # 2. pavardė
        # 3. el_paštas
        # 4. valandinis_atlyginimas
        # 5. specializacija (elektra/važiuoklė/variklis/kėbulai)
class Mechanikas():
    def __init__ (self, vardas, pavarde, el_pastas, valandinis_atlyginimas, specializacija):
        self.vardas = vardas
        self.pavarde = pavarde
        self.el_pastas = el_pastas
        self.valandinis_atlyginimas = valandinis_atlyginimas
        self.specializacija = specializacija
    # 2. Klientus:
        # 1. vardas
        # 2. pavardė
        # 3. el_paštas
class Klientas():
    def __init__ (self, vardas, pavarde, el_pastas):
        self.vardas = vardas
        self.pavarde = pavarde
        self.el_pastas = el_pastas
    # 3. Klientų automobilius:
        # 1. Valstybinis numeris
        # 2. Markė
        # 3. Modelis
        # 4. Savininkas
class Automobilis():
    def __init__ (self, valstybinis_numeris, marke, modelis, savininkas):
        self.valstybinis_numeris = valstybinis_numeris
        self.marke = marke
        self.modelis = modelis
        self.savininkas = savininkas
    # 4. Remontus:
        # 1. kliento_id
        # 2. mechaniko_id
        # 3. darbo_pradzia
        # 4. darbo_pabaiga
        # 5. darbo_kaina (darbo_pabaiga - darbo_pradzia) x mechaniko valandinis įkainis x 2 (autoserviso dalis)
        # 6. remonto_kategorija (elektra/važiuoklė/variklis/kėbulai)
class Remontas():
    def __init__ (self, kliento_id, mechaniko_id, darbo_pradzia, darbo_pabaiga, darbo_kaina, remonto_kategorija):
        self.kliento_id = kliento_id
        self.mechaniko_id = mechaniko_id
        self.darbo_pradzia = darbo_pradzia
        self.darbo_pabaiga = darbo_pabaiga
        self.darbo_kaina = darbo_kaina
        self.remonto_kategorija = remonto_kategorija

class Autoservisas():
    def __init__(self):
        self.conn = sqlite3.connect('autoservisas.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS mechanikai(
                            mechaniko_id INTEGER PRIMARY KEY,
                            vardas VARCHAR(50) NOT NULL, 
                            pavarde VARCHAR(50) NOT NULL,
                            el_pastas TEXT,
                            valandinis_atlyginimas FLOAT,
                            specializacija VARCHAR(50))""")
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS klientai(
                            kliento_id INTEGER PRIMARY KEY,
                            vardas VARCHAR(50) NOT NULL, 
                            pavarde VARCHAR(50) NOT NULL,
                            el_pastas TEXT)""")
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS automobiliai(
                            automobilio_id INTEGER PRIMARY KEY,
                            valstybinis_numeris TEXT, 
                            marke TEXT,
                            modelis TEXT,
                            kliento_id INTEGER,
                            FOREIGN KEY (kliento_id) REFERENCES klientai(kliento_id))""")
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS remontai(
                            remonto_id INTEGER PRIMARY KEY,
                            kliento_id INTEGER,
                            mechaniko_id INTEGER,
                            darbo_pradzia DATETIME,
                            darbo_pabaiga DATETIME,
                            darbo_kaina REAL,
                            remonto_kategorija VARCHAR(20) NOT NULL,                                          
                            FOREIGN KEY (kliento_id) REFERENCES klientai(kliento_id),
                            FOREIGN KEY (mechaniko_id) REFERENCES mechanikai(mechaniko_id))""")
# 1. pridėti:
    # 1. mechaniką
    def prideti_mechanika(self, vardas, pavarde, el_pastas, valandinis_atlyginimas, specializacija):
        mechanikas = Mechanikas(vardas, pavarde, el_pastas, valandinis_atlyginimas, specializacija)
        self.cursor.execute('INSERT INTO mechanikai (vardas, pavarde, el_pastas, valandinis_atlyginimas, specializacija) VALUES (?,?,?,?,?)', (vardas, pavarde, el_pastas, valandinis_atlyginimas, specializacija))
        # jeigu norime imti reikšmes iš objekto
        # self.cursor.execute('INSERT INTO gydytojai (vardas, pavarde, specializacija, el_pastas) VALUES (?,?,?,?)', (gydytojas.vardas, gydytojas.pavarde, gydytojas.specializacija, gydytojas.el_pastas))
        self.conn.commit()
        return mechanikas
    # 2. klientą
    def prideti_klienta(self, vardas, pavarde, el_pastas):
        klientas = Klientas(vardas, pavarde, el_pastas)
        self.cursor.execute('INSERT INTO klientai (vardas, pavarde, el_pastas) VALUES (?,?,?)', (vardas, pavarde, el_pastas))
        # jeigu norime imti reikšmes iš objekto
        # self.cursor.execute('INSERT INTO gydytojai (vardas, pavarde, specializacija, el_pastas) VALUES (?,?,?,?)', (gydytojas.vardas, gydytojas.pavarde, gydytojas.specializacija, gydytojas.el_pastas))
        self.conn.commit()
        return klientas
    # 3. kliento automobilį
    def prideti_automobili(self, valstybinis_numeris, marke, modelis, kliento_id):
        automobilis = Automobilis(valstybinis_numeris, marke, modelis, kliento_id)
        self.cursor.execute('INSERT INTO automobiliai (valstybinis_numeris, marke, modelis, kliento_id) VALUES (?,?,?,?)', (valstybinis_numeris, marke, modelis, kliento_id))
        self.conn.commit()
        return automobilis
    # 4. remontą

    def prideti_remonta(self, kliento_id, mechaniko_id, darbo_pradzia, darbo_pabaiga,  remonto_kategorija):
        remontas = Remontas(kliento_id, mechaniko_id, darbo_pradzia, darbo_pabaiga, darbo_kaina=1, remonto_kategorija=remonto_kategorija)
        date_format = "%Y-%m-%d %H:%M"
        darbo_pr_data = datetime.datetime.strptime(darbo_pradzia, date_format)
        darbo_pb_data = datetime.datetime.strptime(darbo_pabaiga, date_format)
        valandos = darbo_pb_data - darbo_pr_data
        val = valandos.total_seconds()/3600 
        val_atlyginimas = self.gauti_ikaini(mechaniko_id)
        darbo_kaina = val * val_atlyginimas*2
        self.cursor.execute('INSERT INTO remontai (kliento_id, mechaniko_id, darbo_pradzia, darbo_pabaiga, darbo_kaina, remonto_kategorija) VALUES (?,?,?,?,?,?)', (kliento_id, mechaniko_id, darbo_pradzia, darbo_pabaiga, darbo_kaina, remonto_kategorija))
        self.conn.commit()
        return remontas
    def gauti_ikaini(self, mechaniko_id):
        self.cursor.execute(f'SELECT valandinis_atlyginimas FROM mechanikai WHERE mechaniko_id = {mechaniko_id} ')
        val_atlyginimas = self.cursor.fetchone()
        print(val_atlyginimas)
        return float(val_atlyginimas[0])

    def perziureti_irasus(self, lentele):
        self.cursor.execute(f'SELECT * FROM {lentele}')
        rezultatu_sarasas = self.cursor.fetchall() 
        print('Įrašai pagal jūsų užklausą: ')
        for rezultatas in rezultatu_sarasas:
            print(rezultatas)

# papildomos užduotys, jas iškviesti reikia terminale nurodant veiksmo numerį/įvedant skaičių:
# patobulinkite funkciją, kuri prieš pridedant remontą patikrintų ar tuo metu, kai klientas pageidauja remontuoti automobilį yra laisvų automechanikų
    def ar_laisvas_mechanikas(self, darbo_pradzia, darbo_pabaiga, mechaniko_id):
        print(f'SELECT mechaniko_id FROM remontai WHERE mechaniko_id NOT IN (SELECT mechaniko_id FROM remontai (darbo_pradzia <= {darbo_pabaiga} AND darbo_pabaiga >= {darbo_pradzia})')
        self.cursor.execute(f'SELECT mechaniko_id FROM remontai WHERE mechaniko_id NOT IN (SELECT mechaniko_id FROM remontai (darbo_pradzia <= {darbo_pabaiga} AND darbo_pabaiga >= {darbo_pradzia})')
        rezultatu_sarasas = self.cursor.fetchall()
        print(rezultatu_sarasas)
        return rezultatu_sarasas

# sukurkite funkciją, kuri apskaičiuotų, kiek vienas klientas yra mums sumokėjęs iš viso už visų savo automobilių visus remontus
    def apskaiciuoti_kliento_visus_sumokejimus(self, kliento_id):
        self.cursor.execute("SELECT SUM(darbo_kaina) FROM remontai INNER JOIN automobiliai ON remontai.kliento_id = automobiliai.kliento_id WHERE automobiliai.kliento_id = ?", (kliento_id,))
        suma = self.cursor.fetchone()[5]
        if suma is None:
            suma = 0
        print(suma)
        return suma

# sukurkite funkciją, kuri apskaičiuotų, kiek vienas klientas yra mums sumokėjęs iš viso už vieno konkretaus automobilio remontą
    # def skaiciuoti_vieno_automobilio_remonto_kaina(self, kliento_id, automobilio_id, marke, modelis):
    #     self.cursor.execute("SELECT SUM(darbo_kaina) FROM remontai INNER JOIN automobiliai ON remontai.kliento_id = automobiliai.kliento_id WHERE automobiliai.kliento_id = ? AND automobiliai.marke = ? AND automobiliai.modelis = ?", (kliento_id, marke, modelis))
    #     suma = self.cursor.fetchone()[0]
    #     if suma is None:
    #         suma = 0
    #     return suma
# sukurkite funkciją, kuri apskaičiuotų kiek uždirbo konkretus mechanikas X
    # def skaiciuti_mechaniko_uzdarbi(self, mechaniko_id):
    #     self.cursor.execute("SELECT SUM(darbo_kaina) FROM remontai WHERE mechaniko_id = ?", (mechaniko_id,))