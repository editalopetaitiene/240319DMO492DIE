# 1. sukurkite duomenų bazę, kurioje turėtų būti šios lentelės: gydytojai, pacientai, susitikimai
import sqlite3
conn = sqlite3.connect('duomenu_baze_medicina.db')
cursor = conn.cursor()
# 1. Gydytojai:
    # ID (unikalus)
    # Vardas
    # Pavardė
    # Specializacija
    # Kontaktinė informacija (el. paštas)
cursor.execute('''CREATE TABLE IF NOT EXISTS gydytojai
              (gydytojo_id INTEGER PRIMARY KEY, 
               vardas VARCHAR(50) NOT NULL, 
               pavarde VARCHAR(50) NOT NULL,
               specializacija text, 
               el_pastas text)''')

# 2. Pacientai:
    # ID (unikalus)
    # Vardas
    # Pavardė
    # Gimimo data
    # Lytis
    # Kontaktinė informacija (el. paštas)
    # Gydytojo ID (susiejimas su gydytoju, pvz. šeimos gydytojas)
cursor.execute('''CREATE TABLE IF NOT EXISTS pacientai
                (paciento_id INTEGER PRIMARY KEY, 
                vardas VARCHAR(50) NOT NULL, 
                pavarde VARCHAR(50) NOT NULL,
                gimimo_data TEXT, 
                lytis TEXT, 
                el_pastas TEXT,
                gydytojo_id INTEGER,
                FOREIGN KEY (gydytojo_id) REFERENCES gydytojai(gydytojo_id))''')
# 3. Susitikimai:
    # ID
    # Paciento ID
    # Gydytojo ID
    # Susitikimo data ir laikas
    # Susitikimo paskirtis/arba diagnozė
    # Komentarai/arba pastabos
cursor.execute('''CREATE TABLE IF NOT EXISTS susitikimai
               (susitikimo_id INTEGER PRIMARY KEY, 
               paciento_id INTEGER,
               gydytojo_id INTEGER,
               susitikimo_data_laikas TEXT,
               susitikimo_paskirtis_diagnoze TEXT,
               komentarai_pastabos TEXT,
               FOREIGN KEY (paciento_id) REFERENCES pacientai(paciento_id),
               FOREIGN KEY (gydytojo_id) REFERENCES gydytojai(gydytojo_id))''')

# 2. Užpildykite šias lenteles duomenimis (bent 10 įrašų kiekvienai lentelei)
# cursor.execute("INSERT INTO gydytojai (vardas, pavarde, specializacija, el_pastas) VALUES(?,?,?,?)",('Jonas', 'Jonaitis', 'chirurgas', 'jonas@jonaitis.com'))
# cursor.execute("INSERT INTO gydytojai (vardas, pavarde, specializacija, el_pastas) VALUES(?,?,?,?)",('Petras', 'Petraitis', 'šeimos gydytojas', 'petras@petraitis.com'))
# cursor.execute("INSERT INTO gydytojai (vardas, pavarde, specializacija, el_pastas) VALUES(?,?,?,?)",('Antanas', 'Antanaitis', 'ortopedas', 'Antanas@antanaitis.com'))
# cursor.execute("INSERT INTO gydytojai (vardas, pavarde, specializacija, el_pastas) VALUES(?,?,?,?)",('Ona', 'Onauskaitė', 'stomatologas', 'ona@onauskaite.com'))
# cursor.execute("INSERT INTO gydytojai (vardas, pavarde, specializacija, el_pastas) VALUES(?,?,?,?)",('Marytė', 'Marijauskaitė', 'vaikų gydytojas', 'maryte@marijauskaite.com'))
# cursor.execute("INSERT INTO gydytojai (vardas, pavarde, specializacija, el_pastas) VALUES(?,?,?,?)",('Joana', 'Jonyte', 'ginekologas', 'joana@jonyte.com'))
# cursor.execute("INSERT INTO gydytojai (vardas, pavarde, specializacija, el_pastas) VALUES(?,?,?,?)",('Tadas', 'Tadauskas', 'stomatologas', 'ona@onauskaite.com'))
# cursor.execute("INSERT INTO gydytojai (vardas, pavarde, specializacija, el_pastas) VALUES(?,?,?,?)",('Mindaugas', 'Mindaugaskas', 'chirurgas', 'ona@onauskaite.com'))
# cursor.execute("INSERT INTO gydytojai (vardas, pavarde, specializacija, el_pastas) VALUES(?,?,?,?)",('Gintaras', 'Gintarauskas', 'šeimos gydytojas', 'ona@onauskaite.com'))
# cursor.execute("INSERT INTO gydytojai (vardas, pavarde, specializacija, el_pastas) VALUES(?,?,?,?)",('Vytautas', 'Vytautauskas', 'kardiologas', 'ona@onauskaite.com'))

