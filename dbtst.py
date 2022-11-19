import sqlite3


def name_key(dct):
    return dct['name']


filename = input()
condition = input()
op = input()
con = sqlite3.connect(filename)
con.row_factory = sqlite3.Row
cur = con.cursor()
lst = cur.execute(f"""SELECT * FROM island_biota WHERE poisonous=1 {op} {condition}""").fetchall()
con.commit()
con.close()
lst.sort(key=name_key, reverse=True)
for i in lst:
    di = dict(i)
    print(di['name'] + " (" + ('plant' if di['animal_plant'] else 'animal') + ')')
