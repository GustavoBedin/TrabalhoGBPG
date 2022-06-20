# O que é
Esse programa deixa o usuário escolher de uma selecao de 10 ótimos filtros e 5 belos stickers e alterar a sua foto de incontáveis maneiras. Após as alterações existe a possibilidade de salvar a nova foto editada.
# Como executar
Alguns imports são necessários para que o programa funcione, a seguir uma imagem com eles.\
![Imports](imagens%20md/imports.png)\
Apenas altere o local onde a foto dos stickers está armazenada no seu computador nas linhas: **163, 165, 167, 169, 171**.\
Caso a câmera esteja dando erro ao abrir provavelmente será necessario mudar a linha **178** de (0) para (1) ou algo parecido.\
Após realizar essas mudanças apenas execute o arquivo e seja feliz!

# Como funciona
Ao executar o arquivo depois de ter feito as devidas modificações, ele irá perguntar se o usuário deseja utilizar uma foto ou a câmera dele.
#### Arquivo
- Case seja selecionado abrir uma foto, o usuário deve passar o caminho de onde essa foto esta localizada.\
Duas janelas serão abertas para o usuário, as janelas "**Controle**" e "**Imagem**".

# Janela Controle 
## Trackbar 
Existem duas trackbars na janela controle que são utilizadas para mudar o filtro e aplicar stickers.\
A "**Efeitos**" vai de 0 a 10, cada uma correspondendo a um filtro diferente disponivel.\
A "**Stickers**" vai de 0 a 5, cada uma selecionando um sticker diferente.
![Trackbars](imagens%20md/trackbar_imagem.png)
## Filtros
Abaixo estão exemplos de cada filtro com o nome e o numero da trackbar para aplicar o filtro.
### Greyscale (1)
![Filtro 1](imagens%20md/filtro%201.png)
### Brightness Adjustment (2)
![Filtro 2](imagens%20md/filtro%202.png)
### Sharp Effect (3)
![Filtro 3](imagens%20md/filtro%203.png)
### Sepia Filter (4)
![Filtro 4](imagens%20md/filtro%204.png)
### Pencil Sketch Effect: Greyscale (5)
![Filtro 5](imagens%20md/filtro%205.png)
### Pencil Sketch Effect: Colour (6)
![Filtro 6](imagens%20md/filtro%206.png)
### HDR effect (7)
![Filtro 7](imagens%20md/filtro%207.png)
### Invert Filter (8)
![Filtro 8](imagens%20md/filtro%208.png)
### Summer Effect Filter (9)
![Filtro 9](imagens%20md/filtro%209.png)
### Winter Effect Filter (10)
![Filtro 10](imagens%20md/filtro%2010.png)

## Stickers
Os stickers disponiveis com o nome dele e o número da trackbar. Para aplicar um sticker ele deve estar selecionado e o usuário deve dar um double click esquerdo para determinar o ponto superior esquerdo do sticker.
### Fogo (1)
![Sticker 1](stickers/fogo.png)
### Estrela (2)
![Sticker 2](stickers/estrela.png)
### Bola (3)
![Sticker 3](stickers/bola.png)
### Arco-Iris (4)
![Sticker 4](stickers/arco-iris.png)
### Feliz (5)
![Sticker 5](stickers/feliz.png)

# Janela Imagem
Mostra a imagem ou o vídeo da camera com o filtro selecionado e os stickers colados, sera constantemente atualizada de acordo com os desejos do usuário.

# Salvar imagem e saida do programa
Para salvar, deve clicar duas vezes com o botao direito do mouse na imagem, isso resultara em uma nova imagem no diretório do programa com o nome sendo um numero aleatório entre 1 e 3000.\
Para sair do programa a tecla '**q**' deve ser pressionada.