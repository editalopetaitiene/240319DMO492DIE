import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_get_todo():
    response = requests.get('https://jsonplaceholder.typicode.com/todos/1')
    assert response.status_code == 200
    data = response.json()
    # print(data)   # print(type(response.json()))
    assert data['userId']==1
    assert 'title' in data
    assert 'delectus' in data['title']
    print('OK')

test_get_todo()

# def test_puslapis():
#     driver = webdriver.Chrome()
#     driver.get('https://delfi.lt')
#     elementas = driver.find_element(By.CLASS_NAME, 'C-button__content')
#     tekstas = elementas.text
#     assert 'Prenumeruoti' in tekstas
#     assert 'Delfi' in driver.title
#     print('Delfi nuskaitymas baigtas')
#     driver.quit()

# test_puslapis()


# def test_aruodas():
#     driver = webdriver.Chrome()
#     driver.get('https://www.aruodas.lt/butai/vilniuje/')
#     kainos = driver.find_elements(By.CLASS_NAME, 'list-item-price-v2')
#     plotai = driver.find_elements(By.CLASS_NAME, 'list-AreaOverall-v2')
#     plotu_reiksmes = []
#     kainos_reiksmes = []
#     for kaina in kainos:
#         kainos_reiksmes.append(kaina.text)
#     # print(kainos_reiksmes)
#     # print('________________')
#     # print(len(kainos_reiksmes))
#     assert not kainos_reiksmes == []
#     assert len(kainos_reiksmes) == 25
#     for kaina in kainos_reiksmes:
#         # assert kaina[-1] == '€'
#         assert kaina.endswith('€')

#     for plotas in plotai:
#         plotu_reiksmes.append(plotas.text)
#     plotu_sarasas = plotu_reiksmes[2:]
#     print(plotu_sarasas)
#     assert not plotu_sarasas == []
#     assert len(plotu_sarasas) == 25
#     for plotas in plotu_sarasas: 
#         assert(plotas.replace('.', '').isnumeric())
#         # print(plotas.isnumeric())
#         # assert plotas isnumeric
#         # assert plotas.isnumeric(), f"{plotas}"

#     driver.quit()
# test_aruodas()
# 1 užduotis
# naudojant selenium parašykite testą, kuris bandytų nuskaityti informaciją iš jūsų pasirinkto puslapio
# "ištraukite keletą elementų iš puslapio" ir testuokite ar juose  yra tekstas, kurio jūs tikitės

def test_autoplius():
    driver = webdriver.Chrome()
    driver.get('https://m.autoplius.lt/skelbimai/naudoti-automobiliai?qt=')
    modeliai = driver.find_elements(By.CLASS_NAME, 'title-content')
    modeliu_reiksmes = []
    for modelis in modeliai:
        modeliu_reiksmes.append(modelis.text)
    assert not modeliu_reiksmes == []
    assert len(modeliu_reiksmes) == 20
    # print(type(modeliu_reiksmes))
    # print(len(modeliu_reiksmes))
    
    kuro_tipas = driver.find_elements(By.CLASS_NAME, 'item-parameters')
    kuro_tipai = []
    for tipas in kuro_tipas:
        kuro_rusis = tipas.text.split('\n')[0]
        kuro_tipai.append(kuro_rusis)
    print(type(kuro_tipai))
    print(kuro_tipai)
    print('OK')
    driver.quit()

test_autoplius()

# def test_is_numeric():
#     skaicius = '15.65'
#     print(skaicius .replace('.', '')) 

#     print(skaicius)

# test_is_numeric()

