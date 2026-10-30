import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
from time import sleep

# Configurações globais de estilo para os gráficos
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')

def carregar_dados() -> pd.DataFrame:
    """Carrega a base de dados eleitorais e aplica as transformações iniciais necessárias."""
    if not os.path.exists("C:\\Users\\Felipe\\Downloads\\Documentos\\Projetar Soluções Tecnologia\\trilha-felipe\\semana-04\\aula_estatistica_python\\eleicao_ficticia.csv"):
        print(f"Erro: O arquivo não foi encontrado na pasta atual.")
        print("Certifique-se de que o CSV está na mesma pasta do script.")
        sys.exit(1)
        
    df = pd.read_csv("C:\\Users\\Felipe\\Downloads\\Documentos\\Projetar Soluções Tecnologia\\trilha-felipe\\semana-04\\aula_estatistica_python\\eleicao_ficticia.csv")
    
    # Gerando colunas derivadas necessárias para as análises
    df['comparecimento'] = df['eleitores_aptos'] - df['abstencoes']
    df['votos_validos'] = df['votos_ana'] + df['votos_bruno'] + df['votos_carla']
    
    # Criando as taxas em porcentagem (%)
    df['taxa_abstencao'] = (df['abstencoes'] / df['eleitores_aptos']) * 100
    df['taxa_comparecimento'] = (df['comparecimento'] / df['eleitores_aptos']) * 100
    df['pct_brancos_nulos'] = ((df['votos_brancos'] + df['votos_nulos']) / df['comparecimento']) * 100
    
    return df

def exibir_cabecalho(titulo: str):
    """Imprime um cabeçalho visual padronizado no terminal."""
    print(f"\n--- {titulo.upper()} ---")

def exibir_menu():
    """Exibe as opções do menu no terminal."""
    print("""
==================================================
        ANÁLISE DE DADOS ELEITORAIS
==================================================
    [1] Item 1 (Conheça a base)
    [2] Item 2 (Qualidade dos dados)
    [3] Item 3 (Reconstrução de quantidades)
    [4] Item 4 (Taxas por seção)
    [5] Item 5 (Centro e dispersão)
    [6] Item 6 (Média simples vs Taxa global)
    [7] Item 7 (Comparação por Bairro)
    [8] Item 8 (Apuração das Candidaturas)
    [9] Item 9 (Produção de Gráficos)
    [10] Item 10 (Conclusão Responsável)
    [11] Desafio A (Associação e Correlação)
    [12] Desafio B (Simulação de Amostragem)
    [0] Sair
================================================== """)

def executar_item_1(df: pd.DataFrame):
    exibir_cabecalho("Dimensão da Base (Linhas, Colunas)")
    print(df.shape)

    exibir_cabecalho("Primeiras 5 Linhas")
    print(df.head())

    exibir_cabecalho("Informações e Tipos das Colunas")
    print(df.info())

    exibir_cabecalho("Quantidade de Seções e Bairros Únicos")
    print(f"Quantidade de Seções: {df['secao'].nunique()}")
    print(f"Quantidade de Bairros: {df['bairro'].nunique()}")

    exibir_cabecalho("Valores Ausentes por Coluna")
    print(df.isna().sum())

    exibir_cabecalho("Linhas Completamente Duplicadas")
    print(f"Total de linhas duplicadas: {df.duplicated().sum()}")

    exibir_cabecalho("Validação de Unicidade da Coluna 'secao'")
    print(f"A coluna 'secao' possui valores únicos? {df['secao'].is_unique}")

