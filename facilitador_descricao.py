import pyperclip  # Biblioteca para copiar o texto para a área de transferência
import os  # Módulo para interagir com o sistema de arquivos

# Limpar a tela do terminal (Windows)
os.system('cls')

# Solicitar o código do produto (Cp)
cp = input('Cp: ')

#! ENTRADA DAS INFORMAÇÕES
'''
AQUI VÃO AS ENTADAS DE INFORMAÇÕES DO PRODUTO

OBS: lembre de sempre verificar as entradas e descrições antes de começar a gerar as descrições
'''

# Criar a descrição com base nas informações definidas
descricao = f"COLOQUE AQUI A DESCRIÇÃO"
# Copiar a descrição para a área de transferência
pyperclip.copy(descricao)

# Definir o caminho onde o arquivo será salvo
pasta = fr"C:\\Users\\tsilva\\Desktop\\DescriçõesML\\(CATEGORIA DO PRODUTO A SER TRABALHADO)\\(CASO TENHA UMA SUB-CATEGORIA)\\{cp}"

# Nome do arquivo com o código do produto
nome_arquivo = f"{cp}.txt"

# Verificar se a pasta existe e criar, se necessário
if not os.path.exists(pasta):
    os.makedirs(pasta)

# Caminho completo do arquivo
caminho_arquivo = os.path.join(pasta, nome_arquivo)

# Criar e salvar o arquivo de texto com a descrição
with open(caminho_arquivo, "w") as arquivo:
    arquivo.write(descricao)

# Exibir o caminho do arquivo salvo
print(f"Arquivo salvo em: {caminho_arquivo}")

# Informar que o texto foi copiado para a área de transferência
print("\n\nTEXTO COPIADO PARA ÁREA DE TRANSFERÊNCIA\n\n")
