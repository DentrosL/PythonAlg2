# uma função deve printar na vertical um numero inteiro
# exemplo 3214
# 3
# 2
# 1
# 4

def vert(n):
    if n <= 9:
        print(n)
    else:
        vert(n // 10) # divisão 
        print(n % 10) # isolar o último número

print(3214)