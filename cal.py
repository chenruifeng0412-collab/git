# def main():
#     print("欢迎使用计算机")
#     try:
#         a=float(input("请输入第一个数字："))
#         b=float(input("请输入第二个数字："))
#         op=input("请输入运算符(+ - * /): ").strip()
#     except ValueError:
#         print("输出无效，请输入一个数字")
#         return

#     if op=="+":
#         result=a+b
#     elif op=="-":
#         result=a-b
#     elif op=="*":
#         result=a*b
#     elif op=="/":
#         if b==0:
#             print("除数不能为零。")
#             return
#         result=a/b
#     else:
#         print("不支持的运算")
#         return

#     print(f"结果:{result}")

# if __name__ == "__main__":
#     main()

# import random

# def main():
#    target=random.randint(1,100)
#    print("欢迎来到猜数字游戏！我选择了一个1到100之间的数字。")

#    while True:
#         gress=input("请猜一个数字（位于1-100之间）：")

#         if gress>target:
#             print("数字大了")
#         elif gress<target:
#             print("数字小了")
#         else:
#             print("答对了")
#         break

# if __name__ == "__main__":
# main()

# def main():
#     scores=[]
#     while True:
#         score=input("请输入学生成绩（q为退出）：")
#         if score=='q':
#             break
#         scores.append(float(score))

#     if len(scores)==0:
#         print("没有输入成绩")
#         return

#     print(f"最高分：max{scores}")
#     print(f"最低分：min{scores}")
#     print(f"平均分:sum(scores/len(scores):.2f)")

# import json

# FILENAME="contacts.json"

# def load_contacts():
#     try:
#         with open("contacts.json","w",encoding='utf-8')as f:
#             return json.load(f)
#     except FileNotFoundError:
#         return()
    
# def save_contacts(contacts):
#     with open(FILENAME,'w',encoding='utf-8')as f:
#         json.dump(contacts,f,ensure_ascii=False,indent=2)

# def add_contacts(contacts):
#     name=input("请输入姓名：").strip()
#     phone=input("请输入电话：").strip()
#     contacts[name]=phone
#     print(f"已添加：{name}-{phone}")

# def delete_contacts(contacts):
#     name=input("请输入你要删除的姓名:").strip()
#     if name in contacts:
#         del contacts[name]
#         print(f"已删除：{name}")
#     else:
#         print(f"未找到:{name}")

# def search_contact(contacts):
#     name=input("请输入要查询的姓名：").strip()
#     if name in contacts:
#         print(f"{name}-{contacts[name]}")

# def main():
#     contacts=load_contacts()
#     while True:
#             print("\n===== 通讯录 =====")
#             print("1. 新增联系人")
#             print("2. 删除联系人")
#             print("3. 查询联系人")
#             print("4. 退出")
#             choice=input("请选择操作：").strip()

#             if choice=='1':
#                 add_contacts(contacts)
#             elif choice=='2':
#                 delete_contacts(contacts)
#             elif choice=='3':
#                 search_contact(contacts)
#             elif choice=='4':
#                 save_contacts(contacts)
#                 print("已保存")
#                 break
#             else:
#                 print("无效选择")

# if __name__ == "__main__":
#     main()

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


