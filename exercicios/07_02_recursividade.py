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

print(3214)