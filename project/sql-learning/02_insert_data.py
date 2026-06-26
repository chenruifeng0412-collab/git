import sqlite3

import os   

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, '..', 'fragrance.db')

print(DB_PATH)

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# 多条数据（注意：F001 如果已存在会被忽略，不会报错）
perfumes = [
    ('F001', '玫瑰精油', '花香', 50),
    ('F002', '檀香提取物', '木质', 30),
    ('F003', '柠檬香精', '果香', 80),
    ('F004', '薰衣草精油', '花香', 45),
]

# INSERT OR IGNORE：存在则跳过，不存在则插入
cursor.executemany('''
    INSERT OR IGNORE INTO perfumes (id, name, flavor, stock)
    VALUES (?, ?, ?, ?)
''', perfumes)

print("\n---请输入新香精---")
new_id = input(f"请输入编号：").strip()
new_name = input("请输入名称：").strip()
new_flavor=input("香型：").strip()
new_stock = int(input("请输入库存：").strip())


cursor.execute('''
    INSERT OR IGNORE INTO perfumes(id,name,flavor,stock)
    VALUES(?,?,?,?)
''',(new_id,new_name,new_flavor,new_stock))

conn.commit()
print(f"插入完成，本次影响 {cursor.rowcount} 条记录")
conn.close()



