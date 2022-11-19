import sqlite3
import csv


def name_key(dct):
    return dct['name']


def damage_key(dct):
    return dct['damage']


filename = input()
value = int(input())
pirates = []

con = sqlite3.connect(filename)
con.row_factory = sqlite3.Row
cur = con.cursor()

wounded = [dict(i) for i in cur.execute(f"""SELECT * FROM Wounded""").fetchall()]
for i in wounded:
    nid = dict(cur.execute(f"""SELECT * FROM Robbers WHERE id={i['name_id']}""").fetchone())
    name, age = nid['name'], nid['age']
    iid = dict(cur.execute(f"""SELECT * FROM Injuries WHERE id={i['injury_id']}""").fetchone())
    injury, los = iid['title'], iid['level_of_severity']
    pirates.append({'name': name, 'age': age, 'injury': injury, 'severity': i['severity'],
                    'damage': int(i['severity']) * int(i['amount_of_damage']) * int(los)})

con.commit()
con.close()
pirates.sort(key=name_key)
pirates.sort(key=damage_key, reverse=True)
pirates = pirates[:value]
with open('bypass.csv', 'w', newline='') as csvfile:
    fieldnames = ["name", "age", "injury", "severity", "damage"]
    writer = csv.DictWriter(csvfile, fieldnames)
    for pirate in pirates:
        writer.writerow(pirate)
