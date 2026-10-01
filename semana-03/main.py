import funções
from time import sleep

lista_solicitacoes = funções.carregar_dados()

while True:
    funções.exibir_menu()
    opcao = funções.escolher_opcao_menu()

    if opcao == "1":
        funções.cadastrar_solicitacao(lista_solicitacoes)
    if opcao == "2":
            funções.listar_solicitacao(lista_solicitacoes)
    if opcao == "3":
        funções.consultar_solicitacao(lista_solicitacoes)
    if opcao == "4":
        funções.mostrar_estatistica(lista_solicitacoes)
    if opcao == "5":
        print('\nEncerrando o sistema... Até logo.')
        sleep(1)
        break
