# def countdown(n):
#  print(n)
#  countdown(n-1)

# infinito

def countdown(n):
  if n==1: #caso base
    print(n)
  else:
    print(n)
    countdown(n-1)

# para quando chegar no 1

n = int(input('informe um numero'))
countdown(n)

# 3 leis da recursão
# - deve ter um caso base
# - deve mudar seu estado e se aproximar do seu caso básico
# - deve chamar a si mesma
