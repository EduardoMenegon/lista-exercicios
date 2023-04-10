
nome = input("Insira o nome do aluno: ")
nota1 = float(input("Insira a nota 1 do aluno: "))
nota2 = float(input("Insira a nota 2 do aluno: "))
nota3 = float(input("Insira a nota 3 do aluno: "))

with open('notas.txt', 'a') as arquivo:
    arquivo.write(f"{nome}: {nota1}, {nota2}, {nota3}\n")