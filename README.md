# Copiando imagens de produtos
Este é um programa em Python que lê um arquivo CSV com nomes de produtos e copia as imagens correspondentes da pasta de origem para a pasta de destino.

## Configuração
O programa lê as configurações a partir do arquivo config.ini. As seguintes configurações são necessárias:

- arquivo: o caminho completo para o arquivo CSV que contém os nomes dos produtos.
- pasta_origem: a pasta de onde as imagens dos produtos serão copiadas.
- pasta_destino: a pasta para onde as imagens dos produtos serão copiadas.


## Utilização
Para utilizar este programa, você precisa ter Python 3 instalado em sua máquina.

1 - Clone este repositório em sua máquina local.

2 - Crie um arquivo config.ini na raiz do projeto e configure as seguintes opções:

```
[config]
arquivo = caminho/para/arquivo.csv
pasta_origem = caminho/para/pasta/origem
pasta_destino = caminho/para/pasta/destino
```

3 - Execute o programa com o comando python nome_do_programa.py na pasta raiz do projeto.

O programa percorre o arquivo CSV de produtos e verifica se a imagem correspondente a cada produto existe na pasta de origem. Se existir, a imagem é copiada para a pasta de destino. Se não existir, uma mensagem é exibida indicando que o produto não foi encontrado.

Este programa utiliza a biblioteca csv para ler o arquivo CSV, a biblioteca os para verificar se o arquivo existe na pasta de origem e a biblioteca shutil para copiar o arquivo para a pasta de destino. Ele também utiliza a biblioteca tqdm para exibir uma barra de progresso enquanto as imagens são copiadas.
