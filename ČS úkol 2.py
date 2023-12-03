# Import knihovny requests pro stahování dat z webu
import requests
# Import knihovny time pro práci s časem
import time

#  Funkce pro získání seznamu otázek
def seznam_otazek():

    # Netuším jak přidat ale zde bude URL adresa Stack Overflow API


    # Parametry pro dotaz na otázky s tagem "Python"
    parametry = {
        "site": "stackoverflow",  # Specifikace Stack Exchange webu
        "tagged": "python",  # Hledaný tag
        "fromdate": int(time.time()) - 2 * 24 * 60,  # Před dvěma dny
        "sort": "creation",  # Řazení podle data vytvoření
        "order": "desc",  # Sestupně
    }

    # Odeslání dotazu na API, netuším jak udělat

    # Zpracování výsledků
    if "items" in data:
        for i, otazka in enumerate(data["items"], start=1):
            print(f"Otázka číslo {i}: {otazka['creation_date']}")
            print(otazka["tags"])
            print(otazka["title"])
            print(otazka["link"])
            print("\n")
    else:
        print("Nepodařilo se načíst otázky.")

# Spuštění funkce
if __name__ == "__main__":
    seznam_otazek()

# adresa stackoverflow s nejnovějšími otázky s tagem python:
    # https://stackoverflow.com/questions/tagged/python?sort=Newest&edited=true