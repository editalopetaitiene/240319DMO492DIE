import pytest

from parduotuve import Preke, Parduotuve

@pytest.fixture
def sukurti_parduotuve():
    parduotuve = Parduotuve()
    parduotuve.prideti_preke(Preke('Lėkštė', 5.5, 300))
    parduotuve.prideti_preke(Preke('Sąsiuvinys', 1.2, 50))
    parduotuve.prideti_preke(Preke('Tušinukas', 1.5, 100))
    return parduotuve

def test_gauti_preke(sukurti_parduotuve):
    preke = sukurti_parduotuve.gauti_preke_pagal_index(0)
    assert preke.pavadinimas == 'Lėkštė'
    assert preke.kaina == 5.5
    assert preke.kiekis == 300

def test_gauti_antra_preke(sukurti_parduotuve):
    preke = sukurti_parduotuve.gauti_preke_pagal_index(1)
    assert preke.pavadinimas == 'Sąsiuvinys'
    assert preke.kaina == 1.2
    assert preke.kiekis == 50

def test_gauti_trecia_preke(sukurti_parduotuve):
    preke = sukurti_parduotuve.gauti_preke_pagal_index(2)
    assert preke.pavadinimas == 'Tušinukas'
    assert preke.kaina == 1.5
    assert preke.kiekis == 100

def test_istrinti_preke(sukurti_parduotuve):
    pavadinimai = [preke.pavadinimas for preke in sukurti_parduotuve.prekes]
    assert 'Lėkštė' in pavadinimai
    sukurti_parduotuve.istrinti_preke(0)
    pavadinimai = [preke.pavadinimas for preke in sukurti_parduotuve.prekes]
    assert 'Lėkštė' not in pavadinimai

def test_atnaujinti_preke(sukurti_parduotuve):
    sukurti_parduotuve.atnaujinti_preke(0)
    

# def test_prideti_preke(parduotuve):
#     preke1 = Preke('Lėkštė', 5.5, 300)
#     preke2 = Preke('Sąsiuvinys', 1.2, 50)
#     preke3 = Preke('Tušinukas', 1.5, 100)
#     parduotuve.prideti_preke(preke1)
#     parduotuve.prideti_preke(preke2)
#     parduotuve.prideti_preke(preke3)
#     assert len(parduotuve.prekes) == 3
#     assert parduotuve.prekes[2] == preke3   



# def test_rikiuoti_prekes(parduotuve):
#     preke1 = Preke('Sąsiuvinys', 1.2, 50)
#     preke2 = Preke('Lėkštė', 5.5, 300)
#     preke3 = Preke('Tušinukas', 1.5, 100)

#     parduotuve.prideti_preke(preke1)
#     parduotuve.prideti_preke(preke2)
#     parduotuve.prideti_preke(preke3)

#     parduotuve.rikiuoti_pagal_savybe('pavadinimas')
#     assert len(parduotuve.prekes) == 0
#     # assert parduotuve.prekes[0] == preke2
#     # assert parduotuve.prekes[1] == preke1
#     # assert parduotuve.prekes[2] == preke3