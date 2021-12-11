name = str(input())
salary = float(input())
monthSales = float(input())

TOTAL = salary + (monthSales*15/100)

print('TOTAL = R$', '%.2f' % TOTAL)