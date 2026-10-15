# Relatório de qualidade — base de solicitações

Base original: **246 linhas × 11 colunas** (`solicitacoes_semana4.csv`).
Base após a limpeza: **240 linhas × 11 colunas**.

| Problema | Linhas afetadas | O que eu fiz |
|---|---|---|
| Linhas repetidas | 6 | Removi com `drop_duplicates()`. A base foi de 246 para 240 linhas. |
| Categoria escrita de jeitos diferentes (15 grafias para 5 categorias: `ACESSO`, `acesso`, `Infra`, `infraestrutura`, `Duvida`, `dúvida`, `suporte ti`, ` Suporte TI` com espaço, `Suporte de TI`, `financeiro`...) | 151 de 246 (as outras 95 já estavam no padrão) | Apliquei `.str.strip().str.lower()` e depois `.map()` com um dicionário de padronização. Conferi com `.isna().sum()`: **0 nulos** após o mapeamento, então nenhuma grafia ficou de fora. Resultado: Dúvida 52, Infraestrutura 51, Acesso 48, Financeiro 46, Suporte TI 43. |
| Status com maiúscula/minúscula misturada (`cancelada`, `concluída`, `em andamento`) | 11 de 246 | Apliquei `.str.capitalize()`. Ficaram 4 valores: Concluída 132, Em andamento 48, Cancelada 31, Aberta 29. |
| Prioridade vazia | 14 | Preenchi com `"Não Informada"` (`fillna`), para não perder a linha nem inventar uma prioridade. |
| Prioridade em CAIXA ALTA (`BAIXA`, `MÉDIA`, `ALTA`, `URGENTE`) | 11 de 246 (10 após remover duplicadas) | **Identificado, mas ainda não corrigido no notebook.** Hoje `Baixa` e `BAIXA` contam como valores diferentes. Correção sugerida: `df["prioridade"].str.capitalize()`. |
| Setor vazio | 10 | **Não tratado.** Mantive vazio. Se for preciso agrupar por setor, sugiro preencher com `"Não Informado"`. |
| `data_abertura` em dois formatos (`2026-09-26` e `18/08/2026`) | Não contei | **Não tratado.** A coluna continua como texto (`object`). Antes de calcular tempo de atendimento, convertê-la com `pd.to_datetime(..., format="mixed", dayfirst=True)` e conferir o resultado. |
| `data_fechamento` vazia | 111 | Mantive vazia, de propósito. 111 é exatamente Aberta (30) + Em andamento (49) + Cancelada (32) na base original, ou seja, só tem data de fechamento quem foi concluída. |
| `avaliacao` vazia | 122 | Mantive vazia (`NaN`). A média do pandas ignora esses valores. |
| Avaliações para análise | 119 notas válidas (entre 1 e 5) na base limpa | Filtrei notas entre 1 e 5 para o cálculo das médias, em uma cópia (`df_temp`), sem alterar o `df`. A base original tinha 124 notas preenchidas. A diferença de 5 mistura notas que saíram junto com as duplicadas e possíveis notas fora do intervalo, e as saídas do notebook não permitem separar as duas. Para saber, rode `df["avaliacao"].dropna().between(1, 5).value_counts()`. |

## Validação

- A soma das categorias (240) bate com o total de linhas da base limpa (240).

## Resultado: média de avaliação por categoria (notas de 1 a 5)

| Categoria | Média |
|---|---|
| Financeiro | 4,04 |
| Acesso | 3,95 |
| Dúvida | 3,80 |
| Suporte TI | 3,79 |
| Infraestrutura | 3,43 |

Infraestrutura é a categoria com a pior avaliação.

## Pendências

1. Padronizar `prioridade` (caixa alta).
2. Converter `data_abertura` e `data_fechamento` para data.
3. Decidir o que fazer com `setor` vazio.
4. Conferir quantas avaliações estão fora do intervalo de 1 a 5.