def executar_item_2(df: pd.DataFrame):
    exibir_cabecalho("Tabela de Registros que Violam as Regras")
    colunas_contagem = [
        'eleitores_aptos', 'abstencoes', 'votos_brancos', 
        'votos_nulos', 'votos_ana', 'votos_bruno', 'votos_carla'
    ]

    violacao_tipo_ou_sinal = pd.Series(False, index=df.index)
    for col in colunas_contagem:
        invalido = (df[col] < 0) | (df[col] % 1 != 0)
        violacao_tipo_ou_sinal = violacao_tipo_ou_sinal | invalido

    violacao_abstencao = df['abstencoes'] > df['eleitores_aptos']
    violacao_secao_duplicada = df['secao'].duplicated(keep=False)

    df_violacoes = df[violacao_tipo_ou_sinal | violacao_abstencao | violacao_secao_duplicada]

    if df_violacoes.empty:
        print("Sucesso! Nenhuma linha violou as regras de consistência. A tabela está vazia.")
    else:
        print(df_violacoes)

def executar_item_3(df: pd.DataFrame, totais: dict):
    df_temp = df.copy()
    df_temp['verificacao_valida'] = df_temp['comparecimento'] == (
        df_temp['votos_validos'] + df_temp['votos_brancos'] + df_temp['votos_nulos']
    )

    exibir_cabecalho("Verificação de Consistência por Seção (Todas devem ser True)")
    print(df_temp[['secao', 'comparecimento', 'votos_validos', 'verificacao_valida']])

    exibir_cabecalho("Totais Gerais da Eleição no Município")
    print(f"Total de Eleitores Aptos: {totais['aptos']}")
    print(f"Total de Abstenções:     {totais['abstencoes']}")
    print(f"Total de Comparecimento: {totais['comparecimento']}")
    print(f"Total de Votos Válidos:  {totais['votos_validos']}")

def executar_item_4(df: pd.DataFrame):
    exibir_cabecalho("As 3 Seções com Maior Taxa de Abstenção")
    df_maiores_abstencoes = df.sort_values(by='taxa_abstencao', ascending=False).head(3)
    print(df_maiores_abstencoes[['secao', 'bairro', 'eleitores_aptos', 'taxa_abstencao']].round(2))

def executar_item_5(df: pd.DataFrame):
    def calcular_estatisticas_descritivas(df_dados: pd.DataFrame, coluna: str, nome_exibicao: str, unidade: str = ""):
        serie = df_dados[coluna]
        minimo = serie.min()
        maximo = serie.max()
        q1 = serie.quantile(0.25)
        q3 = serie.quantile(0.75)
        
        exibir_cabecalho(f"Medidas Descritivas: {nome_exibicao}")
        print(f"Média:                  {serie.mean():.2f} {unidade}")
        print(f"Mediana:                {serie.median():.2f} {unidade}")
        print(f"Mínimo:                 {minimo:.2f} {unidade}")
        print(f"Máximo:                 {maximo:.2f} {unidade}")
        print(f"Amplitude:              {(maximo - minimo):.2f} {unidade}")
        print(f"1º Quartil (Q1):        {q1:.2f} {unidade}")
        print(f"3º Quartil (Q3):        {q3:.2f} {unidade}")
        print(f"Intervalo Interquartil: {(q3 - q1):.2f} {unidade}")
        print(f"Desvio Padrão Pop (σ):  {serie.std(ddof=0):.2f} {unidade}")

    calcular_estatisticas_descritivas(df, 'eleitores_aptos', "Eleitores Aptos", "eleitores")
    calcular_estatisticas_descritivas(df, 'taxa_abstencao', "Taxa de Abstenção", "p.p.")

def executar_item_6(df: pd.DataFrame, totais: dict):
    media_simples_taxas = df['taxa_abstencao'].mean()
    taxa_global_abstencao = (totais['abstencoes'] / totais['aptos']) * 100
    diferenca_pp = abs(media_simples_taxas - taxa_global_abstencao)

    exibir_cabecalho("Comparação: Média Simples vs. Taxa Global de Abstenção")
    print(f"Média Simples das Taxas:  {media_simples_taxas:.4f}%")
    print(f"Taxa Global de Abstenção: {taxa_global_abstencao:.4f}%")
    print(f"Diferença Absoluta:       {diferenca_pp:.4f} p.p.")

