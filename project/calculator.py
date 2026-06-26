def main():
    print("简单计算器：加减乘除")
    try:
        a = float(input("请输入第一个数字: "))
        b = float(input("请输入第二个数字: "))
        op = input("请输入运算符 (+ - * /): ").strip()
    except ValueError:
        print("输入格式错误，请输入数字。")
        return

    if op == "+":
        result = a + b
    elif op == "-":
        result = a - b
    elif op == "*":
        result = a * b
    elif op == "/":
        if b == 0:
            print("错误：除数不能为零。")
            return
        result = a / b
    else:
        print("不支持的运算符，请输入 +、-、* 或 /。")
        return

    print(f"结果：{result}")

if __name__ == "__main__":
    main()
