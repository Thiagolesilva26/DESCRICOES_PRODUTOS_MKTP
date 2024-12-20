# GERADOR DE DESCRIÇÃO DE PRODUTOS MERCADO LIVRE

Este projeto tem como objetivo gerar descrições de produtos para facilitar o processo de criação de anúncios em marketplaces, como o Mercado Livre. Ele permite a criação de descrições personalizadas com base nas informações inseridas pelo usuário e gera arquivos de texto que podem ser usados diretamente nas plataformas de vendas.

## Funcionalidades

- Geração automática de descrições detalhadas para produtos.
- Formatação de texto otimizada para SEO, incluindo características, especificações e dúvidas frequentes.
- Criação de arquivos de texto com as descrições geradas.
- Cópia automática do texto para a área de transferência, facilitando o uso em plataformas de vendas.

## Tecnologias Utilizadas

- **Python 3.x**: Linguagem utilizada para o desenvolvimento do sistema.
- **pyperclip**: Biblioteca para copiar o texto gerado para a área de transferência.
- **os**: Módulo para interagir com o sistema de arquivos.

## Como Usar

1. Execute o script `facilitador_descricao.py`.
2. O sistema solicitará o código do produto (Cp). Insira o código desejado.
3. Altere o prompt da descrição de acordo com o produto que está sendo trabalhado.
4. O script irá gerar uma descrição completa para o produto, salvar o arquivo de texto na pasta correspondente e copiar o texto para a área de transferência.
5. O arquivo será salvo em uma estrutura de pastas baseada no código do produto. Exemplo de caminho do arquivo: 
   `C:\Users\<usuário>\Desktop\DescriçõesML\(CATEGORIA DO PRODUTO)\(SUBCATEGORIA)\<Cp>\<Cp>.txt`.

## Exemplo de Execução

```
===========================================================================================

Cp: 12345  
Arquivo salvo em: C:\Users\<usuário>\Desktop\DescriçõesML\ALICATES\OUTROS\12345\12345.txt  
TEXTO COPIADO PARA A AREA DE TRANSFERÊNCIA

===========================================================================================
```

## Estrutura do Arquivo de Texto Gerado

O arquivo gerado contém as seguintes seções:

- **Nome do Produto**: Informações como o nome e descrição do produto.
- **Características Principais**: Lista com as principais funcionalidades do produto.
- **Especificações Técnicas**: Informações sobre o tamanho, material, tipo e marca.
- **Aplicações e Vantagens**: Benefícios do uso do produto em diferentes áreas de atuação.
- **Dúvidas Frequentes**: Perguntas comuns com respostas rápidas para os clientes.

## Modelo de Descrição para Novos Produtos

Para gerar as descrições de novos produtos, utilize o seguinte modelo:

Obs: Atualmente utilizo o Chatgpt para gerar as descrições

```
{nomeProduto} – Praticidade e Desempenho em Um Kit Compacto

===========================================================

O {nomeProduto} da marca {marca} é ideal para quem busca praticidade e precisão em tarefas de corte, crimpagem e manipulação de fios. Com design compacto e robusto, o kit mini alicate oferece a mesma performance das ferramentas tradicionais, sendo perfeito para profissionais que exigem ferramentas versáteis e de alta resistência em um formato compacto.

CARACTERÍSTICAS PRINCIPAIS:
- Versatilidade: Ideal para cortes e crimpações em diferentes tipos de fios e cabos.
- Design Compacto: Fácil de armazenar e ideal para trabalhos em espaços apertados.
- Alta Qualidade: Fabricado em {material}, garantindo durabilidade e resistência.
- Ergonomia: Confortável e fácil de manusear, proporcionando maior precisão durante o trabalho.

ESPECIFICAÇÕES TÉCNICAS:
- Tamanho: 4.1/2"
- Material: {material}
- Tipo: Kit Mini Alicate
- Marca: {marca}

APLICAÇÕES E VANTAGENS: O {nomeProduto} é perfeito para eletricistas, mecânicos e profissionais que necessitam de ferramentas compactas e de alto desempenho para trabalhos de precisão, especialmente em locais de difícil acesso.

Por que Escolher o {nomeProduto}?
- Compacto e Prático: Desempenho de ferramentas grandes em um formato menor.
- Durabilidade: Resistência e longa vida útil.
- Versatilidade: Ideal para diversos tipos de trabalhos.
```

Basta substituir as variáveis `{nomeProduto}`, `{marca}`, `{material}` e outras informações conforme necessário para cada produto novo.

## Observação

Ja existe um local que está sendo guardado as descrições ja criadas, para acessa peça ao responsavél atual (Tsilva)
Atualizado em (25/11/2024)

