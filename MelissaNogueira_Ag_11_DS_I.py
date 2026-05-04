
# Bibliotecas

import colorama 
from colorama import Fore, Style

# Lista e variáveis

reservatório = [('Níveis do Reservatório de Água'),
    (1, 'Muito Baixo'),
    (2, 'Baixo'),
    (3, 'Médio'),
    (4, 'Alto'),
    (5, 'Muito Alto')
]

# Função para definir a cor

def definir_cor(nivel):
    if nivel == 1:
        return Fore.RED
    elif nivel == 2:
        return Fore.YELLOW
    elif nivel == 3:
        return Fore.GREEN
    elif nivel == 4:
        return Fore.CYAN
    elif nivel == 5:
        return Fore.BLUE
    else:
        return Fore.WHITE

# Mensagens de alerta
print("RESERVATÓRIO DE ÁGUA")

nível_atual = int(input("Digite o nível atual do reservatório (1-5): "))
cor_atual = definir_cor(nível_atual)
if nível_atual == 1:
    print(f"{cor_atual}ALERTA: O reservatório está com o nível de água muito baixo!")
elif nível_atual == 2:
    print(f"{cor_atual}ALERTA: O reservatório está com o nível de água baixo!")
elif nível_atual == 3:
    print(f"{cor_atual}O reservatório está estável.")
elif nível_atual == 4:
    print(f"{cor_atual}O reservatório está cheio.")
elif nível_atual == 5:
    print(f"{cor_atual}O reservatório está muito cheio! Pode acabar transbordando!")
else:
    print(f"{cor_atual}Nível inválido. Por favor, digite um número entre 1 e 5.")


