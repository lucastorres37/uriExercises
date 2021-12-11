prod1 = input() # 12 1 5.30
prod2 = input() # 16 2 5.10

id1, qt1, valor1 = prod1.split()
id1 = int(id1)
qt1 = int(qt1)
valor1 = float(valor1)

id2, qt2, valor2 = prod2.split()
id2 = int(id2)
qt2 = int (qt2)
valor2 = float(valor2)

totalCompra = (qt1 * valor1) + (qt2 * valor2)

print('VALOR A PAGAR: R$' + '%.2f' % totalCompra)