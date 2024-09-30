#temos um menu principal: 
# 1 Criar uma nova lista de compras
# 2 Carregar uma lista existente
# 3 Sair

#temos um menu de compras:
# 1 Adicionar item
# 2 Remover item
# 3 Visualizar lista
# 4 Salvar e sair
# 5 Sair sem salvar
# Escolha uma opção
# Digite o nome do item:
# Digite a quantidade:
# Digite o nome do arquivo para salvar:
# Opção inválida

import json
import time
import os



def adicionar_item(compras,item,quantidade):
    compras[item]=quantidade

def remover_item(compras,item):
    if item in compras:
        del compras[item]


def visualisar_compras(compras):
    for item,quantidade in compras.items():
        print(f"{item}: {quantidade}")
    print()
    print('Pressione enter para continuar')
    input()


def salvar_compras(compras,nome_arquivo):
    with open(nome_arquivo,'w') as arquivo:
        json.dump(compras,arquivo)

def carregar_compras(nome_arquivo):
    with open(nome_arquivo,'r') as arquivo:
        return json.load(arquivo)

def gerenciar_compras(compras,nome_arquivo=None):
    #Se o usuário está criando uma nova lista de compras, nome_arquivo será None, porque a função não recebeu um arquivo associado.
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("1 Adicionar item")
        print("2 Remover item")
        print('3 Visualizar lista')
        print('4 Salvar e sair')
        print('5 Sair sem salvar')
        escolha=input('Escolha uma opção: ')

        if escolha=='1':
            item=input('Digite o nome do item: ')
            quantidade = int(input('Digite a quantidade: '))
            adicionar_item(compras,item,quantidade)
        elif escolha=='2':
            item=input('Digite o nome do item: ')
            remover_item(compras,item)
        elif escolha=='3':
            visualisar_compras(compras)
        elif escolha=='4':
            if nome_arquivo is None:
                nome_arquivo=input('Digite o nome do arquivo para salvar: ')
            if not nome_arquivo.endswith('.json'):
                nome_arquivo+='.json'  
            salvar_compras(compras,nome_arquivo)
            break
        elif escolha=='5':
            break
        else:
            print('Opção inválida')
            time.sleep(1)

def main():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print('1 Criar uma nova lista de compras')
        print('2 Carregar uma lista existente')
        print('3 Sair')
        escolha=input('Escolha uma opção: ')
        if escolha=='1':
            compras={}
            gerenciar_compras(compras)
        elif escolha=='2':
            print('Listas disponíveis:')
            arquivos=[]  # Lista para armazenar os arquivos JSON
            todos_arquivos = os.listdir() # Obtemos a lista de arquivos e diretórios no diretório atual
            for arquivo in todos_arquivos:
                if arquivo.endswith('.json'):
                    arquivos.append(arquivo)
            if not arquivos: # Se a lista de arquivos JSON estiver vazia
                print('Nenhuma lista encontrada')
                time.sleep(2)
                continue
            for i,arquivo in enumerate(arquivos,1):
                print(f'{i} {arquivo}')
            escolha = int(input('Escolha uma lista para carregar (0 se nenhuma): '))
            if escolha == 0:
                continue
            if escolha<0 or escolha>len(arquivos):
                print('Opção inválida')
                time.sleep(1)
                continue
            nome_arquivo = arquivos[escolha - 1]
            compras = carregar_compras(nome_arquivo)
            gerenciar_compras(compras,nome_arquivo)
        elif escolha=='3':
            break
        else:
            print('Opção inválida')
            time.sleep(1)


main()



#arquivos = [arquivo for arquivo in os.listdir() if arquivo.endswith(".json")]