def executar_item_7(df: pd.DataFrame):
    exibir_cabecalho("Comparação dos Bairros")
    df_bairros = df.groupby('bairro')[['eleitores_aptos', 'abstencoes', 'comparecimento', 'votos_validos']].sum()
    df_bairros['taxa_abstencao_bairro'] = (df_bairros['abstencoes'] / df_bairros['eleitores_aptos']) * 100
    df_bairros_ordenados = df_bairros.sort_values(by='taxa_abstencao_bairro', ascending=False)
    
    print(df_bairros_ordenados[['eleitores_aptos', 'abstencoes', 'taxa_abstencao_bairro']].round(2))

def executar_item_8(df: pd.DataFrame, totais: dict):
    exibir_cabecalho("Apuração das Candidaturas")

    total_ana = df['votos_ana'].sum()
    total_bruno = df['votos_bruno'].sum()
    total_carla = df['votos_carla'].sum()

    percentual_ana = (total_ana / totais['votos_validos']) * 100
    percentual_bruno = (total_bruno / totais['votos_validos']) * 100
    percentual_carla = (total_carla / totais['votos_validos']) * 100

    print("Votação Geral no Município:")
    print(f"Ana:   {total_ana} votos ({percentual_ana:.2f}%)")
    print(f"Bruno: {total_bruno} votos ({percentual_bruno:.2f}%)")
    print(f"Carla: {total_carla} votos ({percentual_carla:.2f}%)")

    votos_gerais = pd.Series({'Ana': total_ana, 'Bruno': total_bruno, 'Carla': total_carla})
    votos_gerais_ordenados = votos_gerais.sort_values(ascending=False)
    
    vencedor_geral = votos_gerais_ordenados.index[0]
    segundo_geral = votos_gerais_ordenados.index[1]
    dif_votos = votos_gerais_ordenados.iloc[0] - votos_gerais_ordenados.iloc[1]
    
    pct_gerais = pd.Series({'Ana': percentual_ana, 'Bruno': percentual_bruno, 'Carla': percentual_carla})
    dif_pp = pct_gerais[vencedor_geral] - pct_gerais[segundo_geral]
    
    print(f"\nCandidatura mais votada no geral: {vencedor_geral}")
    print(f"Diferença para o 2º colocado ({segundo_geral}): {dif_votos} votos ({dif_pp:.2f} p.p.)")
    
    print("\nCandidatura mais votada por Bairro:")
    df_votos_bairro = df.groupby('bairro')[['votos_ana', 'votos_bruno', 'votos_carla']].sum()
    df_votos_bairro['Mais Votado'] = df_votos_bairro.idxmax(axis=1).str.replace('votos_', '').str.capitalize()
    print(df_votos_bairro[['votos_ana', 'votos_bruno', 'votos_carla', 'Mais Votado']])

