import sqlite3

def line(length):
    print('-'*length)

def create_table():
    conn = sqlite3.connect('data/codons.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE codons (
        codon TEXT, 
        acronym TEXT, 
        protein TEXT
    )''')
    conn.commit()
    conn.close()

def add_codon(cdn, acr, ptn):
    conn = sqlite3.connect('data/codons.db')
    c = conn.cursor()
    c.execute('INSERT INTO codons VALUES (?,?,?)', 
    (cdn, acr, ptn))
    conn.commit()
    conn.close()

def del_codon(id):
    conn = sqlite3.connect('data/codons.db')
    c = conn.cursor()
    c.execute('DELETE from codons WHERE rowid = ?', id)
    conn.commit()
    conn.close()

def convert_codons(rna):

    codons = []
    proteins = []

    for i in range(0, len(rna)):
        if i % 3 == 0:
            try:
                codons.append(rna[i] + rna[i+1] + rna[i+2])
            except:
                break

    conn = sqlite3.connect('data/codons.db')
    c = conn.cursor()

    for codon in codons:
        c.execute('SELECT protein FROM codons WHERE codon = ?', [codon]) # brackets for turning variable to tuple
        proteins.append(c.fetchone())

    
    conn.close()
    return codons, proteins

def format_str(str):
    str = str.upper().replace('T', 'U')
    rna = ''

    for char in str.upper():
        if char in ('U', 'C', 'A', 'G'):
            rna += char
    
    return rna
