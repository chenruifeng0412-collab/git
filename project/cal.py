import json

FILENAME="fragrance.json"

class InventorySteam:
  def __init__(self):
     self.products=[]

  def load_data():
    """从JSON文件读取数据，文件不存在则返回空列表"""
    try:
        with open(FILENAME,'r',encoding='utf-8')as f:
            return json.load(f)
    except FileNotFoundError:
        return[]

  def save_data(data):
    """将数据保存到JSON文件"""      
    with open(FILENAME,'w',encoding='utf-8')as f:
      json.dump(data,f,ensure_ascii=False,indent=2)

  def add_product(self):
     """添加产品"""
     pid=input("请输入编号: ").strip()
     name = input("请输入名称：").strip()
     stock = int(input("请输入库存：").strip())

     product={"id":pid,"name":name,"stock":stock}

     self.products.append(product)

     print("添加成功")

  def show_product(self):
     """展示全部产品"""
     if not self.products:
         print("暂无产品")
     else:
        for p in self.products:
           print(p["id"],["name"],["stock"])

  def search_products(self):
     """查询个别产品"""
     pid=input("请输入编号: ")

     for p in self.products:
        if p["id"]==pid:
           print(p["id"],["name"],["stock"])
           return

        else:
           print("产品不存在")

  def update_product(self):
     pid=input("请输入编号： ").strip()
     for p in self.products:
        if p["id"]==pid:
           print("当前库存：",p["stock"])

           new_stock=int(input("新库存： "))
           p["stock"]=new_stock

           print("修改成功")
           return
        print("产品不存在")
    
  def delete_product(self):
     """删除产品"""
     pid=input("请输入要删除的编号: ").strip()
     for p in self.products:
        if p["id"]==pid:
           self.products.remove(p)

           print("删除成功")
           return
        print("产品不存在")
         
  def search_Mstock(self):
     """查询库存最多的产品"""
     if not self.products:
        print("数据库中不存在已录入产品")
        return
     max_product=self.products[0]
     for p in self.products:
        if p["stock"]>max_product["stock"]:
           max_product=p
      
     print(f"编号:{max_product['id']}|名称：{max_product['name']}|库存：{max_product['stock']}")
      

  def search_Lstock(self):
    """查询库存低于50的产品"""
    found=False
    for p in self.products:
       if p["stock"]<50:
          if not found:
             print("---库存预警[少于50]---")
             found=True
          print(f"编号:{p['id']}|名称:{p['name']}|库存:{p['stock']}")

       if not found:
         print("没有符合条件的产品")

  def count_product(self):
    """查询产品总数"""
    total=len(self.products)
    print(f"产品总数:{total}")

  def count_stock(self):
    """查询总库存"""
    total=0
    for p in self.products:
       total+=p['stock']
    print(f"总库存：{total}")

def menu(self):
     while True:
          print("\n===== 香精样品管理系统 =====")
          print("1. 新增产品")
          print("2. 查询产品")
          print("3. 修改库存")
          print("4. 删除产品")
          print("5. 显示全部产品")
          print("6. 查询库存低于50的产品")
          print("7. 查询产品总数")
          print("8. 查询总库存")
          print("9. 退出")
          
          choice=input("请选择操作：").strip()
          
          if choice=='1':
           self.add_product()

          elif choice=='2':
            self.search_product()

          elif choice=='3':
            self.update_stock()

          elif choice=='4':
           self.delete_product()
            
          elif choice=='5':
           self.show_product()
          
          elif choice=='6':
           self.search_Lstock()
        
          elif choice=='7':
            self.count_product()
            
          elif choice=='8':
            self.count_stock()

          elif choice=='9':
            break
          else:
            print("无效选择")

if __name__ == "__main__":
    manager=InventorySteam()
    manager.menu()
