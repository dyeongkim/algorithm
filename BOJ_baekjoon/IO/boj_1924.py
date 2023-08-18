# 백준 2739 - 2007년

x, y = map(int, input().split())

day_list = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
day = y

for i in range(x) :
    if i in [1, 3, 5, 7, 8, 10, 12] :
        day += 31
    elif i in [4, 6, 9, 11] :
        day += 30
    else :
        day += 28

print(day_list[day%7])
