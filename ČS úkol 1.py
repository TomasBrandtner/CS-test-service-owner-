# Načtení obsahu jednotlivých souborů
with open('1.txt', 'r') as soubor1:
    obsah1 = soubor1.read()

with open('2.txt', 'r') as soubor2:
    obsah2 = soubor2.read()

with open('3.txt', 'r') as soubor3:
    obsah3 = soubor3.read()

# Seřazení obsahu souborů podle počtu řádků
seřazený_obsah = [obsah1, obsah3, obsah2]

# Vytvoření výsledného souboru
with open('merged_files.txt', 'w') as spojený_soubor:
    for i, obsah in enumerate(seřazený_obsah, start=1):
        řádky = obsah.count("\n") + 1
        spojený_soubor.write(f'{i}.txt\n{řádky}\n')
        spojený_soubor.write(obsah)
        spojený_soubor.write('\n\n')