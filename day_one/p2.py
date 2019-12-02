import math

total=0

with open('data.1') as file:
    filelines= file.readlines()
    print(filelines)
    for i in filelines:
        iszero=False
        f=int(i)
        while iszero == False:
            new_f = (math.floor(f/3)-2)
            f=new_f
            if f <= 0:
                iszero=True
                break
            total = total + f
            

print(total)