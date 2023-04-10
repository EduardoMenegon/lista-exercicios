def calcular_media(notas):
    return sum(notas)/len(notas)

def classificar_aluno(media):
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Exame"
    else:
        return "Reprovado"

# Abre o arquivo "notas.txt" para leitura
with open("notas.txt", "r") as arquivo:

    for linha in arquivo:

        dados_aluno = linha.split(":")
        nome = dados_aluno[0]
        notas = [float(nota) for nota in dados_aluno[1].split(",")]


        media = calcular_media(notas)
        situacao = classificar_aluno(media)


        with open(f"{situacao.lower()}.txt", "a") as arquivo_situacao:
            arquivo_situacao.write(f"Nome: {nome}\n")
            arquivo_situacao.write(f"Notas: {notas}\n")
            arquivo_situacao.write(f"Média: {media:.2f}\n")
            arquivo_situacao.write(f"Situação: {situacao}\n")
            arquivo_situacao.write("-" * 30 + "\n")