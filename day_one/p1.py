import math

total=0

with open('data.1') as file:
    filelines= file.readlines()
    print(filelines)
    for i in filelines:
        total = total + (math.floor(int(i)/3)-2)

print(total)