def calcular_nova_media(media_anterior, nota_exame):
    return (media_anterior + nota_exame) / 2

# Abre o arquivo "exame.txt" para leitura
with open("exame.txt", "r") as arquivo:

    for linha in arquivo:

        dados_aluno = linha.split("Média anterior: ")
        nome = dados_aluno[0].replace("Nome: ", "")
        media_anterior = float(dados_aluno[1])


        nota_exame = float(input(f"Informe a nota do exame de {nome}: "))


        nova_media = calcular_nova_media(media_anterior, nota_exame)
        if nova_media >= 5:
            situacao = "Aprovado após exame"
            arquivo_saida = "aprovados.txt"
        else:
            situacao = "Reprovado após exame"
            arquivo_saida = "reprovados.txt"

        # Salva as informações do aluno no arquivo correspondente
        with open(arquivo_saida, "a") as arquivo_situacao:
            arquivo_situacao.write(f"Nome: {nome}\n")
            arquivo_situacao.write(f"Média anterior: {media_anterior:.2f}\n")
            arquivo_situacao.write(f"Nota do exame: {nota_exame:.2f}\n")
            arquivo_situacao.write(f"Nova média: {nova_media:.2f}\n")
            arquivo_situacao.write(f"Situação: {situacao}\n")
            arquivo_situacao.write("-" * 30 + "\n")