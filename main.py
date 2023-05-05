import configparser
import os
import shutil
from shutil import make_archive

import tqdm
from PIL import Image
from pywebio import config, input, output, start_server

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

@config(theme="dark")
def main():

    output.put_markdown('## DOWNLOAD DE PRODUTOS')

    # Lista de produtos ajustada
    produtos = input.textarea("Nome dos produtos a serem baixados", rows=8, placeholder="Produtos que deseja realizar o download")
    lista_produtos = list(map(lambda x: x.strip(),produtos.split('\n'))) # transforma em lista e remove espaços
    lista_produtos = list(filter(bool, lista_produtos)) # remove elementos vazios

    # Remove pasta de destino e cria novamente para apagar os arquivos
    shutil.rmtree(pasta_destino, ignore_errors=True)
    os.mkdir(pasta_destino)

    # Percorre os produtos listados
    for produto in tqdm.tqdm(lista_produtos, desc='Copiando imagens', unit=' Produtos'):

        # Ajusta o produto
        produto = produto.upper().replace('/', '_')

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
            output.put_markdown(f"- {produto} não encontrado")
            tqdm.tqdm.write('Produto não encontrado: ' + produto)

    # Cria o zip se existirem arquivos na pasta de destino
    if os.listdir(pasta_destino):
        make_archive('gerados/saida', 'zip', pasta_destino)

        file = open('gerados/saida.zip', 'rb')
        text = file.read()

        output.put_file('saida.zip', text, 'Arquivo ZIP das Imagens')
    else:
        output.put_markdown('#### *Não há arquivos para serem baixados* ')

    # Chama o main novamente
    main()


# Inicia o servidor
start_server(main, port=8082, debug=True)