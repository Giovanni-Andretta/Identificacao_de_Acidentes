# Visão Computacional -- Identificação de Acidentes

****************************************************

| Nome da ferramenta  |  Versão  |
| ------------------  | -------- |
| Anaconda | 4.10.3 |
| Jupyter Notebook | 6.3.0 |
| Python | 3.8.8 |
| Opencv-python | 4.6.0.66 |
| Twilio | 7.12.0 |
| LabelImage | windows_v1.8.0 |
| Image downloader - Imageye | 3.0.7 |
| charset-normalizer | 2.1.0 |
| idna | 3.3 |
| numpy | 1.23.2 |
| PyJWT | 2.4.0 |
| pytz | 2022.2.1 |
| requests | 2.28.1 |
| urllib3 | 1.26.11 |


****************************************************

# Instalação

## Anacondae e Jupyter Notebook

Para baixar e instalar o __Anaconda__ utilize o link abaixo:

[Anaconda](https://www.anaconda.com/)

O __Jupyter Notebook__ ja vem em conjunto com o __Anaconda__.

## Python

Para instalar o __Python__ na versão 3.8.8 utilizando o __Anaconda__, abra o __Anaconda Prompt__ e digite o comando abaixo:

```
conda install python=3.8.8
```

## Virtualenv

Para que seja instalado os pacotes nas versões corretas utilize o comando:

```
pip install -r requirements.txt
```

## LabelImage

Para a instalação do __LabelImg__ utilizando o __Anaconda__, abra o __Anaconda Prompt__ e digite os comandos abaixo:

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

Nessa etapa você deve decidir qual arquivo de pesos pré-treinado você usará, a diferença deles está em questão de tamanho e performance, exemplos abaixo:

***CPU utilizado foi um i5-9300H***

- __yolov4.conv.137__ utilizando esse modelo você terá uma média de __2.5 fps__ rodando em ***CPU***, valores de precisão e detecção __ótimos__, o tempo de treino no Google Colab é aproximadamente __16 horas__
- __yolov4-tiny.conv.29__ utilizando esse modelo você terá uma média de __10 fps__ rodando em ***CPU***, valores de precisão e detecção __inferiores__, o tempo de treino no Google Colab é aproximadamente __5 horas__

Após decidir qual arquivo de peso você utilizará para treinar seu modelo, siga as instruções abaixo:

- Entre no [Google Colab]https://colab.research.google.com/
- Logue com sua conta
- No canto esquerdo superior clique na opção __Editar__
- Clique em __Configurações de notebook__
- Em __Acelerador de hardware__ coloque a opção __GPU__ e clique em __Salvar__
- Siga os passos dos arquivos [google_colab](https://github.com/GiovanniAndrettaCarbonero/Identificacao_de_Acidentes/tree/main/google_colab)

Quando o treinamento for concluído, em sua pasta __yolov4__ do __Google Drive__ deve conter os arquivos:

1. classes.txt
2. images.zip
3. yolov4_testing.cfg
4. yolov4_training_1000.weights
5. yolov4_training_2000.weights
6. yolov4_training_3000.weights
7. yolov4_training_4000.weights
8. yolov4_training_final.weights
9. yolov4_training_last.weights

Você tera que baixar os arquivos: classes.txt, yolov4_testing.cfg e yolov4_training_last.weights, coloque-os dentro da pasta [modelo_pre_treinado](https://github.com/GiovanniAndrettaCarbonero/Identificacao_de_Acidentes/tree/main/modelo_pre_treinado)

Para mais informações do YOLO acesse https://github.com/AlexeyAB/darknet


Com isso o código ja irá funcionar!

Basta comentar a linha [104](https://github.com/GiovanniAndrettaCarbonero/Identificacao_de_Acidentes/blob/e10a38ac8393966ad6138853f6c1a4a673c0fdb2/yolov4/main.py#L104) até a linha [110](https://github.com/GiovanniAndrettaCarbonero/Identificacao_de_Acidentes/blob/e10a38ac8393966ad6138853f6c1a4a673c0fdb2/yolov4/main.py#L110) para que não envie um SMS ao detectar um acidente, se não quiser comentar as linhas siga os passos abaixo.

## Twilio

Para que a mensagem seja enviada, é preciso que se crie uma conta no [Twilio](https://www.twilio.com/)

Ao logar no __Twilio__ você precisa fazer a solicitação de seu número __Twilio__ para fazer isso clique em __Get a Twilio phone number__.
Após isso, descendo a página irá ter o campo __Account Info__ que deve conter as segunintes informações:

- Account SID
- Auth Token
- My Twilio phone number

Essas informações deverão ser preenchidas no código

- [#Dados informados na sua conta twilio](https://github.com/GiovanniAndrettaCarbonero/Identificacao_de_Acidentes/blob/125b3934a42dd1577e324ab48c8f29cb229e83b5/yolov4/main.py#L34)
