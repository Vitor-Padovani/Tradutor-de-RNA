# Tradutor de RNA

Software feito com *Python* e *SQLite3* que converte as sequências de **Nucleotídios**, de um RNA, nos **Aminoácidos** e **Proteínas** que este produz.

## Estrutura

A estrutura do programa é simples, contando com o executável *main.py* e dois arquivos '*.txt*': 

1. ( */input/input.txt* ) - para o RNA que vai ser traduzido 
2. ( */output/output.txt* ) - para o resultado da tradução

Exemplo:

- Input

```
CAUGCAGCGUGA
```

- Output ( se comando = 'all' )

| Número | Códon | Aminoácidos |
|--------|-------|-------------|
| 1      | CAU   | Histidina   |
| 2      | GCA   | Alanina     |
| 3      | GCG   | Alanina     |
| 4      | UGA   | -           |

## Comandos

Ao executar *main.py*, será pedido a opção de tradução:
- 'all' - numera os códons e suas proteínas 
- 'ptn' - numera e mostra proteínas 
- 'cdn' - mostra apenas os códons 
- '   ' - fecha o programa
