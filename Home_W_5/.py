
                                                           #Задание первое
num_zeroes = 0
for i in range(int(input())):
    if int(input()) == 0:
        num_zeroes += 1
print(num_zeroes)

                                                            #Задание второе

x = int(input())
count = 0
for i in range(1, x+1):
    if x % i == 0:
        count += 1

print(count)