# PyPaint
Esse projeto faz parte de um repositório referente a todos os trabalhos da disciplina de Computação Gráfica e, por isso, para utilizá-lo será necessário baixar todo o repositório, incluindo possíveis futuros trabalhos distintos.

## Instalação & Execução
### Ubuntu
- Instale o gerenciador de pacotes PIP:

  ```
  $ sudo apt update
  $ sudo apt install python3-pip
  ```

- Baixe o repositório zipado ou clone utilizando o git (o caminho padrão, quando omitido, é ./comp-grafica):
  
  ```
  $ sudo apt update
  $ sudo apt install git
  $ git clone https://github.com/pucminas-luigidomenico/comp-grafica.git [caminho/para/repositorio]
  ``` 
  
- Navegue até a pasta raíz do projeto e instale as dependências necessárias para a execução do programa (numpy, pyqt5):

  ```
  $ cd caminho/para/repositório/py-paint
  $ sudo pip3 install -e .
  ```
  
- OBS: Em caso de erros relacionados a biblioteca tkinter, proceda da seguinte forma:

  ```
  $ sudo apt install python3-tk
  ```
 
- Uma vez dentro da pasta raíz do projeto, o execute:

  ```
  $ python3 pypaint
  ```
  
### Windows 10
- Instale o gerenciador de pacotes Chocolatey. Para isso, siga as instruções do link: https://chocolatey.org/install

- Baixe o repositório zipado ou, pelo CMD ou Powershell (ambos como administrador), clone o projeto utilizando o git (o caminho padrão, quando omitido, é .\comp-grafica):

  ```
  $ choco install git
  $ git clone https://github.com/pucminas-luigidomenico/comp-grafica.git [caminho/para/repositorio]
  ```
  
- Instale a versão 3 do Python:

  ```
  $ choco install python
  ```

- Feche e reabra o CMD/Powershell (como administrador) para garantir que as variáveis de ambiente estejam atualizadas

- Atualize o gerenciador de pacotes PIP:

  ```
  $ python -m pip install pip --upgrade
  ```
  
- Navegue até a pasta raíz do projeto e instale as dependências necessárias para a execução do programa (numpy, pyqt5):

  ```
  $ cd caminho\para\repositório\py-paint
  $ pip install -e .
  ```
  
- Uma vez dentro da pasta raíz do projeto, o execute:

  ```
  $ python .\pypaint
  ```

## Utilização
- Menu superior (Algoritmos):
  - Retas: selecione o algoritmo a ser usado na rasterização de retas (Bresenham ou DDA)
  - Recorte: selecione o algoritmo a ser usado pela ferramenta de recorte (Cohen-Sutherland ou Liang-Barsky)
  - Preenchimento: selecione o algoritmo a ser usado no preenchimento de áreas (Boundary-Fill ou Flood-Fill)
- Barra de ferramentas lateral:
  - Reta: Uma vez selecionada a ferramenta, basta clicar em um ponto, segurar e arrastar até o final da reta
  - Circunferência: Uma vez selecionada a ferramenta, basta clicar em um ponto, segurar e arrastar de acordo com o raio desejado
  - Preenchimento: Uma vez selecionada a ferramenta, basta clicar em um ponto interno a algum polígono fechado
  - Recorte: Uma vez selecionada a ferramenta, basta clicar em um ponto inicial e arrastar o mouse na diagonal, para criar a janela de visualização desejada
  - Transformações: Clicar na ferramenta abrirá uma janela contendo todas as 5 transformações. Basta selecionar a(s) transformação(ões) desejadas, informar os respectivos parâmetros e clicar no botão "OK"
  - Limpar Tela: Basta clicar na ferramenta, para apagar todos os desenhos

## Estrutura
- pypaint:
  - `<__main__.py>` (Inicialização do programa)
  - algorithm:
    - `<boundary_fill.py>` (Algoritmo Boundary-Fill, com conectividade 4)
    - `<flood_fill.py>` (Algoritmo Flood-Fill, com conectividade 4)
    - `<bresenham.py>` (Rasterização de retas e circunferências)
    - `<dda.py>` (Rasterização de retas)
    - `<cohen_sutherland.py>` (Recorte 2D para retas)
    - `<liang_barsky.py>` (Recorte 2D para retas)
    - `<transform2d.py>` (Translação, escala, rotação, reflexão e cisalhamento, além de funções auxiliares)
    - `<bezier.py>` (Curva de Bézier, além de funções auxiliares)
  - data:
    - `<circumferences.py>` (Contém uma classe auxiliar para armazenas todas as circunferências)
    - `<lines.py>` (Contém uma classe auxiliar para armazenas todas as retas)
  - gui
    - `<action.py>` (Contém uma classe auxiliar para as ferramentas do menu lateral)
    - `<dialog.py>` (Contém uma classe referente a caixa de diálogo das transformações)
    - `<icon.py>` (Funções auxiliares para construção dos ícones das ferramentas)
    - `<painter.py>` (Contém uma classe auxiliar referente a ação de desehar na tela)
    - `<toolbar.py>` (Contém uma classe auxiliar referente a barra lateral de ferramentas)
    - `<window.py>` (Janela principal da aplicação)
    
