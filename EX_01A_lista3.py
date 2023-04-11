paises = ["Argentina", "Brasil", "Chile", "Colômbia", "Equador", "Paraguai", "Peru", "Uruguai", "Venezuela"]


def posicao_pais(nome_pais):
    if nome_pais in paises:
        return paises.index(nome_pais)
    else:
        print("O pais não está na lita.")


nome_pais = input("Digite o nome do pais: ")
posicao = posicao_pais(nome_pais)
print("A posição do país", nome_pais, "na lista é:" , posicao +1)
