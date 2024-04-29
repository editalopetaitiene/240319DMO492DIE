import pytest
from receptai.receptu_valdymas import Receptas, ReceptuValdymas

@pytest.fixture
def receptu_valdymas():
    valdymas = ReceptuValdymas()
    valdymas.prideti_recepta(Receptas('Cepelinai', 180, ['bulvės', 'mėsa']))
    valdymas.prideti_recepta(Receptas('Cezario salotos', 30, []))
    valdymas.prideti_recepta(Receptas('Karbonadas', 45, []))
    return valdymas

def test_gauti_receptus_pagal_laika(receptu_valdymas):
    rezultatas = receptu_valdymas.gauti_receptus_pagal_laika(30)
    print(rezultatas)
    pavadinimai = [receptas.pavadinimas for receptas in rezultatas]
    assert pavadinimai == ['Cezario salotos']
    assert 'Karbonadas' not in pavadinimai

def test_pasalinti_recepta(receptu_valdymas):
    receptu_valdymas.pasalinti_recepta('Cepelinai')
    assert 'Cepelinai' not in [receptas.pavadinimas for receptas in receptu_valdymas.receptai] 

def test_gauti_receptus_pagal_zodi(receptu_valdymas):
    receptai_pagal_zodi = receptu_valdymas.gauti_receptus_pagal_zodi('Karbonadas')
    assert receptai_pagal_zodi== ['Karbonadas']
    
 
def test_gauti_bendra_ruosimo_laika(receptu_valdymas):
    assert receptu_valdymas.gauti_bendra_ruosimo_laika() == 255   

def test_atrinti_pagal_ingredintus(receptu_valdymas):
    tikimes_rezultato = receptu_valdymas.receptai[0]
    assert receptu_valdymas.atrinti_pagal_ingredintus('bulvės') == [tikimes_rezultato]

def test_isvalyti_receptus(receptu_valdymas):
    receptu_valdymas.isvalyti_receptus()
    assert receptu_valdymas.receptai == []

def test_isvalyti_receptus_2(receptu_valdymas):
    receptu_valdymas.isvalyti_receptus_2()
    assert receptu_valdymas.receptai == []
