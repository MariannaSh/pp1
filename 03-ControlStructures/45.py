# a=[]
# n=int(input('Dowolna liczba:'))
# for i in range(2,n+1):
#     k=0 # Инициализируем переменную k, которая будет считать количество делителей числа i.
#     for j in range(1,i+1):
#         if i%j == 0: #проверяем каждое число до определнного числа все делители
#          k+=1
#     if k==2: #если равняется 2 , то число простое
#         a.append(i)
# print(a)
def f(n):
    new=[]
    for i in range(2,n+1):
        k=0
        for j in range(1,i+1):
            if i%j==0:
                k+=1
        if k==2:
            new.append(i)
    return new

print(f(50))
print(f(10))