# cursor.execute("INSERT INTO pacientai (vardas, pavarde, gimimo_data, lytis, el_pastas) VALUES(?,?,?,?,?)", ('Kazys', 'Kazimierauskas', '1999-09-22', 'vyras', 'kazys@kazimieraskas.com'))
# cursor.execute("INSERT INTO pacientai (vardas, pavarde, gimimo_data, lytis, el_pastas) VALUES(?,?,?,?,?)", ('Stasys', 'Stasauskas', '1976-08-20', 'vyras', 'stasys@stasauskas.com'))
# cursor.execute("INSERT INTO pacientai (vardas, pavarde, gimimo_data, lytis, el_pastas) VALUES(?,?,?,?,?)", ('Kazys1', 'Kazimierauskas1', '1951-09-22', 'vyras', 'kazys1@kazimieraskas1.com'))
# cursor.execute("INSERT INTO pacientai (vardas, pavarde, gimimo_data, lytis, el_pastas) VALUES(?,?,?,?,?)", ('Kazys2', 'Kazimierauskas2', '1995-09-22', 'vyras', 'kazys2@kazimieraskas2.com'))
# cursor.execute("INSERT INTO pacientai (vardas, pavarde, gimimo_data, lytis, el_pastas) VALUES(?,?,?,?,?)", ('Kazys3', 'Kazimierauskas3', '1989-09-22', 'vyras', 'kazys3@kazimieraskas3.com'))
# cursor.execute("INSERT INTO pacientai (vardas, pavarde, gimimo_data, lytis, el_pastas) VALUES(?,?,?,?,?)", ('Kazys4', 'Kazimierauskas4', '1959-09-22', 'vyras', 'kazys4@kazimieraskas4.com'))
# cursor.execute("INSERT INTO pacientai (vardas, pavarde, gimimo_data, lytis, el_pastas) VALUES(?,?,?,?,?)", ('Kazys5', 'Kazimierauskas5', '1964-09-22', 'vyras', 'kazys5@kazimieraskas5.com'))
# cursor.execute("INSERT INTO pacientai (vardas, pavarde, gimimo_data, lytis, el_pastas) VALUES(?,?,?,?,?)", ('Kazys6', 'Kazimierauskas6', '1989-09-22', 'vyras', 'kazys6@kazimieraskas6.com'))
# cursor.execute("INSERT INTO pacientai (vardas, pavarde, gimimo_data, lytis, el_pastas) VALUES(?,?,?,?,?)", ('Kazys7', 'Kazimierauskas7', '1981-09-22', 'vyras', 'kazys7@kazimieraskas7.com'))
# cursor.execute("INSERT INTO pacientai (vardas, pavarde, gimimo_data, lytis, el_pastas) VALUES(?,?,?,?,?)", ('Kazys8', 'Kazimierauskas8', '1952-09-22', 'vyras', 'kazys8@kazimieraskas8.com'))
# cursor.execute("INSERT INTO pacientai (vardas, pavarde, gimimo_data, lytis, el_pastas) VALUES(?,?,?,?,?)", ('Kazys9', 'Kazimierauskas9', '1992-09-22', 'vyras', 'kazys9@kazimieraskas9.com'))

