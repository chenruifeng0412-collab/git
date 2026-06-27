import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, '..', 'fragrance.db')

conn=sqlite3.connect(DB_PATH)
cursor=conn.cursor()

new_id=input("请输入编号: ").strip()
print("---修改前---")
cursor.execute("SELECT id,name,stock FROM perfumes WHERE id=?",(new_id,))
row=cursor.fetchone()
print(f"编号： {row[0]},名称：{row[1]},库存：{row[2]}")

new_stock=int(input("请输入新库存：").strip())
cursor.execute('''
    UPDATE perfumes
    SET stock=?
    WHERE id=?
''',(new_stock,new_id))

conn.commit()

print('\n---修改后---')
cursor.execute("SELECT id,name,stock FROM perfumes WHERE id=?",(new_id,))
row=cursor.fetchone()
print(f"编号： {row[0]},名称：{row[1]},库存：{row[2]}")

conn.close()