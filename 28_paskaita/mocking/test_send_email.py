from send_email import pranesti_vartotojui, skaiciavimas, nuskaityti_faila, apskaiciuoti_suma, apskaiciuoti_vidurkis, zodziu_skaicius, unikalios_reiksmes, patvirtinti_apmokejima, patvirtinti_apmokejima_ar_yra, saraso_suma_2

# from pytest_mock import mock_open
from unittest.mock import patch, mock_open
import pytest 

@pytest.fixture
def mock_send_email():
    with patch ('send_email.send_email') as mock_send_email:
        yield mock_send_email # yield galii gražinti ne viena karta

def test_pranesti_vartotoju(mock_send_email):
    email = 'siuntejas@gmail.com'
    ivykis = 'Susitikimas'
    pranesti_vartotojui(email, ivykis)
    mock_send_email.assert_called_once() # testuoja ar mokinama funkcija buvo išjviesta tik viena karta
    args, _ = mock_send_email.call_args # gražins ne viena atsakymą, o [], <..>
    # assert kwargs == {}
    assert args[0] == 'antanas@gmail.com'
    assert len(args)==4
    assert ivykis in args[3]

@pytest.fixture
def mock_daugyba():
    with patch ('send_email.daugyba') as mocked_daugyba: # patch užtikrins, kad bus sukurta įvykio dbjektas (istorija) iš kurio galėsime pasiimti veiksmus/ užtikrins, kad funkcija bus iškviečiama
        yield mocked_daugyba

def test_skaiciavimas(mock_daugyba):
    skaiciavimas (1,1)
    mock_daugyba.assert_not_called()
    skaiciavimas(2,5)
    mock_daugyba.assert_called_once

from pytest_mock import mocker

@pytest.fixture
def test_nuskaityti_faila(mocker):
    mocker.patch('builtins.open', mock_open(read_data='čia yra tekstas, kurį mes teigiam, kad nuskaitė open' ))
    rezultatas_kurio_tikimės = 'čia yra tekstas, kurį mes teigiam, kad nuskaitė open' 
    rezultatas = nuskaityti_faila('tekstas.txt')
    assert rezultatas_kurio_tikimės == rezultatas

@pytest.fixture
def uzpildyti_skaicius():
    sarasas = [1,2,3,4,5]
    return sarasas

def test_apskaiciuoti_suma(uzpildyti_skaicius):
    assert apskaiciuoti_suma(uzpildyti_skaicius) == 15

@pytest.fixture
def sukurti_sarasa1():
    sarasas =[1,5,2,3,4,5]
    return sarasas
@pytest.fixture
def sukurti_sarasa2():
    sarasas =[10,20,30,40,50]
    return sarasas
@pytest.fixture
def sukurti_sarasa3():
    sarasas =[0.1, 0.5, 0.8, 40,50]
    return sarasas

def test_apskaiciuoti_vidurkis(sukurti_sarasa1, sukurti_sarasa2, sukurti_sarasa3):
    assert apskaiciuoti_vidurkis(sukurti_sarasa1) == sum(sukurti_sarasa1)/len(sukurti_sarasa1)
    assert apskaiciuoti_vidurkis(sukurti_sarasa2) == sum(sukurti_sarasa2)/len(sukurti_sarasa2)
    assert apskaiciuoti_vidurkis([1, 2, 10, 'k']) == 'klaida'
    assert apskaiciuoti_vidurkis(sukurti_sarasa3) == sum(sukurti_sarasa3)/len(sukurti_sarasa3)


@pytest.fixture
def tekstas():
    tekstas = ['Šiandien', 'yra', 'penktadienis', 'jau', 'beveik', 'savaitgalis']
    return tekstas

@pytest.fixture
def tekstas1():
    tekstas = 'šiandien  yra penktadienis, jau beveik savaitgalis'
    return tekstas

def test_zodziu_skaicius(tekstas1):
    tiketinas_rezultatas = zodziu_skaicius(tekstas1)
    assert tiketinas_rezultatas == 6

def test_unikalios_reiksmes(sukurti_sarasa1):
    tiketinas_rezultatas = unikalios_reiksmes(sukurti_sarasa1)
    assert tiketinas_rezultatas == [1,5,2,3,4,]
    
def test_patvirtinti_apmokejima():
    assert patvirtinti_apmokejima('LT5555', 290) == True
    assert patvirtinti_apmokejima('LT5555', 4000) == False
    assert patvirtinti_apmokejima('EE4532', 500) == False

@pytest.fixture
def mock_patvirtinti_apmokejima_atsakymas():
    return True

@patch ('send_email.patvirtinti_apmokejima')
def test_patvirtinti_apmokejima_ar_yra(mock_patvirtinti_apmokejima):
    mock_patvirtinti_apmokejima.return_value = False
    # mock_patvirtinti_apmokejima.return_value = mock_patvirtinti_apmokejima_atsakymas
    assert patvirtinti_apmokejima_ar_yra('LT5433', 259)== "Banko sąskaita LT5433 negali atlikti mokėjimą"

def test_saraso_suma_2():
    duomenys = [1, 'a']
    with pytest.raises(Exception) as e:
        saraso_suma_2(duomenys)
    # assert e == 'Saraso nariai privalo būti skaičiai'
    
