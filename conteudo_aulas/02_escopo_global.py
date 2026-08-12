# escopo global
# reconhecida em qualquer parte do programa
# deve ser utilizada com cuidado, pois pode estar sendo utilizada em vários pontos do código
x = 0

def keyPassed():
    global x # para conseguir alterar o valor da variavel de fora, é passado o "global" antes
    x += 1
    return x

print(keyPassed())