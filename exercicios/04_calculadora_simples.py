# esse vai ser por if else básico, retirando a tipagem dos dados 
def calculadora(n1, n2, op):
    if op == "+":
        return n1 + n2
    elif op == "-":
        return n1 - n2
    elif op == "*":
        return n1 * n2
    elif op == "/":
        if n2 == 0:
            return "Erro: divisão por zero"
        return n1 / n2
    else:
        return "Erro: operação inválida"

print(calculadora(10, 5, "+"))
print(calculadora(10, 5, "-"))
print(calculadora(10, 5, "*"))
print(calculadora(10, 5, "/"))
print(calculadora(10, 0, "/"))
print(calculadora(10, 5, "%"))