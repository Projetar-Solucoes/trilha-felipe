from datetime import date
from time import sleep
import json
import os

ARQUIVO_JSON = "solicitações.json"

SETORES = {
    "1": "Financeiro",
    "2": "Atendimento ao Cliente",
    "3": "Suporte Técnico",
    "4": "Vendas",
    "5": "Marketing"}

CATEGORIAS = {
    "1": "Suporte",
    "2": "Acesso",
    "3": "Sistema"}

PRIORIDADES = {
    "1": "Alta",
    "2": "Média",
    "3": "Baixa"}

def dormir(segundos):
    sleep(segundos)

def carregar_dados():
    if not os.path.exists(ARQUIVO_JSON):
        return[]
    try:
        with open(ARQUIVO_JSON, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        print("\n Erro ao ler arquivo JSON. Iniciando com uma lista vazia.")
        return []

def salvar_dados(solicitacoes):
    try:
        with open(ARQUIVO_JSON, "w", encoding="utf-8") as f:
            json.dump(solicitacoes, f, indent=4, ensure_ascii=False)
    except IOError:
        print("\nErro ao salvar dados no arquivo JSON.")

def testar_vazio(frase):
    variavel = input(frase).strip()
    while not variavel:
        variavel = input("Campo inválido digite novamente: ").strip()
    return variavel

def obter_ano_valido():
    while True:
        try:
            ano_str = testar_vazio("Digite o ano da solicitação: ")
            ano = int(ano_str)
            ano_atual = date.today().year
            if 2000 <= ano <= ano_atual:
                return ano
            print(f"Ano Inválido. Digite um ano entre 2000 e {ano_atual}.")
        except ValueError:
            print("Digite um número de ano válido (Ex: 2025).")

def escolher_opcao_menu():
    while True:
        try:
            escolha = input("Escolha uma opção: ").strip()
            if escolha in ["1", "2", "3","4", "5"]:
                return escolha
            print("Opção inexistente no menu. Tente novamente.")
        except Exception:
            print("Entrada Inválida")

def exibir_menu():
    print("\n" + "="*40)
    print("      CENTRAL DE SOLICITAÇÕES - M3      ")
    print("="*40)
    print("[1] Cadastrar Solicitação")
    dormir(1)
    print("[2] Listar Todas as Solicitações")
    dormir(1)
    print("[3] Consultar Solicitação por Protocolo")
    dormir(1)
    print("[4] Visualizar Estatísticas")
    dormir(1)
    print("[5] Sair")
    dormir(1)
    print("-"*40)

def cadastrar_solicitacao(solicitacoes):
    print('\n --- NOVO CADASTRO ---')
    dormir(1)
    ano = obter_ano_valido()
    dormir(1)
    nome = testar_vazio("Digite seu nome: ").title()
    dormir(1)

    proximo_numero = len(solicitacoes) + 1
    numero_protocolo_str = str(proximo_numero).zfill(4)
    nomes = nome.upper().split()
    iniciais = ''.join([palavra[0] for palavra in nomes])
    protocolo = f"{ano}-{numero_protocolo_str}-{iniciais}"

    print("\nSetores Disponíveis:")
    for k, v in SETORES.items():
        print(f"[{k}] {v}")
        dormir(1)
    setor_opcao = input("Escolha o setor: ").strip()
    dormir(1)
    while setor_opcao not in SETORES:
        setor_opcao = input("Setor Inválido. Escolha novamente: ")
    setor = SETORES[setor_opcao]

    print("\nCategorias Disponíveis:")
    for k, v in CATEGORIAS.items():
        print(f"[{k}] {v}")
        dormir(1)
    categoria_opcao = input("Escolha a categoria: ").strip()
    dormir(1)
    while categoria_opcao not in CATEGORIAS:
        categoria_opcao = input("Categoria Inválida. Escolha novamente: ").strip()
    categoria = CATEGORIAS[categoria_opcao]

    print("\nNíveis de Prioridade:")
    for k, v in PRIORIDADES.items():
        print(f"[{k}] {v}")
        dormir(1)
    prioridade_opcao = input("Escolha a prioridade: ").strip()
    dormir(1)
    while prioridade_opcao not in PRIORIDADES:
        prioridade_opcao = input("Prioridade Inválida. Escolha novamente: ").strip()
    prioridade = PRIORIDADES[prioridade_opcao]
                
    assunto = testar_vazio('Qual o assunto da sua solicitação? ')
    descricao = testar_vazio('Por favor, descreva sua solicitação detalhadamente: ')
    dormir(1)
    print('Cadastrando solicitação...')
    dormir(1)

    nova_solicitacao = {
        "protocolo": protocolo,
        "nome": nome,
        "setor": setor,
        "categoria": categoria,
        "assunto": assunto,
        "descricao": descricao,
        "prioridade": prioridade}

    solicitacoes.append(nova_solicitacao)
    salvar_dados(solicitacoes)

    print("-"*40)
    print(f"Solicitação de Protocolo {protocolo} Cadastrada com Sucesso!")
    dormir(3)
    print("-"*40)

def listar_solicitacao(solicitacoes):
    if not solicitacoes:
        print("\nNenhuma solicitação cadastrada no sistema")
        return

    print("\n================ LISTA DE SOLICITAÇÕES ================")
    for sol in solicitacoes:
        print(f"\nProtocolo: {sol['protocolo']}")
        dormir(1)
        print(f"Nome: {sol['nome']} | Setor: {sol['setor']}")
        dormir(1)
        print(f"Categoria: {sol['categoria']} | Prioridade: {sol['prioridade']}")
        dormir(1)
        print(f"Assunto: {sol['assunto']}")
        dormir(1)
        print(f"Descrição: {sol['descricao']}")
        dormir(3)
        print("-" * 50)

def consultar_solicitacao(solicitacoes):
    print("\n--- CONSULTA DE PROTOCOLO ---")
    busca = input("Digite o protocolo completo (Ex: 2026-001-JAP): ").strip().upper()
    
    encontrado = False
    for s in solicitacoes:
        if s["protocolo"].upper() == busca:
            print("\nDADOS DA SOLICITAÇÃO ENCONTRADA:")
            print(f"Protocolo:  {s['protocolo']}")
            dormir(1)
            print(f"Nome:       {s['nome']}")
            dormir(1)
            print(f"Setor:      {s['setor']}")
            dormir(1)
            print(f"Categoria:  {s['categoria']}")
            dormir(1)
            print(f"Prioridade: {s['prioridade']}")
            dormir(1)
            print(f"Assunto:    {s['assunto']}")
            dormir(1)
            print(f"Descrição:  {s['descricao']}")
            dormir(3)
            encontrado = True
            break
            
    if not encontrado:
        print(f"\nO protocolo '{busca}' não foi encontrado no sistema.")

def mostrar_estatistica(solicitacoes):
    total = len(solicitacoes)
    print('\n=== ESTATÍSTICAS ===')
    print(f'Total de Solicitações: {total}')
    dormir(1)
    cont_prioridade = {"Alta": 0, "Média": 0, "Baixa": 0}
    cont_categoria = {"Suporte": 0, "Acesso": 0, "Sistema": 0}

    for sol in solicitacoes:
        p = sol.get("prioridade")
        c = sol.get("categoria")
        if p in cont_prioridade:
            cont_prioridade[p] += 1
        if c in cont_categoria:
            cont_categoria[c] += 1
            
    print("\nPor prioridade:")
    for k, v in cont_prioridade.items():
        print(f"  {k}: {v}")
        dormir(1)
        
    print("\nPor categoria:")
    for k, v in cont_categoria.items():
        print(f"  {k}: {v}")
        dormir(1)
    print("=" * 20)