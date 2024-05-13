# Jūsų užsakovas yra smulkus autoservisas, kuriam yra reikalinga registracijos sistema
# Autoservisas nori kaupti informaciją apie:

    # 1. Mechanikus:
        # 1. vardas
        # 2. pavardė
        # 3. el_paštas
        # 4. valandinis_atlyginimas
        # 5. specializacija (elektra/važiuoklė/variklis/kėbulai)

    # 2. Klientus:
        # 1. vardas
        # 2. pavardė
        # 3. el_paštas

    # 3. Klientų automobilius:
        # 1. Valstybinis numeris
        # 2. Markė
        # 3. Modelis
        # 4. Savininkas

    # 4. Remontus:
        # 1. kliento_id
        # 2. mechaniko_id
        # 3. darbo_pradzia
        # 4. darbo_pabaiga
        # 5. darbo kaina (darbo_pabaiga - darbo_pradzia) x mechaniko valandinis įkainis x 2 (autoserviso dalis)
        # 6. remonto_kategorija (1)

# jums taip pat reikės lentelės autoservisas, kuriame bus laikoma visa informacija.

# turint šias žinias jums reikės sukurti sistemą, valdomą per terminalą, vartotojas įjungęs aplikaciją, gali pasirinkti šiuos žingsnius:

# 1. pridėti:
    # 1. mechaniką
    # 2. klientą
    # 3. kliento automobilį
    # 4. remontą

# 2. parodyti visus:
    # 1. mechanikus
    # 2. klientus
    # 3. klientų automobilus
    # 4. remontus

# papildomos užduotys, jas iškviesti reikia terminale nurodant veiksmo numerį/įvedant skaičių:

# patobulinkite funkciją, kuri prieš pridedant remontą patikrintų ar tuo metu, kai klientas pageidauja remontuoti automobilį yra laisvų automechanikų
# sukurkite funkciją, kuri apskaičiuotų, kiek vienas klientas yra mums sumokėjęs iš viso už visų savo automobilių visus remontus
# sukurkite funkciją, kuri apskaičiuotų, kiek vienas klientas yra mums sumokėjęs iš viso už vieno konkretaus automobilio remontą
# sukurkite funkciją, kuri apskaičiuotų kiek uždirbo konkretus mechanikas X

