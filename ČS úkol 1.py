# Otevření a načtení obsahu jednotlivých souborů
with open('1.txt', 'r') as soubor1:  # Otevření souboru '1.txt' v režimu čtení
    obsah1 = soubor1.read()  # Načtení obsahu souboru '1.txt' a uložení do proměnné 'obsah1'

with open('2.txt', 'r') as soubor2:  # Otevření souboru '2.txt' v režimu čtení
    obsah2 = soubor2.read()  # Načtení obsahu souboru '2.txt' a uložení do proměnné 'obsah2'

with open('3.txt', 'r') as soubor3:  # Otevření souboru '3.txt' v režimu čtení
    obsah3 = soubor3.read()  # Načtení obsahu souboru '3.txt' a uložení do proměnné 'obsah3'

# Vytvoření seznamu obsahů souborů spolu s jejich názvy a počtem řádků
data_souboru = [  # Vytvoření seznamu obsahujícího názvy souborů a jejich obsahy a počty řádků
    ('1.txt', obsah1, obsah1.count('\n') + 1),  # Tuple obsahující název souboru, obsah a počet řádků pro '1.txt'
    ('2.txt', obsah2, obsah2.count('\n') + 1),  # Tuple obsahující název souboru, obsah a počet řádků pro '2.txt'
    ('3.txt', obsah3, obsah3.count('\n') + 1)  # Tuple obsahující název souboru, obsah a počet řádků pro '3.txt'
]

# Seřazení seznamu podle počtu řádků
data_souboru.sort(key=lambda x: x[2])  # Seřazení seznamu podle třetího prvku (počet řádků) v každém tuple

# Zápis do výsledného souboru
with open('merget_files.txt', 'w') as spojený_soubor:  # Otevření souboru 'merget_files.txt' v režimu zápisu
    for název_souboru, obsah, počet_řádků in data_souboru:  # Procházení seznamu souborů podle jejich počtu řádků
        spojený_soubor.write(f"{název_souboru}\n{počet_řádků}\n{obsah}\n\n")  # Zápis názvu souboru, počtu řádků a obsahu souboru do výsledného souboru
