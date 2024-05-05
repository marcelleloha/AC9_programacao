"""
Autor: Marcelle Lohane Gonçalves Ganimo
Programação Estruturada 
2024.01
beecrowd - AC9

"""
#1028
def mdc(a, b):
    while b != 0:
        a, b = b, a % b
    return a

N = int(input())

for _ in range(N):
    F1, F2 = map(int, input().split())
    max_pilha = mdc(F1, F2)
    print(max_pilha)

#1087
while True:
    X1, Y1, X2, Y2 = map(int, input().split())
    
    if X1 == 0 and Y1 == 0 and X2 == 0 and Y2 == 0:
        break
    
    if X1 == X2 and Y1 == Y2:
        print("0")
    elif X1 == X2 or Y1 == Y2 or abs(X1 - X2) == abs(Y1 - Y2):
        print("1")
    else:
        print("2")

#1161
from math import factorial

while True:
    try:
        M, N = map(int, input().split())

        soma_fatoriais = factorial(M) + factorial(N)

        print(soma_fatoriais)
    except EOFError:
        break

#1170
n = int(input())

for _ in range(n):
    c = float(input())
    dias = 0
    while c > 1:
        c /= 2
        dias += 1
    
    print(f"{dias} dias")

#1171
N = int(input())
contagem = {}

for _ in range(N):
    valor = int(input())
    contagem[valor] = contagem.get(valor, 0) + 1

for numero in sorted(contagem.keys()):
    print(f"{numero} aparece {contagem[numero]} vez(es)")

#1221
from math import sqrt

def primo(num):
    if num <= 1:
        return False
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False 
    return True
    
for _ in range(int(input())):
    x = int(input())
    if primo(x) == True:
        print("Prime")
    else:
        print("Not Prime")

#1329
while True:
    num = int(input())
    if num == 0:
       break 
    resultados = [int(x) for x in input().split()]
    m = 0
    for resultado in resultados:
        if resultado == 0:
            m += 1
    j = num - m
    print("Mary won " + str(m) + " times and John won " + str(j) + " times")

#1555
n = int(input())
for _ in range (n):
    x, y = [int(val) for val in input().split()]
    
    b = 2*(x**2) + (5*y)**2 
    r = (3*x)**2 + y**2
    c = -100*x + y**3
    
    if b > c and b > r: 
        print("Beto ganhou")
    elif c > b and c > r:
        print("Carlos ganhou")
    else:
        print("Rafael ganhou")