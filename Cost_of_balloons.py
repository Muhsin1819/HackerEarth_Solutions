def min_price(i, sum_arr):
    price_green, price_purple = map(int, input().split())
    num_participants = int(input())
    big_sum = 0
    sum1 = 0
    sum2 = 0
    for j in range(num_participants):
        f, s = map(int, input().split())
        sum1 += f
        sum2 += s
    if(i % 2 == 0):
        big_sum = (price_green * sum1) + (price_purple * sum2)
    else:
        big_sum = (price_purple * sum1) + (price_green * sum2)
    sum_arr.append(big_sum)


case = int(input())
sum_arr = list()
for i in range(case):
    min_price(i, sum_arr)

for ele in sum_arr:
    print(f"{ele}")
