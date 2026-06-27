import sqlite3
import os

BASE_DIR=os.path.dirname(os.path.abspath(__file__))
DB_PATH=os.path.join(BASE_DIR,'..','fragrance.db')

conn=sqlite3.connect(DB_PATH)
cursor=conn.cursor()

target_id=input("请输入删除编号： ").strip()

print("---修改前---")
cursor.execute("SELECT id,name,stock FROM perfumes ")
for row in cursor.fetchall():
    print(f"{row[0]}|{row[1]}|库存：{row[2]}")

cursor.execute("DELETE FROM perfumes WHERE id=?",(target_id,))

conn.commit()

print(f"\n已删除编号:{target_id}")

print("\n---删除后---")
cursor.execute("SELECT id,name,stock FROM perfumes")
for row in cursor.fetchall():
    print(f"{row[0]}|{row[1]}|库存：{row[2]}")

conn.close()