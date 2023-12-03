#Tento příklad jsem nedokázal vyřešit jelikož nemám patřičné znalosti a nezbyl mi čas se vše doučit.
#Snažil jsem se však popřemýšlet a vyhledat postup.
#K výsledku bychom dosáhli pomocí Pandas knihovny, která by usnadnila práci s daty.
#Bohužel s ní ještě neumím pracovat, nicméně postup by mohl být následující:
#Načteme původní data ze souboru phonebook_raw.csv do Pandas DataFrame.
#Budeme předpokládat, že soubor obsahuje sloupce LASTNAME, FIRSTNAME, SECONDNAME, ORGANIZATION, POSITION, PHONE a EMAIL.
#Sloučíme duplicitní záznamy se stejným jménem a příjmením do jednoho záznamu.
#Pokud některý záznam nemá uvedené telefonní číslo nebo e-mail, ponecháme ho prázdný.
#Telefonní čísla převedeme poté pomocí řetězcových metod na formát +3 (123)-XXX-XX-XX.
#Uložíme výstup do nového souboru, např. phonebook_clean.csv, do kterého zapíšeme sloupce s upravenými daty.