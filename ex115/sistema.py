from ex115.lib.interface import*
from ex115.lib.arquivo import*
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
      resposta = menu(['Ver pessoas cadastradas', 'Cadastrar uma pessoa', 'Sair do sistema'])
      if resposta == 1:
          #Opção de listar o conteúdo do arquivo
          lerArquivo(arq)
      elif resposta == 2:
          #Cadastrar uma nova pessoa
          cabeçalho('NOVO CADASTRO')
          nome = str(input('Nome:'))
          idade = leiaInt('Idade: ')
          cadastrar(arq, nome, idade)
      elif resposta == 3:
          cabeçalho('Saindo do sistema... Até logo!')
          break
      else:
          print('\033[31mERRO! Digite uma opção válida!\033[m')
      sleep(2)

