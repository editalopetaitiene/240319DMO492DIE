class Motociklas():
    def __init__ (self, marke, modelis, metai):
        self.marke = marke
        self.modelis = modelis
        self.metai = metai

    def užkurti(self):
        print(f"motociklas {self.marke} {self.modelis} buvo užkurtas")

motociklas1 = Motociklas('KTM', 'EXC450', 2016)
print(motociklas1.marke)
print(motociklas1.modelis)
print(motociklas1.metai)

motociklas1.užkurti()

motociklas2 = Motociklas('Suzuki', 'DR400Z', 2006)
motociklas2.užkurti()

# print(motociklas1['marke'])
motociklas = {'marke':'Honda', 'modelis':'CRF250', 'metai': 2018}
print(motociklas['modelis'])

print(type(motociklas))
zodis = 'labas'
print(type(zodis))
zodis=zodis.upper()
print(zodis)

skaicius = 5

print(type(motociklas))

print(type(motociklas1))
# ___________________________
tv_kanalai = [
    {"pavadinimas":"LRT", "programos" : [{"savaites_diena":1, "laidos" : [{"laikas":"8:00", "pavadinimas":"Gustavo enciklopedija", "dalyviai": [{'vardas':"Gustavas"}]}]}]}
]
print(tv_kanalai[0]['programos'][0]['laidos'][0]['dalyviai'][0])