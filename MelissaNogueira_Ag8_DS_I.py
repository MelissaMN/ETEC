## Pesquisa de Satisfação

print("Bem-vindo(a) a nossa pesquisa de satisfação! \nSua opinião é muito importante para nós!")
print("Por favor, responda as seguintes perguntas:")

##Variáveis
excelente = 0
bom = 0
ruim = 0    
Participante = []

for i in range(0, 9):

    print(f"\nParticipante {i+1}:")

    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    
    print("Qual sua opinião sobre o atendimento prestado?")
    print("Digite: \n1 - EXCELENTE \n2 - BOM \n3 - RUIM")

    nota = int(input("Digite sua opção: "))

    while nota != 1 and nota != 2 and nota != 3:
        print("Opção inválida. Por favor, digite 1, 2 ou 3.")
        nota = int(input("Digite sua opção: "))
    
    if nota == 1:
        excelente += 1
    elif nota == 2:
        bom += 1
    elif nota == 3:
        ruim += 1
        
    Participante.append({"nome": nome, "idade": idade, "nota": nota})

## Resultado final
print("\nResultado da pesquisa: ")
print(f"Quantidade de notas na categoria EXCELENTE: {excelente}")
print(f"Quantidade de notas na categoria BOM: {bom}")
print(f"Quantidade de notas na categoria RUIM: {ruim}")
