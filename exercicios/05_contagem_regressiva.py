# duas funções com o mesmo propósito usando estruturas de repetição diferentes while e for
def contagem_regressiva(n):
    while n >= 0:
        print(n)
        n -= 1

print(contagem_regressiva(5))

print('---')

def contagem_regressiva2(n):
    for i in range(n, -1, -1): # para cada i no range que começa em n, vai até antes de -1 (0), andando de -1 em -1
        print(i)

print(contagem_regressiva2(10))