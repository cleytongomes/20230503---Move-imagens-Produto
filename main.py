import configparser
import os
import shutil
import time
from shutil import make_archive

import tqdm
from PIL import Image
from pywebio import config, input, output, start_server
from rich import print

# leitura do arquivo de configuração
configparser = configparser.ConfigParser()
configparser.read('config.ini')

# leitura de parâmetros
arquivo = configparser.get('config', 'arquivo')
pasta_origem = configparser.get('config', 'pasta_origem')
pasta_destino = configparser.get('config', 'pasta_destino')
redimensionar = configparser.getboolean('config', 'redimensionar')
porta = configparser.get('config', 'port')
debug = configparser.getboolean('config', 'debug')
altura = configparser.getint('resize', 'altura')
largura = configparser.getint('resize', 'largura')


@config(theme='dark')
def main():

    # Título da página
    output.put_markdown('## DOWNLOAD DE PRODUTOS')

    # Lista de produtos ajustada
    produtos = input.textarea(
        'Nome dos produtos a serem baixados',
        rows=8,
        placeholder='Insira linha a linha os produtos que deseja realizar o download\nObs.: O programa pegará todos os produtos que sejam semelhantes aos códigos passados\n\nExemplo: 1130 => 1130ZCR, 1130BR, 113TBR, 1130TETRA...',
    )
    lista_produtos = list(
        map(lambda x: x.strip(), produtos.split('\n'))
    )   # transforma em lista e remove espaços
    lista_produtos = list(
        filter(bool, lista_produtos)
    )   # remove elementos vazios

    # Remove pasta de destino e cria novamente para apagar os arquivos
    shutil.rmtree(pasta_destino, ignore_errors=True)
    os.mkdir(pasta_destino)

    # Retira os nomes duplicados com set
    lista_produtos = list(set(lista_produtos))

    # Produtos dentro da pasta
    produtos_na_pasta = os.listdir(pasta_origem)

    # Percorre os produtos listados
    for produto in tqdm.tqdm(
        lista_produtos, desc='Copiando Imagens', unit=' Produtos'
    ):

        # Flag para marcar se achou algum produto semelhante
        flag_encontrado = False

        # Ajusta o produto
        produto = produto.upper().replace('/', '_')

        # verifica se o produto existe como imagem na pasta origem
        for produto_pasta in produtos_na_pasta:
            if produto_pasta.startswith(produto):
                flag_encontrado = True

                # Remove da lista
                produtos_na_pasta.remove(produto_pasta)

                if redimensionar:
                    # redimensiona imagem e move para pasta destino
                    img = Image.open(os.path.join(pasta_origem, produto_pasta))
                    img_resized = img.resize((largura, altura))
                    img_resized.save(
                        os.path.join(pasta_destino, produto_pasta)
                    )
                else:
                    # copia imagem para pasta destino
                    shutil.copy(
                        os.path.join(pasta_origem, produto_pasta),
                        pasta_destino,
                    )

        # Caso nenhum produto comece com o que foi digitado pelo usuário
        if flag_encontrado == False:
            output.put_markdown(f'- {produto} não encontrado')
            tqdm.tqdm.write('Produto não encontrado: ' + produto)

    # Cria o zip se existirem arquivos na pasta de destino
    if os.listdir(pasta_destino):
        make_archive('gerados/produtos', 'zip', pasta_destino)

        file = open('gerados/produtos.zip', 'rb')
        text = file.read()

        output.put_file('produtos.zip', text, 'Arquivo ZIP das Imagens')
    else:
        output.put_markdown('#### *Não há arquivos para serem baixados* ')

    # Chama o main novamente
    main()


# Mensagens do console
print('[red b]COPIADOR DE IMAGENS DE PRODUTOS[/red b]')
print(f'[italic]tentando conexão na porta {porta}[/italic]')
print(f'Acesse o painel pelo link: http://127.0.0.1:{porta}\n\n')

# Inicia o servidor
try:
    start_server(main, porta, debug=debug)
except Exception as e:
    print(f'[red]{e}[/red]')
    time.sleep(10)
