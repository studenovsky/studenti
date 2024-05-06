zaci = {}
pocty_krestni = {}
fd = open("zaci.txt", "r")

# čtení jednoho řádku ze souboru
for line in fd:
    jmeno_list = line.strip().split()
    prijmeni = jmeno_list.pop(-1)
    zaci[prijmeni]= "*".join(jmeno_list)

# výpis záznamů s oddělovačem * a -
for prijmeni in zaci.keys():
    print(f"*{zaci[prijmeni]}*-{prijmeni}-")

# výpis počtu žáků se stejným křestním jménem
    if zaci[prijmeni] in pocty_krestni:
        pocty_krestni[zaci[prijmeni]] += 1
    else:
        pocty_krestni[zaci[prijmeni]] = 1
print(pocty_krestni)
fd.close()