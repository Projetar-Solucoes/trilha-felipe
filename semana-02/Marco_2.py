from time import sleep
from datetime import date

escolha = 0
numero_solicitacao = 0
numero_alta_urgencia = 0
numero_media_urgencia = 0
numero_baixa_urgencia = 0
numero_protocolo = 0

def testar_vazio(frase):
    name = input(f"{frase}").strip().title()
    while name == "":
        name = input("Campo inválido digite novamente: ").strip().title()
    return name

def setor_vazio(frase):
    print('''
    [1] Financeiro
    [2] Atendimento ao Cliente 
    [3] Suporte Técnico
    [4] Vendas
    [5] Marketing''')
    print('--=--' *20)
    setor_decisao = input(f'{frase}').strip()
    while setor_decisao != '1' and setor_decisao != '2' and setor_decisao != '3' and setor_decisao != '4' and setor_decisao != '5':
        setor_decisao = input('Campo Inválido! Digite novamente: ').strip()
    return setor_decisao

while escolha == 0:
    print('''Seja bem vindo à XXXXXXXXX. Decida entre uma das opções abaixo:
    [1]Cadastrar Solicitação
    [2]Consultar Solicitação
    [3]Estatísticas
    [4]Sair''')
    escolha = str(input('Escolha: '))

    if escolha == "1":
        print('-'*50)
        ano = int(testar_vazio("Digite o ano da Solicitação: "))
        while ano > date.today().year or ano <=0:
            ano = int(testar_vazio("Ano Inválido. Digite o ano da solicitação novamente: "))

        numero_protocolo += 1
        nome = testar_vazio("Digite seu nome: ").strip()
        print('-'*50)
        
        numero_protocolo_str = str(numero_protocolo).zfill(4)
        nomes = nome.upper().split()
        iniciais = ''.join([palavra[0] for palavra in nomes])
        
        protocolo = '-'.join([str(ano), numero_protocolo_str, iniciais])
        print('-'*50)

        setor = setor_vazio('Qual setor você deseja entrar em contato? ').strip()
        
        categoria = input('''
            [1]Alta Urgência
            [2]Média Urgência
            [3]Baixa Urgência
            Digite a categoria: ''').strip()
        while categoria != '1' and categoria != '2' and categoria != '3':
            print('Categoria Inválida. Escolha novamente.')
            categoria = input('''
            [1]Alta Urgência
            [2]Média Urgência
            [3]Baixa Urgência
            Digite a categoria: ''').strip()
        match categoria:
            case '1':
                numero_alta_urgencia += 1
            case '2':
                numero_media_urgencia += 1
            case '3':
                numero_baixa_urgencia += 1
                  
        assunto = testar_vazio('Qual o assunto da sua solicitação? ').strip()
        descricao = testar_vazio('Por favor, descreva sua solicitação detalhadamente: ').strip()
        print('-'*50)
        print(f'Solicitação Cadastrada com Sucesso!')
        print('-'*50)
        escolha = 0
        numero_solicitacao += 1

    elif escolha =="2":
        if numero_solicitacao == 0:
            print('Nenhuma solicitação cadastrada.')
            escolha = 0
        else:
            print('-'*50)
            print(f'Obrigado, {nome}. Sua reclamação foi registrada no \n setor de {setor} \n com a categoria "{categoria}", \n assunto "{assunto}" \n e descrição: "{descricao}". \n O número do seu protocolo é {protocolo}')
            print('-'*50)
            sleep(5)
            escolha = 0

    elif escolha =="3":
        print(f'A quantidade de solicitações registradas é igual a {numero_solicitacao}')
        print(f'''A quantidade de solicitações registradas como:
        [1]Alta Urgência = {numero_alta_urgencia}
        [2]Média Urgência = {numero_media_urgencia}
        [3]Baixa Urgência = {numero_baixa_urgencia}''')
        escolha = 0

    elif escolha =="4":
        print('Muito obrigado por contatar-nos. A XXXXXXXXXXXXX agradece! Volte sempre!')

    else:
        print('Opção Inválida. Tente novamente!')
        escolha = 0