def executar_item_9(df: pd.DataFrame):
    exibir_cabecalho("Produzindo os Três Gráficos")
    
    df_bairros = df.groupby('bairro')[['eleitores_aptos', 'abstencoes']].sum()
    df_bairros['taxa_abstencao_bairro'] = (df_bairros['abstencoes'] / df_bairros['eleitores_aptos']) * 100
    df_bairros_ordenados = df_bairros.sort_values(by='taxa_abstencao_bairro', ascending=False)

    # Gráfico (a): Barras com a taxa de abstenção por bairro
    plt.figure(figsize=(8, 5))
    plt.bar(df_bairros_ordenados.index, df_bairros_ordenados['taxa_abstencao_bairro'], color='royalblue', edgecolor='black')
    plt.title('Taxa de Abstenção por Bairro', fontsize=14, pad=15)
    plt.xlabel('Bairro', fontsize=12)
    plt.ylabel('Taxa de Abstenção (%)', fontsize=12)
    plt.ylim(0, max(df_bairros_ordenados['taxa_abstencao_bairro']) + 5)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    for i, v in enumerate(df_bairros_ordenados['taxa_abstencao_bairro']):
        plt.text(i, v + 0.5, f"{v:.2f}%", ha='center', va='bottom', fontsize=10, fontweight='bold')
        
    plt.savefig("abstencao_por_bairro.png", dpi=150, bbox_inches="tight")
    plt.close()
    print("[Gráfico A] 'abstencao_por_bairro.png' salvo com sucesso!")

    # Gráfico (b): Histograma
    plt.figure(figsize=(8, 5))
    plt.hist(df['taxa_abstencao'], bins=6, color='seagreen', edgecolor='black', alpha=0.8)
    plt.title('Distribuição da Taxa de Abstenção das Seções', fontsize=14, pad=15)
    plt.xlabel('Taxa de Abstenção por Seção (%)', fontsize=12)
    plt.ylabel('Número de Seções (Frequência)', fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    plt.savefig("histograma_abstencao.png", dpi=150, bbox_inches="tight")
    plt.close()
    print("[Gráfico B] 'histograma_abstencao.png' salvo com sucesso!")

    # Gráfico (c): Dispersão
    plt.figure(figsize=(8, 5))
    plt.scatter(df['eleitores_aptos'], df['taxa_abstencao'], color='crimson', edgecolor='black', s=50, alpha=0.8)
    plt.title('Dispersão: Tamanho da Seção vs. Taxa de Abstenção', fontsize=14, pad=15)
    plt.xlabel('Eleitores Aptos por Seção (Quantidade)', fontsize=12)
    plt.ylabel('Taxa de Abstenção na Seção (%)', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.5)
    
    plt.savefig("dispersao_aptos_vs_abstencao.png", dpi=150, bbox_inches="tight")
    plt.close()
    print("[Gráfico C] 'dispersao_aptos_vs_abstencao.png' salvo com sucesso!")
    
    print("\nOBSERVAÇÕES E LEITURA DOS GRÁFICOS:")
    print("1. Gráfico de Barras: O Centro exibe a maior taxa de evasão proporcional, enquanto o Jardim apresenta o eleitorado mais assíduo.")
    print("2. Histograma: Mostra que a abstenção na maioria das seções se concentra entre 14% e 26%, com um pico nítido de seções registrando taxas na faixa de 18% a 22%.")
    print("3. Gráfico de Dispersão: Os pontos mapeados revelam que não há um padrão linear óbvio ou inclinação forte; seções grandes e pequenas flutuam de forma parecida na taxa de abstenção.")

def executar_item_10():
    exibir_cabecalho("Conclusão Responsável")
    conclusao = (
        "A eleição fictícia registrou uma taxa global de abstenção de 19.25% no município, "
        "com a candidatura de Ana sendo a mais votada ao conquistar um total de 3.176 votos (39.40% dos válidos). "
        "A análise geográfica aponta um contraste entre os bairros: o Centro registrou a maior evasão proporcional com "
        "21.43% de abstenção, enquanto o bairro Serra apresentou o maior volume absoluto de faltosos e deu a vitória local para Carla. "
        "Como limitação metodológica relevante, esses dados são puramente agregados por seção eleitoral, o que configura um "
        "impedimento técnico para inferir o comportamento de voto individual ou determinar de forma factual as causas da abstenção."
    )
    print(conclusao)
    print(f"\nNota de entrega: O texto consolidado possui {len(conclusao.split('. '))} sentenças estruturadas para o relatório técnico.")

def executar_desafio_a(df: pd.DataFrame):
    exibir_cabecalho("Desafio A: Associação e Correlação Pearson")
    correlacao = df["eleitores_aptos"].corr(df["taxa_abstencao"])
    
    print(f"Coeficiente de correlação de Pearson (r): {correlacao:.4f}")
    print("\nInterpretação Estatística:")
    print(f"O valor encontrado de {correlacao:.2f} indica uma correlação linear extremamente fraca (praticamente nula).")
    print("Isso confirma visualmente o que foi observado no gráfico de dispersão do Item 9: os pontos estão espalhados")
    print("e o tamanho de uma seção eleitoral (quantidade de aptos) não influencia a sua taxa de abstenção.")
    print("\nCuidado Metodológico Importante:")
    print("Correlação não demonstra causalidade. Além disso, por se tratar de dados agregados, este resultado")
    print("não reflete o comportamento individual dos eleitores (evitando a falácia ecológica).")

def executar_desafio_b(df: pd.DataFrame, totais: dict):
    exibir_cabecalho("Desafio B: Simulação de Amostragem")
    
    amostra_fixa = df.sample(n=6, random_state=42)
    taxa_amostra_42 = (amostra_fixa['abstencoes'].sum() / amostra_fixa['eleitores_aptos'].sum()) * 100
    taxa_global_real = (totais['abstencoes'] / totais['aptos']) * 100
    
    print("Resultado da Amostra Única (Semente 42):")
    print(f"Taxa de Abstenção da Amostra (6 seções): {taxa_amostra_42:.2f}%")
    print(f"Taxa de Abstenção Global Real (População): {taxa_global_real:.2f}%")
    print(f"Diferença da estimativa: {abs(taxa_amostra_42 - taxa_global_real):.2f} p.p.")
    
    estimativas_taxas = []
    for semente in range(100):
        amostra_simulada = df.sample(n=6, random_state=semente)
        taxa_estimada = (amostra_simulada['abstencoes'].sum() / amostra_simulada['eleitores_aptos'].sum()) * 100
        estimativas_taxas.append(taxa_estimada)
        
    print("\nGerando Histograma das 100 estimativas amostrais...")
    plt.figure(figsize=(8, 5))
    plt.hist(estimativas_taxas, bins=10, color='gold', edgecolor='black', alpha=0.8)
    plt.axvline(taxa_global_real, color='red', linestyle='--', linewidth=2, label=f'Taxa Real: {taxa_global_real:.2f}%')
    
    plt.title('Distribuição Amostral das 100 Estimativas (n=6)', fontsize=13, pad=15)
    plt.xlabel('Taxa de Abstenção Estimada (%)', fontsize=11)
    plt.ylabel('Frequência de Sorteios', fontsize=11)
    plt.legend()
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    plt.show()
    
    print("\nExplicação da Variabilidade Amostral:")
    print("O gráfico gerado demonstra o Teorema Central do Limite e o conceito de erro amostral.")
    print("Cada sorteio resulta em um valor diferente porque amostras pequenas (n=6) são altamente suscetíveis")
    print("ao acaso e podem selecionar seções que não representam bem a realidade de todos os bairros.")

def main():
    # 1. Carregar base de dados de forma segura utilizando caminho relativo
    df = carregar_dados()
    
    # Dicionário centralizado com os totais gerais da população
    totais = {
        'aptos': df['eleitores_aptos'].sum(),
        'abstencoes': df['abstencoes'].sum(),
        'comparecimento': df['comparecimento'].sum(),
        'votos_validos': df['votos_validos'].sum()
    }

    while True:
        exibir_menu()
        try:
            escolha = int(input("Escolha uma opção (0 para Sair): "))
        except ValueError:
            print("Entrada inválida! Por favor, digite um número inteiro.")
            continue

        if escolha == 0:
            print("\nSaindo do programa... Até logo!")
            break
        elif escolha == 1:
            executar_item_1(df)
        elif escolha == 2:
            executar_item_2(df)
        elif escolha == 3:
            executar_item_3(df, totais)
        elif escolha == 4:
            executar_item_4(df)
        elif escolha == 5:
            executar_item_5(df)
        elif escolha == 6:
            executar_item_6(df, totais)
        elif escolha == 7:
            executar_item_7(df)
        elif escolha == 8:
            executar_item_8(df, totais)
        elif escolha == 9:
            executar_item_9(df)
        elif escolha == 10:
            executar_item_10()
        elif escolha == 11:
            executar_desafio_a(df)
        elif escolha == 12:
            executar_desafio_b(df, totais)
        else:
            print("Opção inválida! Escolha um número presente no menu.")
            
        print("\nRetornando ao menu principal em 2 segundos...")
        sleep(2)

if __name__ == "__main__":
    main()