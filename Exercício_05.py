# Tabela de notas - Você foi contratado por uma escola pra fazer o sistema de boletim dos alunos. Como primeiro passo, escreva um programa que produza a seguinte saída

# Lista de alunos e notas
listadealuno = ("Aline", 9),("Mario", 9),("Sergio", 9),("Shirley", 9)

# Imprimir cabeçalho
print ("ALUNO(A)          NOTA")
print("========          ====")

# Imprimir cada aluno e nota
for listadealuno, nota in listadealuno:
    print(f"{listadealuno:<17} {nota}")
