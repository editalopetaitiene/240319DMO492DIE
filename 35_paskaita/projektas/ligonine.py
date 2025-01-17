import sqlite3

class Gydytojas:
    def __init__ (self, vardas, pavarde, specializacija, el_pastas):
        self.vardas = vardas
        self.pavarde = pavarde
        self.specializacija = specializacija
        self.el_pastas = el_pastas

class Pacientas:
    def __init__ (self, vardas, pavarde, gimimo_data, lytis, el_pastas, gydytojo_id):
        self.vardas = vardas
        self.pavarde = pavarde
        self.gimimo_data = gimimo_data
        self.lytis = lytis
        self.el_pastas = el_pastas
        self.gydytojo_id = gydytojo_id

class Susitikimas:
    def __init__ (self, paciento_id, gydytojo_id, susitikimo_data, paskirtis, komentarai):
        self.paciento_id = paciento_id
        self.gydytojo_id = gydytojo_id
        self.susitikimo_data = susitikimo_data
        self.paskirtis = paskirtis
        self.komentarai = komentarai

class Ligonine:
    def __init__ (self):
        self.conn = sqlite3.connect('ligonine.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS gydytojai
              (gydytojo_id INTEGER PRIMARY KEY, 
               vardas VARCHAR(50) NOT NULL, 
               pavarde VARCHAR(50) NOT NULL,
               specializacija VARCHAR(50) NOT NULL, 
               el_pastas text)""")
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS pacientai(
                paciento_id INTEGER PRIMARY KEY, 
                vardas VARCHAR(50) NOT NULL, 
                pavarde VARCHAR(50) NOT NULL,
                gimimo_data TEXT, 
                lytis TEXT, 
                el_pastas TEXT,
                gydytojo_id INTEGER,
                FOREIGN KEY (gydytojo_id) REFERENCES gydytojai(gydytojo_id))""")
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS susitikimai
               (susitikimo_id INTEGER PRIMARY KEY, 
               paciento_id INTEGER,
               gydytojo_id INTEGER,
               susitikimo_data TEXT,
               paskirtis TEXT,
               komentarai TEXT,
               FOREIGN KEY (paciento_id) REFERENCES pacientai(paciento_id),
               FOREIGN KEY (gydytojo_id) REFERENCES gydytojai(gydytojo_id))""")
        self.conn.commit()
    
    def prideti_gydytoja(self, vardas, pavarde, specializacija, el_pastas):
        gydytojas = Gydytojas(vardas, pavarde, specializacija, el_pastas)
        self.cursor.execute('INSERT INTO gydytojai (vardas, pavarde, specializacija, el_pastas) VALUES (?,?,?,?)', (vardas, pavarde, specializacija, el_pastas))
        # jeigu norime imti reikšmes iš objekto
        # self.cursor.execute('INSERT INTO gydytojai (vardas, pavarde, specializacija, el_pastas) VALUES (?,?,?,?)', (gydytojas.vardas, gydytojas.pavarde, gydytojas.specializacija, gydytojas.el_pastas))
        self.conn.commit()
        return gydytojas
    
    def prideti_pacienta(self, vardas, pavarde, gimimo_data, lytis, el_pastas, gydytojo_id):
        pacientas = Pacientas(vardas, pavarde, gimimo_data, lytis, el_pastas, gydytojo_id)
        self.cursor.execute('INSERT INTO pacientai (vardas, pavarde, gimimo_data, lytis, el_pastas, gydytojo_id) VALUES (?, ?, ?, ?, ?, ?)', (vardas, pavarde, gimimo_data, lytis, el_pastas, gydytojo_id))
        self.conn.commit()
        return pacientas
    
    def prideti_susitikima(self, paciento_id, gydytojo_id, susitikimo_data, paskirtis, komentarai):
        susitikimas = Susitikimas(paciento_id, gydytojo_id, susitikimo_data, paskirtis, komentarai)
        self.cursor.execute('INSERT INTO susitikimai (paciento_id, gydytojo_id, susitikimo_data, paskirtis, komentarai) VALUES (?, ?, ?, ?, ?)', (paciento_id, gydytojo_id, susitikimo_data, paskirtis, komentarai))
        self.conn.commit()
        # self.cursor.execute('SELECT susitikimo_id FROM susitikimai ORDER BY susitikimo_id DESC LIMIT 1')
        # rezultatas=self.cursor.fetchone()
        # id = rezultatas[0]
        return self.cursor.lastrowid
    
    def perziureti_irasus(self, lentele):
        self.cursor.execute(f'SELECT * FROM {lentele}')
        rezultatu_sarasas = self.cursor.fetchall() 
        print('Įrašai pagal jūsų užklausą: ')
        for rezultatas in rezultatu_sarasas:
            print(rezultatas)

    def gauti_susitikimo_info_pagal_id(self, susitikimo_id):
        self.cursor.execute('SELECT p.vardas, g.vardas, s.susitikimo_data FROM susitikimai AS s JOIN pacientai as p USING(paciento_id) JOIN gydytojai AS g USING (gydytojo_id) WHERE susitikimo_id =?', (susitikimo_id,))
        rezultatas = self.cursor.fetchone()
        return rezultatas