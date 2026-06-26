import json

FILENAME="fragrance.json"

def load_data():
    try:
        with open(FILENAME,'r',encoding='utf-8')as f:
            return json.load(f)
    except FileNotFoundError:
        return{}

def save_data(data):
        with open(FILENAME,'w',encoding='utf-8')as f:
            json.dump(data,f,ensure_ascii=False,indent=2)

def add_product():
     pid=input("请输入编号: ").strip()

     name = input("请输入名称：").strip()
     stock = int(input("请输入库存：").strip())

     cursor.execute('''
     INSERT OR IGNORE perfumes
     VALUE(?,?,?)
     ''',(pid,name,stock))

     conn.commit()
     print("添加成功")


def search_product():
     pid=input("请输入要查询的编号：").strip()

     cursor.execute('SELECT id,name,stock FROM perfumes WHERE id=?',(pid,))
     row=cursor.fetchone()

     if not row:
         print("暂无产品")
     else:
         print(f"{row[0]}|{row[1]}|库存：{row[2]}")

def update_stock():
     pid=input("请输入编号： ").strip()
     cursor.execute('SELECT stock FROM perfumes WHERE id=?',(pid,))
     row=cursor.fetchone()

     print(f"{row[2]}")

     new_stock=int(input("输入库存： ").strip())
     cursor.execute('''
        UPDATE FROM perfumes 
        SET stock=?          
        WHERE id=?''',
        (new_stock,pid,))
     cursor.execute("SELECT stock FROM perfumes WHERE id=?", (pid,))
     row=cursor.fetchone()
     conn.commit()
     print(f"新库存：{row[2]}")
    
def delete_product():
     pid=input("请输入要删除的编号: ").strip()
     
     cursor.execute('SELECT id,name,stock FROM perfumes WHERE id=?',(pid,))
     row=cursor.fetchone()
     if row is None:
        print("编号不存在")
     else:
         print("---将要删除的数据---")
         print(f"{row[0]}|{row[1]}|库存: {row[2]}")
         cursor.execute('''
            DELETE FROM perfumes
            WHERE id=?
            ''',(pid,))
         conn.commit()
         

def search_Mstock():
      cursor.execute('SELECT * FROM perfumes ORDER BY stock DESC LIMIT 1')
      row=cursor.fetchone()
      if row is None:
        print("库存中不存在已录入产品")
      else:
        print(f"编号：{row[0]}|名称：{row[1]}|库存：{row[2]}")

def search_Lstock():
    cursor.execute('SELECT * FROM perfumes WHERE stock < 50')
    rows=cursor.fetchall()

    if rows is None:
     print("没有符合条件的产品")
    else:
        print("---库存预警（少于50）---")
        for row in rows:
            print(f"编号：{row[0]}|名称：{row[1]}|库存：{row[2]}")

def count_product():
    cursor.execute('SELECT COUNT(*)FROM perfumes')
    rows=cursor.fetchone()
    total_product=rows[0] if rows[0] else 0
    print(f"产品总数：{total_product}")

def count_stock():
    cursor.execute('SELECT SUM(stock) FROM perfumes')
    rows=cursor.fetchall()
    total_stock=rows[0] if rows[0] else 0
    print(f"总库存：{total_stock}")

def main():
     while True:
          print("\n===== 香精样品管理系统 =====")
          print("1. 新增产品")
          print("2. 查询产品")
          print("3. 修改库存")
          print("4. 删除产品")
          print("5. 查询库存最高的产品")
          print("6. 查询库存低于50的产品")
          print("7. 查询产品总数")
          print("8. 查询总库存")
          print("9. 退出")
          
          choice=input("请选择操作：").strip()
          
          if choice=='1':
           add_product()

          elif choice=='2':
            search_product()

          elif choice=='3':
            update_stock()

          elif choice=='4':
           delete_product()
            
          elif choice=='5':
           search_Mstock()
          
          elif choice=='6':
           search_Lstock()
        
          elif choice=='7':
            count_product()
            
          elif choice=='8':
            count_stock()

          elif choice=='9':
            break
          else:
            print("无效选择")

if __name__ == "__main__":
    main()


