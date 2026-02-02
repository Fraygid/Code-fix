mx = -10**7
s = 0
count_neg = 0
for i in range(10): #
    x = int(input())
    if x < 0:
        s += x #
        if x > mx:
            mx = x
        count_neg += 1
if count_neg == 0:
    print('NO')
else:
    print(s)
    print(mx)
