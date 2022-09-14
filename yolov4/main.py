import cv2
import time
import threading
from twilio.rest import Client

#Inicializa a variaveis globais de contagens
#Controle da função send
aux = 0;

#Valor em tempo real de número de acidentes indentificados
accidentCounter = 0;

#Função para fazer o reset da variável aux apos 30 minutos
def reset():
    
    #Chama a váriavel global
    global aux
    
    #Espera 30 minutos
    time.sleep(1800)
    
    #Zera a variável aux
    aux = 0

#Função para fazer a chamada que ira transmitir as informações
def send(counter, score):
    
    #Chama a váriavel global
    global aux
    
    #Formata o valor da váriavel
    score = round(score*100, 2)

    #Dados informados na sua conta twilio
    account_sid = ""
    auth_token = ""
    numero_twilio = ""
    meu_numero = ""

    #Faz a ponte entre o codigo e a internet utilizando seu SID e seu TOKEN da twilio, para fazer a ligação
    cliente = Client(account_sid, auth_token)

    #Envia as informações acima, e faz a ligação
    ligacao = cliente.messages.create(
        to=meu_numero,
        from_=numero_twilio,
        body="Acidente detectado! Foi identificado " + str(counter) + " acidente com precisão de " + str(score) + "% de ser um acidente! Acione as autoridades responsáveis para verificar o local!"
    )
    
    #Adiciona 1 na váriavel de controle
    aux+=1

#Carrega o conteudo para análise (pode ser uma câmera ou um vídeo em um arquivo)
cap = cv2.VideoCapture("../data/any_video.mp4");

#Identifica a resolução do vídeo (será usado para definir a resolução da saída)
vwidth = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH) + 0.5)
vheight = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT) + 0.5)
size = (vwidth, vheight)

#Inicializa a saída do vídeo
fourcc = cv2.VideoWriter_fourcc(*'MP4V')
out = cv2.VideoWriter('../results/output.mp4', fourcc, 30.0, size)

#Seleciona o modelo que será usado na detecção
net = cv2.dnn.readNet('../modelo_pre_treinado/yolov4_training_last.weights', '../modelo_pre_treinado/yolov4_testing.cfg')

#Seta o modelo de detecção no OpenCV
model = cv2.dnn_DetectionModel(net)
model.setInputParams(size=(416,416), scale=1/255)

#Loop para percorrer os quadros
while (cap.isOpened()):
    #inicia a contagem do tempo do quadro
    start = time.time()

    #Captura o quadro
    _, frame = cap.read()

    #Realiza o scan no quadro
    classes, scores, boxes = model.detect(frame, 0.1, 0.2)

    #fecha a contagem do tempo do quadro
    end = time.time()

    #Variavel contadora de detecções
    counter = 0

    #Percorre as detecções feitas no quadro
    for(classid, score, box) in zip(classes, scores, boxes):
        # Precisão minima de 50%
        if (score > .70):
            counter+=1
            #Amarelo 0,255,150
            #Vermelho 0,0,255
            color = (0,0,255)
            cv2.rectangle(frame, box, color, 1)

            #Escreve acima da box a precisão da detecção
            cv2.rectangle(frame, (box[0]-10, box[1]-25, 75, 25), (0,0,0), -1)
            cv2.putText(frame, f"{str(round((score*100), 1))}%", (box[0], box[1] - 10), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255), 2)
            
            #Verifica se o valor da váriavel é zero
            if (aux == 0):
            
                #Chama a função responsável a enviar as mensagens
                threading.Thread(target=send(counter, score)).start()
                
                #Chama a função responsável a resetar o valor da variável de controle aux
                threading.Thread(target=reset).start()
                
    
    #Seta a contagem na variavel global
    accidentCounter = counter

    #Imprime no frame a contagem de acidentes
    accident_label = f"Acidentes: {accidentCounter}"
    cv2.rectangle(frame, (0,0), (110,25), (0,0,0), -1)
    cv2.putText(frame, accident_label, (0,15), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255), 2)

    #imprime no frame o FPS
    fps = f"FPS: {round((1.0/(end - start)), 2)}"
    cv2.rectangle(frame, (0,50), (110,25), (0,0,0), -1)
    cv2.putText(frame, fps, (0,45), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255), 2)
    
    #Grava o quadro no vídeo de saída
    out.write(frame)

    #Mostra o quadro detectado
    cv2.namedWindow('detections', cv2.WINDOW_NORMAL)
    cv2.imshow('detections', frame)
        
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
