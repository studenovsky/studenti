# zaci.py - program načte ze souboru zaci.txt seznam žáků a jejich křestních jmen a příjmení, vytiskne seznam žáků s hvězdičkami mezi křestními jmény a příjmením a příjmením, vytiskne jméno s největším zastoupením a vytiskne žáka s největším počtem jmen
# Autor: Jaroslav Studenovský <studenovskyj@jirovcovka.net>

# Definování proměnných
zaci = {}
pocty_krestni = {}
max_hvezdicky = 0
nejvice_jmen = ""
fd = open("zaci.txt", "r")

# čtení jednoho řádku ze souboru
for line in fd:
    jmeno_list = line.strip().split()
    prijmeni = jmeno_list.pop(-1)
    zaci[prijmeni]= "*".join(jmeno_list)
    hvezdicky = zaci[prijmeni].count("*")

    # najít člověka s největším počtem jmen(=počet hvezdicky + 1)
    if hvezdicky > max_hvezdicky:
        max_hvezdicky = hvezdicky
        nejvice_jmen = zaci[prijmeni].replace("*", " ")

# výpis záznamů s oddělovačem * a -
for prijmeni in zaci.keys():
    print(f"*{zaci[prijmeni]}*-{prijmeni}-")

# výpis počtu žáků se stejným křestním jménem
    if zaci[prijmeni] in pocty_krestni:
        pocty_krestni[zaci[prijmeni]] += 1
    else:
        pocty_krestni[zaci[prijmeni]] = 1

# najít jméno s největším zastoupením
nejcastejsi_jmeno = max(pocty_krestni, key=pocty_krestni.get)
print(f"\nJméno s největším zastoupením je {nejcastejsi_jmeno} s počtem {pocty_krestni[nejcastejsi_jmeno]}")

# výpis člověka s největším počtem jmen
print(f"\nNejvíce jmen má {nejvice_jmen} s počtem {max_hvezdicky+1}")

fd.close()
### Konec souboru zaci.py