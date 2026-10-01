# nome, setor, categoria, assunto e descrição
print("Seja bem-vindo(a) ao nosso setor de reclamações! Estamos aqui para ouvir suas preocupações e ajudá-lo(a) da melhor forma possível.")

nome = input('Qual o seu nome? ')
lista_setores = ['Financeiro', 'Atendimento ao Cliente', 'Suporte Técnico', 'Vendas', 'Marketing']
setor = input(f'Qual setor você deseja entrar em contato? (Escolha entre: {", ".join(lista_setores)}) ')
if setor not in lista_setores:
    print('Setor inválido. Por favor, escolha um setor válido da lista.')
else:
    categoria = input('Qual a categoria da sua reclamação? ')
    assunto = input('Qual o assunto da sua reclamação? ')
    descricao = input('Por favor, descreva sua reclamação detalhadamente: ')
    print(f'Obrigado, {nome}. Sua reclamação foi registrada no \n setor de {setor} \n com a categoria "{categoria}", \n assunto "{assunto}" \n e descrição: "{descricao}".')