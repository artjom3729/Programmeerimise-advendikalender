sundmused = """Naaber viib prügikoti välja: 0
Naaber kaevab midagi tagahoovis: 5
Naaber kannab raskeid kotte autosse: 2
Naaber lohistab suurt musta kotti keldrisse: 10
Naaber vaatab pikalt aknast välja: 7
Naaber viib hilisõhtul midagi autosse: 4
Naaber grillib keset talve: 1
Naaber paneb keset päeva kardinad kinni: 6
Naaber lahkub hilisõhtul majast: 3
Naabril käivad pidevalt külalised, kes kauaks ei jää: 7
Naaber väldib teisi naabreid: 5
Naaber jalutab oma koera: -1
Naaber parandab oma aeda: -3
Naaber kaunistab maja: -2
Naaber on alati sõbralik: -5
Naaber laenab suhkrut, et piparkooke küpsetada: 0"""

naabrid = """0: Naaber on alati sõbralik, Naaber vaatab pikalt aknast välja, Naaber jalutab oma koera, Naaber viib prügikoti välja, Naaber vaatab pikalt aknast välja
1: Naaber parandab oma aeda, Naaber kaunistab maja, Naaber grillib keset talve
2: Naaber lahkub hilisõhtul majast, Naabril käivad pidevalt külalised, kes kauaks ei jää, Naaber kannab raskeid kotte autosse, Naaber väldib teisi naabreid
3: Naaber väldib teisi naabreid, Naaber väldib teisi naabreid
4: Naaber kaunistab maja, Naaber viib hilisõhtul midagi autosse, Naaber viib prügikoti välja"""

naabrid = naabrid.replace(", N", "; N")

sundmuste_dict = {}

for line in sundmused.strip().splitlines():
    sundmus, number = line.split(':', 1)
    sundmuste_dict[sundmus.strip()] = int(number.strip())

naabrid = naabrid.strip().splitlines()

naabrid_list = []

for line in naabrid:
    _, tegevused = line.split(':')
    tegevuste_list = [tegevus.strip() for tegevus in tegevused.split(';')]
    naabrid_list.append(tegevuste_list)

naabrite_skoorid = []

for naaber in naabrid_list:
    naabri_skoor = 0
    for n in naaber:
        naabri_skoor += sundmuste_dict[n]
    naabrite_skoorid.append(naabri_skoor)

kahtlased_naabrid = 0

for n in naabrite_skoorid:
    if n > 10:
        kahtlased_naabrid += 1
    
print(kahtlased_naabrid)


