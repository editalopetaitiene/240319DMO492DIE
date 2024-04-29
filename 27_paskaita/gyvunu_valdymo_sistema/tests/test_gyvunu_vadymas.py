import pytest
from gyvunai.gyvunu_valdymas import Gyvunas, GyvunuValdymas

@pytest.fixture
def gyvunu_valdymas():
    valdymas = GyvunuValdymas()
    valdymas.prideti_gyvuna(Gyvunas('Arčis', 'šuo', '4 m.', 38))
    valdymas.prideti_gyvuna(Gyvunas('Luna', 'šuo', '4 m.', 34))
    valdymas.prideti_gyvuna(Gyvunas('Garfildas', 'katė', '3 m.', 4))
    return valdymas

# gyvunas1 = Gyvunas('Luna', 'šuo', 2020, 34)
# prieglauda1 = GyvunuValdymas('Keturkojis')
# prieglauda2 = GyvunuValdymas('Augintinis')

# prieglauda1.prideti_gyvuna(gyvunas1)
# prieglauda1.prideti_gyvuna(Gyvunas('Garfildas', 'katė', 2022, 4))
# print(prieglauda1.gyvunai[0].vardas)
# gyvunai = prieglauda1.gauti_gyvunus_pagal_rusi('šuo')
# print(gyvunai)


def test_gauti_gyvunus_pagal_rusi(gyvunu_valdymas):
    sunys = gyvunu_valdymas.gauti_gyvunus_pagal_rusi('šuo')
    kates = gyvunu_valdymas.gauti_gyvunus_pagal_rusi('katė')
    assert sunys == [gyvunu_valdymas.gyvunai[0]]
    assert len(sunys) ==1
    assert len(gyvunu_valdymas.gyvunai ==2)
    assert kates == [gyvunu_valdymas.gyvunai[2]]


  