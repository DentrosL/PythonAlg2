# escopo local
def calcular_desconto(valor, desconto):
    vlr_desconto = valor * desconto / 100
    
    return vlr_desconto

# print(vlr_desconto) <- não retornará, pois é uma variável que "vive" apenas dentro da função... o escopo dela é só a função
print(calcular_desconto(100, 10))

# vlr_desconto = 20
# print(vlr_desconto) <- agora o print retornaria 20 como resultado