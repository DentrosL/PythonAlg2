# esse vai ser por switch/match
def classifica_idade(i: int) -> str:
    match i:
        case idade if idade <= 12:
            return "crianca"
        case idade if idade <= 17:
            return "adolescente"
        case idade if idade <= 59:
            return "adulto"
        case _:
            return "idoso"

print(classifica_idade(10))
print(classifica_idade(15))
print(classifica_idade(30))
print(classifica_idade(70))