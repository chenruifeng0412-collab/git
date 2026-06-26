import sqlite3

import os
import sqlite3

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, '..', 'fragrance.db')

print(DB_PATH)

conn = sqlite3.connect(DB_PATH)
cursor=conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS perfumes(
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    flavor TEXT,
    stock INTEGER
)
''')    

cursor.execute("""
SELECT name
FROM sqlite_master
WHERE type='table'
""")

print(cursor.fetchall())
conn.commit()
print("表创建成功")
conn.close()
