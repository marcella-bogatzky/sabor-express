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

print('1. Cadastrar restaurante')
print('2. Listar restaurante')
print('3. Ativar restaurante')
print('4. Sair \n') #\n também serve para pular linha. 

opcao_escolhida = input('Escolha uma opção: ') #Com input a gente quer trazer uma informação do usuário. "opcao_escolhida" é uma variável
print('Você escolheu a opção', opcao_escolhida) #A virgula concatena a string com a variável. Outra forma de fazer isso é: print(f'Você escolheu a opção {opcao_escolhida}')


# Convenções Python
# snake_case para variáveis, funções e métodos;
# PascalCase para classes;
# SCREAMING_SNAKE_CASE para constantes.