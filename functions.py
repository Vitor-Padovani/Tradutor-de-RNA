import sqlite3

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
