# samohlasky.py - program, který spočítá počet samohlásek v textu a vypíše je do slovníku
# Autor: Jaroslav Studenovský <studenovskyj@jirovcovka.net>

# Definování proměnných
vocals = ("a","á","e","ě","é","i","í","o","ó","u","ú","ů","y","ý")
slovnik = {}

# Funkce pro spočítání samohlásek v textu
def num_vocals(text):
    for item in vocals:
        pocet = text.count(item)
        if pocet > 0:
            slovnik[item] = pocet
    print(slovnik)

# Hlavní program
text = input("Zadejte větu: ")
num_vocals(text)
# Konec programu


