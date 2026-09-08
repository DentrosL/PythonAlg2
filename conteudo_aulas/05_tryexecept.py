# exercicios slides
# 1 - exercício de soma segura
try:
    x = int(input('informe sua idade')) # se for colocado um float vai cair no erro de valor
    y = 2 # se o string for '2' vai cair no erro de tipo
    print(x+y)
except ValueError:
    print('digite apenas números inteiros')
except TypeError:
    print('digite apenas números que podem ser somados')

# 2 - "calculadora" segura, só a divisão
try:
    x = float(input('informe o primeiro número'))
    y = float(input('informe o segundo número'))
    d = x/y
except ZeroDivisionError:
    print('não é possível dividir por zero')
except TypeError:
    print('digite apenas números que podem ser divididos')
except Exception as e:
    print('erro inesperado', e)
else:
    print('divisão realizada com sucesso')
    print(f'o resultado da divisão é: {d}')

# lista de exercicios
# 2. + 3.(exercicio 3 é a ultima parte "Exception as e" do exercicio 2)
lista = [1, 2, 3, 4, 5]
def somar_elemento(lista, i1, i2):
    try:
        return lista[i1] + lista[i2]
    except IndexError:
        print('índice inválido')
    except TypeError:
        print('não é possível somar os elementos informados')
    except Exception as e:
        print('erro inesperado', e)

somar_elemento(lista, 1, 2) # resultado esperado: 5
somar_elemento(lista, 1, 5) # resultado esperado: índice inválido

# 4.
