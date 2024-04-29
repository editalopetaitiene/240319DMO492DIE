from datetime import datetime
class Gyvunas:
    def __init__(self,  vardas, rusis, metai, svoris):
        self.vardas = vardas
        self.rusis = rusis
        self.gimimo_metai = metai
        self.svoris = svoris
        self.amzius = self.apskaiciuoti_amziu(metai)

    def apskaiciuoti_amziu(self, metai):
        today = datetime.now()
        return today.year - metai

class GyvunuValdymas:
    def __init__(self, pavadinimas):
        self.gyvunai = []
        self.pavadinimas = pavadinimas
        

    def prideti_gyvuna(self, gyvunas):
        self.gyvunai.append(gyvunas)
        
    def gauti_pavadinimus(self):
        return [gyvunas.vardas for gyvunas in self.gyvunai]

    def gauti_gyvunus_pagal_rusi(self, gyvuno_rusis):
        # return [gyvunas for gyvunas in self.gyvunai if gyvunas.rusis == gyvuno_rusis]
        gyvunai = []
        for gyvunas in self.gyvunai:
            if gyvunas.rusis == gyvuno_rusis:
                gyvunai.append(gyvunas)
        return gyvunai

    
    def gauti_gyvunus_pagal_svori(self, gyvuno_svoris):
        return [gyvunas for gyvunas in self.gyvunai if gyvunas.svoris == gyvuno_svoris]

gyvunas1 = Gyvunas('Luna', 'šuo', 2020, 34)
prieglauda1 = GyvunuValdymas('Keturkojis')
prieglauda2 = GyvunuValdymas('Augintinis')

prieglauda1.prideti_gyvuna(gyvunas1)
prieglauda1.prideti_gyvuna(Gyvunas('Garfildas', 'katė', 2022, 4))
print(prieglauda1.gyvunai[0].vardas)
gyvunai = prieglauda1.gauti_gyvunus_pagal_rusi('šuo')
print(gyvunai)



# Sukurkite klasę Gyvūnas, suteikite jai keletą properties (amzius, rusis, vardas, svoris arba savo nuožiūra)
# Sukurkite antrą klasę GyvūnųPrieglauda
# Ši klasė turi turėti metodus pridėti naujus gyvūnus, taip pat gauti gyvūnus gal rūšį (pvz. matyti tik kates), pagal svorį

# class Receptas:
#     def __init__(self, pavadinimas, ruosimo_laikas):
#         self.pavadinimas = pavadinimas
#         self.ruosimo_laikas = ruosimo_laikas

# class ReceptuValdymas:
#     def __init__(self):
#         self.receptai = []

#     def prideti_recepta(self, receptas):
#         self.receptai.append(receptas)

#     def gauti_receptus_pagal_laika(self, maksimalus_laikas):
#         return [receptas for receptas in self.receptai if receptas.ruosimo_laikas <= maksimalus_laikas]