import sqlite3

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, '..', 'fragrance.db')

print(DB_PATH)

conn = sqlite3.connect(DB_PATH)
cursor=conn.cursor()

cursor.execute('SELECT * FROM perfumes')
rows=cursor.fetchall()

print("编号 | 名称 | 香型 | 库存 |")
print(" - "*30)
for row in rows:
    print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]}")

conn.close()
