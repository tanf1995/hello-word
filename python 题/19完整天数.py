date = input('输入时间，格式为1990.10.10\n>>')

year, month, day = list(map(int, date.split('.')))

if month < 8:
    if month//2 == month/2:
        full_day = ((month-1) // 2) * 61 + 31 + day

    else:
        full_day = ((month-1) // 2) * 61 + day

else:
    if month // 2 == month / 2:
        full_day = 4*31 + 3*30 + ((month-8)//2 * 61) + day

    else:
        full_day = 4*31 + 3*30 + ((month-8)//2 * 61) + 31 + day

if month > 2:
    full_day -=2

    if year%400 != 0:
        if year%4 == 0 and year%100 != 0:
            full_day += 1

print(full_day)
