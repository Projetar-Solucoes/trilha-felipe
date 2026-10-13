# Dicionário de dados — solicitações

Base: `solicitacoes_semana4.csv`, com 246 linhas na origem e 240 após a limpeza. Cada linha é uma solicitação (chamado) aberta por um colaborador.

As descrições foram deduzidas dos nomes das colunas e dos valores vistos no notebook. Confirme com quem forneceu a base se algum significado estiver diferente.

| Coluna | Tipo no pandas | O que é | Exemplo | Valores / observações |
|---|---|---|---|---|
| `protocolo` | texto | Número de identificação da solicitação, no formato `ano-número`. | `2026-0173` | Sem vazios. |
| `data_abertura` | texto (deveria ser data) | Data em que a solicitação foi aberta. | `2026-09-26` | Dois formatos misturados (`AAAA-MM-DD` e `DD/MM/AAAA`). Sem vazios. |
| `solicitante` | texto | Nome de quem abriu a solicitação. | `Marta Dias` | Sem vazios. |
| `setor` | texto | Setor do solicitante. | `Atendimento` | Vistos: Atendimento, Comercial, Operações, RH. 10 vazios. |
| `categoria` | texto | Tipo da solicitação, depois de padronizada. | `Suporte TI` | Acesso, Dúvida, Financeiro, Infraestrutura, Suporte TI. Veio com 15 grafias, hoje são 5. |
| `assunto` | texto | Descrição curta do que foi pedido. | `Impressora sem conexão` | Texto livre. Também apareceram `Acesso ao sistema de ponto`, `Horário do plantão` e `Cadeira quebrada`. |
| `prioridade` | texto | Urgência dada à solicitação. | `Alta` | Baixa, Média, Alta, Urgente, ou `Não Informada` (14 que estavam vazias). Ainda há versões em CAIXA ALTA a corrigir. |
| `status` | texto | Situação atual da solicitação. | `Concluída` | Aberta, Em andamento, Concluída, Cancelada. |
| `data_fechamento` | texto (deveria ser data) | Data em que a solicitação foi concluída. | `2026-09-03` | Vazia para quem não foi concluída (111 na base original). |
| `avaliacao` | decimal | Nota que o solicitante deu ao atendimento. | `4.0` | Escala esperada de 1 a 5. Vazia quando não houve avaliação (122 na base original). |
| `unidade` | texto | Unidade onde a solicitação foi feita. | `Parambu` | Parambu e Solonópole (123 linhas cada na base original). Sem vazios. |
