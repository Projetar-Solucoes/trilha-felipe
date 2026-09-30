# Como usar o Git neste projeto

Um guia rápido para consultar quando bater a dúvida. Guarde este arquivo — ele vale para a trilha inteira e para o seu primeiro emprego.

## O ciclo de todo dia

```bash
git status                  # 1. O que mudou?
git add .                   # 2. Prepara as mudanças
git commit -m "mensagem"    # 3. Grava no histórico
git push                    # 4. Envia para o GitHub
```

Rode `git status` sempre que ficar em dúvida. Ele diz em que situação cada arquivo está.

## Mensagens de commit

Escreva **o que mudou**, como se completasse a frase *"este commit…"*:

| ✔ Assim | ✘ Assim não |
|---|---|
| `adiciona validação do e-mail no cadastro` | `update` |
| `corrige erro quando o arquivo não existe` | `ajustes` |
| `semana 3: salva as solicitações em JSON` | `commit`, `.`, `asdf` |

Um commit = uma mudança. Se você precisa escrever "e" na mensagem, provavelmente eram dois commits.

## Trabalhando com branch e pull request

É assim que as equipes trabalham: ninguém mexe direto na `main`.

```bash
git checkout -b semana-04          # cria a branch e muda para ela
# ... faz as mudanças, add e commit ...
git push -u origin semana-04       # envia a branch (só na primeira vez precisa do -u)
```

Depois, no GitHub: **Compare & pull request** → escreva o que fez → **Create pull request**.
Espere a revisão, responda os comentários e só então clique em **Merge pull request**.

Para voltar para a `main` e trazer o que foi juntado:

```bash
git checkout main
git pull
```

## Deu errado. E agora?

| Situação | Comando |
|---|---|
| Quero ver o que mudei e ainda não preparei | `git diff` |
| Mudei um arquivo e quero voltar como estava no último commit | `git restore nome-do-arquivo.py` |
| Fiz `git add` de algo sem querer | `git restore --staged nome-do-arquivo.py` |
| Preciso desfazer um commit que já foi para o GitHub | `git revert <código-do-commit>` |
| Quero ver o histórico | `git log --oneline` |

**Nunca** suba senha, chave ou arquivo `.env`. Se subiu sem querer, avise o instrutor: apagar o arquivo não basta, a senha continua no histórico e precisa ser trocada.
