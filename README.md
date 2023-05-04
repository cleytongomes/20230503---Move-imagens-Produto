# Copiando imagens de produtos
Este é um programa em Python que lê um arquivo CSV com nomes de produtos e copia as imagens correspondentes da pasta de origem para a pasta de destino.

## Configuração
O programa lê as configurações a partir do arquivo config.ini. As seguintes configurações são necessárias:

- arquivo: o caminho completo para o arquivo CSV que contém os nomes dos produtos.
- pasta_origem: a pasta de onde as imagens dos produtos serão copiadas.
- pasta_destino: a pasta para onde as imagens dos produtos serão copiadas.
- redimensionamento: Caso queira que as imagens sejam redimensionadas antes de serem copiadas.

Caso seja optado pelo redimensionamento, dois parâmetros devem ser preenchidos:
- largura: largura da imagem redimensionada.
- altura: altura da imagem redimensionada.

## Utilização
Para utilizar este programa, você precisa ter o Python 3 instalado em sua máquina.

1 - Clone este repositório em sua máquina local.

2 - Crie um arquivo config.ini na raiz do projeto e configure as seguintes opções:

```
[config]
arquivo = caminho/para/arquivo.csv
pasta_origem = caminho/para/pasta/origem
pasta_destino = caminho/para/pasta/destino
redimensionar = True

[resize]
largura=1750
altura=1750
```

3 - Execute o programa com o comando abaixo na pasta raiz do projeto.
```
python main.py
```

O programa percorre o arquivo CSV de produtos e verifica se a imagem correspondente a cada produto existe na pasta de origem. Se existir, a imagem é copiada para a pasta de destino. Se não existir, uma mensagem é exibida indicando que o produto não foi encontrado.

Este programa utiliza a biblioteca csv para ler o arquivo CSV, a biblioteca os para verificar se o arquivo existe na pasta de origem e a biblioteca shutil para copiar o arquivo para a pasta de destino. Ele também utiliza a biblioteca tqdm para exibir uma barra de progresso enquanto as imagens são copiadas. Além dela, caso a imagem precise ser redimensionada, usa a biblioteca Pillow para esse procedimento.
