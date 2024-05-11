import os #Esse comando serve para importar uma biblioteca pré-existente em python

restaurantes = ['Restaurante Italiano do Gepreto', 'FoodTruck do Oberyn']

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

def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)
    print()

def voltar_ao_menu_principal():
    input('\n Digite uma tecla para voltar ao menu principal')
    main()

def opcao_invalida():
    print('Opção inválida! \n')
    voltar_ao_menu_principal()

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    restaurantes.append(nome_do_restaurante) #Append coloca itens em uma lista. Corresponde ao "push" do JS
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Listando restaurantes')
    for restaurante in restaurantes: #"Para cada" restaurante "na lista" restaurantes
        print(f'.{restaurante}')
    voltar_ao_menu_principal()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: ')) #Com input a gente quer trazer uma informação do usuário. "opcao_escolhida" é uma variável. O int serve para transformar a resposta em um núemero inteiro
        print('Você escolheu a opção', opcao_escolhida) #A virgula concatena a string com a variável. Outra forma de fazer isso é: print(f'Você escolheu a opção {opcao_escolhida}')

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            print('Ativar restaurante')
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except: opcao_invalida() #O "Try" no início com o "Except" ao fim serve para que o sistema TENTE entregar o resultado, mas caso não consiga, devolva a mensagem da exceçao

def finalizar_app(): #def é o comando que abre uma função (função é um bloco de códigos que realiza uma ação)
    exibir_subtitulo('Finalizando o app')
 
def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__': #Esse formato é uma convenção do python para declarar uma página como principal do programa
    main ()

# Convenções Python
# snake_case para variáveis, funções e métodos;
# PascalCase para classes;
# SCREAMING_SNAKE_CASE para constantes