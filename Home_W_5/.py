
                                                           #Задание первое
n = int(input("Введите количество чисел "))

a = 0

for i in range(1, n+1):

 s = int(input("введите целое число "))

 if s == 0:

  a+=1

print(a)

                                                            #Задание второе

x = int(input())
count = 0
for i in range(1, x+1):
    if x % i == 0:
        count += 1

print(count)

                                                          # Задание третье
print("Введите целое число А: ")

a=int(input())

print("Введите число B: ")

b = int(input())

for i in range(a, b + 1):

 if i % 2 == 0:

  print(i, end=' ')                                                    