#1013
A, B, C = input().split()

A = int(A)
B = int(B)
C = int(C)

# compara qual o maior entre A ou B
maiorAB = (A + B + abs (A - B)) / 2

# comparando o resultado do maior entre A ou B com o C
maiorABC = (maiorAB + C + abs (maiorAB - C)) / 2

# print ABC por ser a comparação final entre os três valores
print(int(maiorABC), 'eh o maior')