# cursor.execute("INSERT INTO susitikimai (paciento_id, gydytojo_id, susitikimo_data_laikas, susitikimo_paskirtis_diagnoze, komentarai_pastabos) VALUES (?,?,?,?,?)", (1, 4, '2024-04-28 10.30', 'burnos higiena', 'atlikta'))
# cursor.execute("INSERT INTO susitikimai (paciento_id, gydytojo_id, susitikimo_data_laikas, susitikimo_paskirtis_diagnoze, komentarai_pastabos) VALUES (?,?,?,?,?)", (2, 1, '2024-04-28 10.30', 'burnos higiena', 'atlikta'))
# cursor.execute("INSERT INTO susitikimai (paciento_id, gydytojo_id, susitikimo_data_laikas, susitikimo_paskirtis_diagnoze, komentarai_pastabos) VALUES (?,?,?,?,?)", (3, 2, '2024-04-28 10.30', 'burnos higiena', 'atlikta'))
# cursor.execute("INSERT INTO susitikimai (paciento_id, gydytojo_id, susitikimo_data_laikas, susitikimo_paskirtis_diagnoze, komentarai_pastabos) VALUES (?,?,?,?,?)", (5, 3, '2024-04-28 10.30', 'burnos higiena', 'atlikta'))
# cursor.execute("INSERT INTO susitikimai (paciento_id, gydytojo_id, susitikimo_data_laikas, susitikimo_paskirtis_diagnoze, komentarai_pastabos) VALUES (?,?,?,?,?)", (1, 4, '2024-04-28 10.30', 'burnos higiena', 'atlikta'))
# cursor.execute("INSERT INTO susitikimai (paciento_id, gydytojo_id, susitikimo_data_laikas, susitikimo_paskirtis_diagnoze, komentarai_pastabos) VALUES (?,?,?,?,?)", (4, 5, '2024-04-28 10.30', 'burnos higiena', 'atlikta'))
# cursor.execute("INSERT INTO susitikimai (paciento_id, gydytojo_id, susitikimo_data_laikas, susitikimo_paskirtis_diagnoze, komentarai_pastabos) VALUES (?,?,?,?,?)", (6, 6, '2024-04-28 10.30', 'burnos higiena', 'atlikta'))
# cursor.execute("INSERT INTO susitikimai (paciento_id, gydytojo_id, susitikimo_data_laikas, susitikimo_paskirtis_diagnoze, komentarai_pastabos) VALUES (?,?,?,?,?)", (7, 7, '2024-04-28 10.30', 'burnos higiena', 'atlikta'))
# cursor.execute("INSERT INTO susitikimai (paciento_id, gydytojo_id, susitikimo_data_laikas, susitikimo_paskirtis_diagnoze, komentarai_pastabos) VALUES (?,?,?,?,?)", (9, 8, '2024-04-28 10.30', 'burnos higiena', 'atlikta'))
# cursor.execute("INSERT INTO susitikimai (paciento_id, gydytojo_id, susitikimo_data_laikas, susitikimo_paskirtis_diagnoze, komentarai_pastabos) VALUES (?,?,?,?,?)", (8, 9, '2024-04-28 10.30', 'burnos higiena', 'atlikta'))

# print('_________pacientai____________')
# cursor.execute("SELECT * FROM pacientai")
# pacientai = cursor.fetchall() 
# for pacientas in pacientai:
#     print(pacientas)
# print('_________gydytojai____________')
# cursor.execute("SELECT * FROM gydytojai")
# gydytojai = cursor.fetchall() 
# for gydytojas in gydytojai:
#     print(gydytojas)

# print('_________susitikimai____________')
# cursor.execute("SELECT * FROM susitikimai")
# susitikimai = cursor.fetchall() 
# for susitikimas in susitikimai:
#     print(susitikimas)
# 3. Atlikite šias užklausas:

    # 1. Visi pacientai, kurių gimimo data yra mažiau nei 1970-01-01 turėtų būti priskirti gydytojui, kurio ID yra 1
cursor.execute(f"UPDATE pacientai SET gydytojo_id = 1 WHERE gimimo_data '1970-01-01'")
cursor.execute(f"SELECT * FROM pacientai WHERE gimimo_data < '1970-01-01'AND gydytojo_id = 1 ")
print('----- pacientai, kurių gimimo data yra mažiau nei 1970-01-01----- ')
rezultatai = cursor.fetchall()
for pacientas in rezultatai:
    print(pacientas)

    # 2. Raskite visus susitikimus, kurie vyksta šiandien. (rezultate norime matyti kliento vardą ir pavardę, gydytojo vardą ir pavardę ir susitikimo paskirtį)
    # 3. Sukurkite užklausą, kuri ištrintų visus susitikimus, kurie įvyko daugiau nei 6 mėnesiai nuo šiandienos datos.
    # 4. Parašykite užklausą, kuri rastų gydytojų vardus ir pavardes, kuriems yra priskirti pacientai, kurių susitikimo paskirtyje yra žodis "trauma"
    # 5. Raskite visus pacientus, kurių gydytojo specializacija yra chirurgija ir susitikimo paskirtis yra operacija.



conn.commit() # išsaugo visus duomenis
conn.close()