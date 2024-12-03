# importando bibliotecas e classe
import cv2


# Função para achar o centro do objeto, será utilizada na detecção dele
def center(x, y, w, h):
    x1 = int(w / 2)
    y1 = int(h / 2)

    cx = x + x1
    cy = y + y1

    return cx, cy

def detectionVideo():
    #cap = cv2.VideoCapture('./imgs/test/1.mp4')
    cap = cv2.VideoCapture('./imgs/proc/video.mp4')
    scale = 0.5
    Total = 0
    Up = 0
    Down = 0

    detects = []

    posL = 450
    offset = 40

    xy1 = (245, posL)
    xy2 = (645, posL)

    fgbg = cv2.createBackgroundSubtractorMOG2()

    # Iniciando tratamento e analise das imagens
    while True:
        ret, frame = cap.read()

        # Verifica se o vídeo acabou
        if not ret or frame is None:
            print("fim do vídeo.")
            break

        # Redimensionando o video para facilitar a visualização
        rw = int(frame.shape[1] * scale)
        rh = int(frame.shape[0] * scale)
        framer = cv2.resize(frame, (rw, rh))

        #print(framer.shape[1]) #x = 960
        #print(framer.shape[0]) #y = 540
            
        # Processamento dos frames 

            # Step 1 - Escala de cinza 
        gray = cv2.cvtColor(framer, cv2.COLOR_BGR2GRAY)

            # Step 2 - Blur
        fgblur = fgbg.apply(gray)

            # Step 3 - Binarização
        retval, th = cv2.threshold(fgblur, 200, 255, cv2.THRESH_BINARY)

            # Padronizando objetos vistos e aumentando area para melhorar a detecção
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))

        opening = cv2.morphologyEx(th, cv2.MORPH_OPEN, kernel, iterations = 2)

        dilation = cv2.dilate(opening,kernel,iterations = 8)

        closing = cv2.morphologyEx(dilation, cv2.MORPH_CLOSE, kernel, iterations = 8)

        #cv2.imshow("closing", closing)

        # Adicionando faixa aonde será realizada o tracking do objeto e a contagem dele
        # Linha Central
        cv2.line(framer,xy1,xy2,(255,0,0),3)
        # Linhas secundarias 
        cv2.line(framer,(xy1[0],posL-offset),(xy2[0],posL-offset),(255,255,0),2)
        cv2.line(framer,(xy1[0],posL+offset),(xy2[0],posL+offset),(255,255,0),2)
            
        # Step 4 - Encontrando contornos do objeto
        contours, hierarchy = cv2.findContours(closing,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

        i = 0
        for cnt in contours: 
            (x, y, w, h) = cv2.boundingRect(cnt)

            area = cv2.contourArea(cnt)

            # Desenhando retangulo no objeto encontrado
            if int(area) > 3000:
                centro = center(x, y, w, h)
                cv2.putText(framer, str(i), (x+5, y+15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255),2)
                cv2.circle(framer, centro, 4, (0, 0,255), -1)
                cv2.rectangle(framer,(x,y),(x+w,y+h),(0,255,0),2)

                    # Se é um objeto não reconhecido, é adicionado a detecção
                if len(detects) <= i:
                        detects.append([])
                    
                    # Verifica se o centro do objeto esta entre a faixa de detecção
                if centro[1] > posL - offset and centro[1] < posL + offset:
                    detects[i].append(centro) 
                    #print(detects)
                    #print(Total, Up, Down)

                # Zerando os dados de cada objeto no tracking 
                else:
                    detects[i].clear()
                i += 1 

        # Verifica se existe imagem no momento, se não haver, limpar detecções
        if i == 0:
            detects.clear()

        if len(contours) == 0:
            detects.clear()

        # Se existe contorno, ele entra para verificar os detectados e trackear o objeto
        else:
            for detect in detects:
                for (c, l) in enumerate(detect):
                    # Iniciando tracking do objeto
                        
                    # Analisando se objeto esta subindo
                    if detect[c-1][1] < posL and l[1] > posL:
                        detect.clear()
                        Up += 1
                        Total += 1
                        cv2.line(framer, xy1, xy2, (0,255,0), 5)
                        continue

                    # Analisando se objeto esta descendo
                    if detect[c-1][1] > posL and l[1] < posL:
                        detect.clear()
                        Down += 1
                        Total += 1
                        cv2.line(framer, xy1, xy2, (0,255,0), 5)
                        continue

                    if c > 0:
                        cv2.line(framer, detect[c-1], l, (0,0,255), 1)

        # Exibindo dados que foram extraídos
        cv2.putText(framer, "TOTAL: "+str(Total), (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255),2)
        cv2.putText(framer, "SUBINDO: "+str(Up), (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0),2)
        cv2.putText(framer, "DESCENDO: "+str(Down), (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255),2)

        yield {"up": Up, "down": Down, "total": Total}

        cv2.imshow("real", framer)
            
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


