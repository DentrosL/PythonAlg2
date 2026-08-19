# uma função deve printar na vertical um numero inteiro
# exemplo 3214
# 3
# 2
# 1
# 4

def vert(n):
    if n <= 9: # ou < 10, mesma coisa = caso base
        print(n)
    else:
        vert(n // 10) # ... resolvendo de trás pra frente... 321... 32.. 3... fim
        print(n % 10) # isolar o último número e imprimir

def verti(m):
    if m <= 9: # ou < 10, mesma coisa = caso base
        print(n)
    else:
        print(m % 10) 
        vert(m // 10)

i = int(input('informe um numero'))

vert(i) # normal
verti(i) # invertido