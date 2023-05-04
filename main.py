import configparser
import csv
import os
import shutil
import tqdm
from PIL import Image

# leitura do arquivo de configuração
configparser = configparser.ConfigParser()
configparser.read('config.ini')

# leitura de parâmetros
arquivo = configparser.get('config', 'arquivo')
pasta_origem = configparser.get('config', 'pasta_origem')
pasta_destino = configparser.get('config', 'pasta_destino')
redimensionar = configparser.getboolean('config', 'redimensionar')
altura = configparser.getint('resize', 'altura')
largura = configparser.getint('resize', 'largura')

# abre arquivo de produtos
file = open(arquivo, 'r')
reader = csv.reader(file)

# percorre arquivo de produtos
for linha in tqdm.tqdm(reader, desc='Copiando imagens', unit=' linhas'):

    # Ajusta o produto
    produto = linha[0].strip().upper()
    produto = produto.replace('/', '_')

    # verifica se o produto existe como imagem na pasta origem
    if (produto + '.jpg') in os.listdir(pasta_origem):

        if redimensionar:
            # redimensiona imagem e move para pasta destino
            img = Image.open(os.path.join(pasta_origem, produto + '.jpg'))
            img_resized = img.resize((largura, altura))
            img_resized.save(os.path.join(pasta_destino, produto + '.jpg'))

        else:
            # copia imagem para pasta destino
            shutil.copy(os.path.join(pasta_origem, produto + '.jpg'), pasta_destino)

    else:
        tqdm.tqdm.write('Produto não encontrado: ' + produto)
