# FII Data Extractor

Este é um programa em Python que extrai dados de cotações de Fundos de Investimento Imobiliário (FII) do site [Funds Explorer](www.fundsexplorer.com.br).

## Declaração de responsabilidade
Não somos responsáveis pela violação de qualquer direito autoral com o uso desse programa. Use por sua própria responsabilidade e lembre-se de dar crédito ao [www.fundsexplorer.com.br](www.fundsexplorer.com.br).

## Dependências
Esse programa usa os seguintes pacotes:

- argparse
- tqdm
- selenium
- pandas
- datetime
- webdriver_manager

Certifique-se de ter esses pacotes instalados em seu ambiente de trabalho Python antes de executar o programa.

## Como usar
Para executar o programa, siga os seguintes passos:

1. Clone este repositório para o seu computador local.
2. Navegue até o diretório onde o arquivo está localizado no seu terminal.
3. Execute o script com o comando `python3 extrator_cotacoes_fiis.py`.

Você pode personalizar a lista de fundos de seu interesse alterando a lista `funds` no script. Por padrão, o programa irá filtrar os dados para exibir apenas informações sobre os fundos especificados nessa lista.

### Argumentos
O programa aceita os seguintes argumentos:

- `-v` ou `--version`: Retorna a versão do programa.
- `-o` ou `--output`: Especifique o nome de saída do seu arquivo. O padrão é `fundsexplorer_ranking_output.csv`.

Por exemplo, para especificar um nome de arquivo de saída diferente, você pode executar o programa como:

```
python3 extrator_cotacoes_fiis.py -o output.csv
```

## Saída
O programa irá raspar dados do site [Funds Explorer](www.fundsexplorer.com.br) e salvará os dados em um arquivo CSV no diretório local. O arquivo de saída inclui todas as informações encontradas na tabela do site. Além disso, o script filtra os dados para exibir apenas informações sobre os fundos especificados na lista `funds`.

## Atualizações
Este programa está atualmente na versão 1.0.0. Fique à vontade para contribuir com o desenvolvimento deste projeto enviando um pull request ou abrindo um issue no GitHub.


## Licença
Este programa é distribuído sob a licença MIT. Consulte o arquivo `LICENSE` para obter mais detalhes.