def maior_de_dois(n : float, n2 : float) -> float:
    if n > n2:
        return n
    else:
        return n2

# ou de forma mais fácil max(n, n2)

print(maior_de_dois(1, 2))
print(maior_de_dois(4, 3))
print(maior_de_dois(5, 5))