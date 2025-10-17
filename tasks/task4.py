# tasks/task4.py

def solve():
# Ниже пишите решение задачи
    
    a = int(input())
    b = int(input())
    c = int(input())
    print((a + b > c) and (a + c > b) and (b + c > a))

# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()