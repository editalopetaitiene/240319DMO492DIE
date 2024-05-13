class Gyvunas:
    def __init__(self, vardas, amzius, svoris, ):
        self.vardas = vardas
        self.amzius = amzius 
        self.soris = svoris

class Prieglauda:
    def __init__(self):
        self.gyvunu_sarasas = []
        print(self.gyvunu_sarasas)

    def prideti_gyvuna(self, gyvunas):
        self.gyvunu_sarasas.append(gyvunas)

    def istrinti_gyvuna(self, vardas):
        neistrinti = []
        for gyvunas in self.gyvunu_sarasas:
            if vardas != gyvunas.vardas:
                neistrinti.append(gyvunas)
        self.gyvunu_sarasas = neistrinti

    def atrinti_pagal_amziu(self, amzius):
        atrinkti = []
        for gyvunas in self.gyvunu_sarasas:
            if amzius == gyvunas.amzius:
                atrinkti.append(gyvunas)
        return atrinkti
    
gyvunai = [{'vardas':'Brisius', 'amzius': 10}, {'vardas':'kate','amzius':5}]
skaicius = 1

prieglauda1 = Prieglauda()
prieglauda2 = Prieglauda()

gyvunas1 = Gyvunas('Kingas', 4, 2)
gyvunas2 = Gyvunas('Džeris', 10, 15)
# gyvunas3 = {
#     'vardas':'Espero',
#     'amzius': 5,
#     'svoris': 2
# }
prieglauda1.prideti_gyvuna(gyvunas1)
prieglauda1.prideti_gyvuna(gyvunas2)
rezultatas = prieglauda1
print(prieglauda1.gyvunu_sarasas)
prieglauda1.gyvunu_sarasas.append(gyvunas1)
prieglauda1.gyvunu_sarasas.append(gyvunas2)
print('ištrintas: ')
print(prieglauda1.istrinti_gyvuna('Kingas'))
print('atrinktas: ')
print(prieglauda1.atrinti_pagal_amziu(10))
# prieglauda1.gyvunu_sarasas.append(gyvunas3)
# print(prieglauda1.gyvunu_sarasas.extend([gyvunas1, gyvunas2])) # extend kaip ir append prideda prie sarašo, bet galima pridėti po kelis

# prieglauda1.gyvunu_sarasas.extend([gyvunas1, gyvunas2])# extend kaip ir append prideda prie sarašo, bet galima pridėti po kelis

# print(prieglauda1.gyvunu_sarasas) 
print('___________________________________')
for gyvunas in prieglauda1.gyvunu_sarasas:
    print(gyvunas.vardas)


print(prieglauda1.gyvunu_sarasas[0].vardas)
print(type(prieglauda1.gyvunu_sarasas[0].vardas))


