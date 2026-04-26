
from datetime import datetime

# Print de boas-vindas
print("Olá professor! Digite o nome e nota dos seus alunos para calcular a média.")
Aluno = []

def calcular_media(nota, nota_1):
    return (nota + nota_1) / 2

# Média dos alunos
while True:
        nome = input("Nome (ou digite ENTER para finalizar): ")
 
        if nome == "":
            break
        
        nota = float(input("Nota Português: "))
        nota_1 = float(input("Nota Matemática: "))

        media = calcular_media(nota, nota_1)
        
        Aluno.append({"nome": nome, "média": media})

# Exibir a média dos alunos

print("\nMédia dos alunos:")
for aluno in Aluno:
    print(f"{aluno['nome']}: {aluno['média']:.2f}")


# Relatório da turma 

print("\nRelatório da turma:")
for aluno in Aluno:
    if aluno['média'] >= 7:
        print(f"{aluno['nome']} - Aprovado")
    elif aluno['média'] >= 5:
        print(f"{aluno['nome']} - Recuperação")
    else:
        print(f"{aluno['nome']} - Reprovado")

# Finalização do programa
print("\nO relatório foi gerado com sucesso! Excelente trabalho, professor!")

# Pega a data e hora atual
agora = datetime.now()

# Exibe no formato padrão
print('Relatório gerado em:', agora)

