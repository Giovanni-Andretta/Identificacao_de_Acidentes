# Visão Computacional -- Identificação de Acidentes

****************************************************

| Nome da ferramenta  |  Versão  |
| ------------------  | -------- |
| Anaconda | 4.10.3 |
| Jupyter Notebook | 6.3.0 |
| Python | 3.8.8 |
| Opencv | 4.6.0 |
| Twilio | 7.12.0 |
| LabelImage | windows_v1.8.0 |
| Image downloader - Imageye | 3.0.7 |


****************************************************

# Instalação

## Anacondae e Jupyter Notebook

Para baixar e instalar o __Anaconda__ utilize o link abaixo:

[Anaconda](https://www.anaconda.com/)

O __Jupyter Notebook__ ja vem em conjunto com o Anaconda.

## Python

Para instalar o __Python__ na versão 3.8.8 abra o Anaconda Prompt e digite o comando abaixo:

```
conda install python=3.8.8
```

## Opencv

Para instalar o __Opencv__ na versão 4.6.0 abra o Anaconda Prompt e digite o comando abaixo:

```
pip install opencv-python==4.6.0
```

## Twilio

Para instalar o __Twilio__ abra o Anaconda Prompt e digite o comando abaixo:

```
pip install twilio==7.12.0
```

## LabelImage

Para a instalação do __LabelImg__ utilizando o __Anaconda__, abra o Anaconda Prompt e digite os comandos abaixo:

```
conda install pyqt=5
conda install -c anaconda lxml
pyrcc5 -o libs/resources.py resources.qrc
python labelImg.py
python labelImg.py [IMAGE_PATH] [PRE-DEFINED CLASS FILE]
```

Para mais informações, verifique: https://github.com/heartexlabs/labelImg

## Image downloader - Imageye

Para baixar e instalar o __Image downloader - Imageye__ utilize o link abaixo:

[Image downloader - Imageye](https://chrome.google.com/webstore/detail/image-downloader-imageye/agionbommeaifngbhincahgmoflcikhm)

****************************************************

# Funcionamento

***Para que o código funcione é preciso que você tenha os arquivos do modelo pré treinado do YOLO***, para gerar esses arquivos siga os passos abaixo:

## Dataset

Se você vai customizar seu próprio modelo pré treinado do YOLO, você irá precisar de um __Dataset__ e para te auxiliar com a coleta das imagens você pode utilizar:

- __Image downloader - Imageye__ que faz o download de várias imagens direto do google imagens.
- [Kaggle](https://www.kaggle.com/datasets) que é um site que disponibiliza inúmeros __Datasets__.

## LabelImg

Com o __Dataset__ ja em mãos, podemos utilizar o __LabelImg__.

- Acessar o __LabelImg__
- Clique em __Open Dir__ e selecione a pasta que você esta armazenando as imagens, e clique em Selecionar pasta.
- Clique em __Change Save Dir__ e selecione a mesma pasta que você selecionou no __Open Dir__ e clique em Selecionar pasta.
- Antes de começar, abaixo de __Save__, se estiver com __PascalVOC__, clique nele para aparecer __YOLO__.
- Clique em __Create RectBox__, va até onde o objeto que você quer que seja identificado pelo seu modelo e crie uma __Create RectBox__ entorno dele.
- Coloque o nome da sua __classe__, e clique em __OK__.
- Após criar todas as __Create RectBox__ na imagem, clique me __Save__.
- Clique em __Next Image__.
- Faça isso para todas as imagens.

Após fazer isso, você vai ter uma pasta com imagens, arquivos txt com o mesmo nome que as imagens contendo coordenadas dos Labels e o arquivo txt __classes__ contendo o nome da sua classe/s.

***O nome da pasta deve ser images, se for diferente, tera que ser alterado nos comandos do google colab***

- Acesse a pasta contendo as imagens, arquivos txt das labels e arquivo txt classes.
- Selecione tudo -- (Ctrl+a)
- Clique com o botão direito do mouse.
- Se tiver __Winrar__, selecione a opção __Adicionar para o arquivo...__ no campo __Formato do arquivo__, selecione a opção zip, e clique em __OK__
- Se não tiver __Winrar__, selecione a opção __Enviar para__ >> __Pasta compactada__

Após fazer isso, acesse seu drive.

***O nome da pasta deve ser yolov4, se for diferente, tera que ser alterado nos comandos do google colab***

- Clique em __Novo__
- Clique em __Nova pasta__
- Coloque o nome: __yolov4__
- Clique em __Criar__

Acesse sua pasta no google drive e envie o arquivo __images.zip__

## Google Colab


