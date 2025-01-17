import sqlite3

# prisijungiame prie duomenų bazės
conn = sqlite3.connect('duomenu_baze.db')

# sukuriame objektą, kuris leis vykdyti užduotis

cursor = conn.cursor()

# cursor.execute('''CREATE TABLE IF NOT EXISTS zmones
#                (id INTEGER PRIMARY KEY, vardas text, amzius INTEGER)''')

# # cursor.execute("INSERT INTO zmones (vardas, amzius) VALUES(?,?)",('Jonas', 30))
# # cursor.execute("INSERT INTO zmones (vardas, amzius) VALUES(?,?)",('Petras', 40))
# # cursor.execute("INSERT INTO zmones (vardas, amzius) VALUES(?,?)",('Ona', 20))

# cursor.execute("SELECT * FROM zmones")
# rezultatai = cursor.fetchall()
# print(type(rezultatai))
# for zmogus in rezultatai:
#     print(zmogus)

# cursor.execute("SELECT * FROM zmones WHERE amzius > 25")
# print('--------------------------')
# rezultatai = cursor.fetchall()
# for zmogus in rezultatai:
#     print(zmogus)

# # tokia pati užklausa, tik naudojami kintamieji
# amzius = 25
# cursor.execute(f"SELECT * FROM zmones WHERE amzius > {amzius}")
# print('-------su kintamuoju--------------------------')
# rezultatai = cursor.fetchall()
# for zmogus in rezultatai:
#     print(zmogus)

# # tas pats, tačiau dažniau naudojamas su užklausomis (?)

# cursor.execute(f"SELECT * FROM zmones WHERE amzius > ?", (25,))
# print('----su užklausa----------------------')
# rezultatai = cursor.fetchall()
# for zmogus in rezultatai:
#     print(zmogus)

# cursor.execute("UPDATE zmones SET amzius = ? WHERE vardas = ?", (31,'Jonas'))
# cursor.execute(f"SELECT * FROM zmones WHERE amzius > ?", (25,))
# print('----su užklausa----------------------')
# rezultatai = cursor.fetchall()
# for zmogus in rezultatai:
#     print(zmogus)

# ka_istrinti = input('Iveskite varda, kuri norite istrinti: ')
# cursor.execute("DELETE FROM zmones WHERE vardas = ?", (ka_istrinti,))
# cursor.execute(f"DELETE FROM zmones WHERE vardas =  {ka_istrinti})

# cursor.execute(f"SELECT * FROM zmones WHERE amzius > ?", (25,))
# print('----su užklausa----------------------')
# rezultatai = cursor.fetchall()
# for zmogus in rezultatai:
#     print(zmogus)

# "SELECT * FROM prekes"
# "SELECT * FROM prekes WHERE category = 'turistines prekes'"

cursor.execute("""
    CREATE TABLE IF NOT EXISTS klientai(
               kliento_id INTEGER PRIMARY KEY,
               vardas VARCHAR(50) NOT NULL,
                pavarde VARCHAR(50) NOT NULL,
               el_pastas TEXT)""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS prekes(
               prekes_id INTEGER PRIMARY KEY,
               pavadinimas TEXT NOT NULL,
               kaina  REAL)""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS uzsakymai(
               uzsakymo_id INTEGER PRIMARY KEY,
               kliento_id INTEGER,
               prekes_id INTEGER,
               kiekis INTEGER,
               FOREIGN KEY (kliento_id) REFERENCES klientai(kiento_id),
               FOREIGN KEY (prekes_id) REFERENCES prekes(prekes_id))""")

# cursor.execute("INSERT INTO klientai (vardas, pavarde, el_pastas) VALUES (?,?,?)", ('Jonas', 'Jonaitis', 'jonas@jonaitis.com'))
# cursor.execute("INSERT INTO klientai (vardas, pavarde, el_pastas) VALUES (?,?,?)", ('Petras', 'Petraitis', 'petras@petraitis.com'))

# cursor.execute("INSERT INTO prekes (pavadinimas, kaina) VALUES (?,?)", ('Kava', 9.99))
# cursor.execute("INSERT INTO prekes (pavadinimas, kaina) VALUES (?,?)", ('Arbata', 4.99))

# cursor.execute("INSERT INTO uzsakymai (kliento_id, prekes_id, kiekis) VALUES (?,?,?)", (1, 1, 2))
# cursor.execute("INSERT INTO uzsakymai (kliento_id, prekes_id, kiekis) VALUES (?,?,?)", (2, 2, 5))

cursor.execute("SELECT * FROM uzsakymai")
uzsakymai = cursor.fetchall() 
for uzsakymas in uzsakymai:
    print(uzsakymas)
cursor.execute("""SELECT 
               uzsakymo_id, vardas, pavarde, pavadinimas, kiekis 
                FROM uzsakymai 
                JOIN klientai 
                ON klientai.kliento_id = uzsakymai.kliento_id
                JOIN prekes 
                ON uzsakymai.prekes_id = prekes.prekes_id""")
# uzsakymai.data = cursor.fetchall()
# output_any(uzsakymai_data, cursor)

# cursor.execute("SELECT uzsakymo_id, vardas, pavarde, pavadinimas, kiekis FROM uzsakymai JOIN klientai ON klientai.kliento_id = uzsakymai.kliento_id JOIN prekes ON uzsakymai.prekes_id = prekes.prekes_id")
uzsakymai_kliento_data = cursor.fetchall()
for uzsakymas in uzsakymai_kliento_data:
    print(uzsakymas)

try:
    cursor.execute("BEGIN TRANSACTION")
    cursor.execute("INSERT INTO klientai (vardas, pavarde, el_pastas VALUES (?,?,?),"('Antanas', 'Antanaitis', 'antanas@antanaitis.com'))
    cursor.execute("UPDATE klientai SET el_pastas = ? WHERE kliento_id =?", ('antanas@gmail.com', 3))
    conn.commit()
    print('Viskas pavyko')
except Exception as e:
    conn.rollback()
    print('Transakcija atšaukta', e)
finally:
    conn.close()

conn = sqlite3.connect('duomenu_baze.db')
cursor = conn.cursor() # antrą kartą sukuriame kursorių, nes prieš tai buvęs susijęs su sesija, kuri yra uždaryta
cursor.execute("SELECT * FROM klientai")
klientai = cursor.fetchall()
for klientas in klientai:
    print(klientas)

nauji_klientai = [
    ('Juozas', 'Juozaitis', 'juozas@juozaitis.com'),
    ('Kazys', 'Kaziauskas', 'kazys@kaziaskas.com')
]
cursor.executemany('INSERT INTO klientai (vardas, pavarde, el_pastas) VALUES (?,?,?)', nauji_klientai)

cursor.execute("SELECT * FROM klientai")
klientai = cursor.fetchall()
for klientas in klientai:
    print(klientas)
    

naujos_prekes = [
    ('masina', 20000 ),
    ('akinia', 250)
]

cursor.executemany('INSERT INTO prekes (pavadinimas, kaina) VALUES (?,?)', naujos_prekes)
cursor.execute("SELECT * FROM prekes")
prekes = cursor.fetchall()
for preke in prekes:
    print(preke)


conn.commit() # išsaugo visus duomenis
conn.close()


