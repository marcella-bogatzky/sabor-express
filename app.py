import os #Esse comando serve para importar uma biblioteca pré-existente em python

def exibir_nome_do_programa():
    print('''
    ╭━━━╮╱╱╭╮╱╱╱╱╱╱╱╭━━━╮
    ┃╭━╮┃╱╱┃┃╱╱╱╱╱╱╱┃╭━━╯
    ┃╰━━┳━━┫╰━┳━━┳━╮┃╰━━┳╮╭┳━━┳━┳━━┳━━┳━━╮
    ╰━━╮┃╭╮┃╭╮┃╭╮┃╭╯┃╭━━┻╋╋┫╭╮┃╭┫┃━┫━━┫━━┫
    ┃╰━╯┃╭╮┃╰╯┃╰╯┃┃╱┃╰━━┳╋╋┫╰╯┃┃┃┃━╋━━┣━━┃
    ╰━━━┻╯╰┻━━┻━━┻╯╱╰━━━┻╯╰┫╭━┻╯╰━━┻━━┻━━╯
    ╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃┃
    ╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰╯
          ''') #Print é código correspondente ao console.log do JS, serve para exibir informação. É possível pular a linha usando aspas triplas (''') e colocando a quebra a de linha
    #Essa letra estilizada foi pega no site: https://fsymbols.com/pt/letras/

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair \n') #\n também serve para pular linha. 

def escolher_opcao():
    opcao_escolhida = int(input('Escolha uma opção: ')) #Com input a gente quer trazer uma informação do usuário. "opcao_escolhida" é uma variável. O int serve para transformar a resposta em um núemero inteiro
    print('Você escolheu a opção', opcao_escolhida) #A virgula concatena a string com a variável. Outra forma de fazer isso é: print(f'Você escolheu a opção {opcao_escolhida}')

    if opcao_escolhida == 1:
        print('Cadastrar restaurante')
    elif opcao_escolhida == 2:
        print('Listar restaurantes')
    elif opcao_escolhida == 3:
        print('Ativar restaurante')
    else:
        finalizar_app()

    # Uma alternativa ao "int" é simplesmente colocar os valores entre as aspas '', por exemplo if opcao_escolhida == '1'
    # Outra alternativa é o uso do "match", que deixaria a construção desta forma:
    # opcao_escolhida = int(input('Escolha uma opção: '))
    # match opcao_escolhida:
    #     case 1:
    #         print('Adicionar restaurante')
    #     case 2:
    #         print('Listar restaurantes')
    #     case 3:
    #         print('Ativar restaurante')
    #     case 4:
    #         print('Finalizar app')
    #     case _:  # O "_" representa qualquer outro valor diferente dos demais listados
    #         print('Opção inválida!')




def finalizar_app(): #def é o comando que abre uma função (função é um bloco de códigos que realiza uma ação)
    os.system('cls') #Comando para limpar o terminal
    print('Finalizando o app')
 
def main():
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__': #Esse formato é uma convenção do python para declarar uma página como principal do programa
    main ()

# Convenções Python
# snake_case para variáveis, funções e métodos;
# PascalCase para classes;
# SCREAMING_SNAKE_CASE para constantes