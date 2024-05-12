import os #Esse comando serve para importar uma biblioteca pré-existente em python

restaurantes = [{'nome':'Massas do Gepreto', 'categoria':'Cantina Italiana', 'ativo':False}, 
                {'nome':'Food Truck do Oberyn','categoria':'Hamburgueria', 'ativo':True},
                {'nome':'Rancho da Matuta', 'categoria':'Comida Caipira', 'ativo':False},
]

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
    print('3. Alternar status de ativação do restaurante')
    print('4. Sair \n') #\n também serve para pular linha. 

def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * (len(texto))  #Coloca um * com base na quantidade de letras do parâmetro
    print(linha)
    print(texto)
    print (linha)
    print()

def voltar_ao_menu_principal():
    input('\n Digite uma tecla para voltar ao menu principal')
    main()

def opcao_invalida():
    print('Opção inválida! \n')
    voltar_ao_menu_principal()

def cadastrar_novo_restaurante():

    #Isso é uma docstring. Serve para explicar o que está sendo feito no código para auxlia outra pessoa que for trabalhar com ele
    ''' 
    Essa função é reponsável por cadastrar um novo restaurante
    
    Inputs:
    - Nome do restaurante
    - Categoria
    
    Outputs:
    - Adiciona um novo restaurante à lista de restaurantes
    '''

    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante) #Append coloca itens em uma lista. Corresponde ao "push" do JS
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Listando restaurantes')

    print(f'{'Nome do Restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status')

    for restaurante in restaurantes: #"Para cada" restaurante "na lista" restaurantes
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}') #"ljust" serve para definir o espaço que a palavra ocupará
    
    voltar_ao_menu_principal()

def alternar_status_ativacao():
    exibir_subtitulo('Alternando o status de ativação do restaurante')
    nome_restaurante = input ('Digite o nome do restaurante que deve ter o status alternado: ')
    restaurante_encontrado = False
    
    for restaurante in restaurantes:
        if nome_restaurante == restaurante ['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante ['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante ['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)

    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')

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
            alternar_status_ativacao()
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