def IsEven(num):
    numb = int(str(num), 2)
    if numb // 2 == 0:  return "Четное"
    else: return "Нечетное"

if __name__ == "__main__":
    while True:
        s = input("Введите число в двоичной сс(или q для выхода): ").strip()
        if s.lower() in ('q', 'quit', 'выход'):
            break
        try:
            print(f"Число {IsEven(s)}")
        except ValueError:
            print("Ошибка: строка должна содержать только 0 и 1")
        
