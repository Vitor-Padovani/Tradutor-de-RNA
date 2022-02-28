import sqlite3
import functions as f

while True:
    f.line(10)
    
    cdn = input('cdn: ').upper()
    acr = input('acr: ').capitalize()
    ptn = input('ptn: ').capitalize()

    if cdn == '' or acr == '' or ptn == '':
        break

    f.add_codon(cdn, acr, ptn)

# f.add_codon('UUU', 'Phe', 'Fenilalamina')
