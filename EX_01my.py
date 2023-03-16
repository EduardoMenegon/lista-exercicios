# Lista de cálculo de horas por turno e cargo
valor_hora = {"G": {"N": 0.1 * 1320, "M": 0.15 * 1320, "V": 0.15 * 1320},
              "O": {"N": 0.09 * 1320, "M": 0.14 * 1320, "V": 0.14 * 1320}}

# Loop para coletar e armazenar as informações dos funcionários
funcionarios = []
while True:
    nome = input("Digite o nome do funcionario(ou digite 0 para sair):")
    if nome == "0":
        break
    horas_trabalhadas = input("Digite a quantidade de horas trabalhadas no mês: ")
    while not horas_trabalhadas.isdigit():
        horas_trabalhadas = input("Quantidade de horas inválida, informe novamente: ")
    turno = input("Informe o turno de trabalho (M = Matutino, V = Vespertino e N = Noturno): ").upper()
    while turno not in ["M", "V", "N"]:
        turno = input("Turno inválido, informe novamente: ").upper()
    categoria = input("Informe a categoria (G = Gerente e O = Operário): ").upper()
    while categoria not in ["G", "O"]:
        categoria = input("Categoria inválida, informe novamente: ").upper()

    # Cálculo do salário
    salario = float(horas_trabalhadas) * valor_hora[categoria][turno]
    funcionarios.append({"nome": nome, "horas_trabalhadas": horas_trabalhadas, "turno": turno, "categoria": categoria,
                         "salario": salario})
# Impressão
for funcionario in funcionarios:
    print("Funcionário: {funcionario['nome']} - Salário: R$ {funcionario['salario']:.2f}")

    
