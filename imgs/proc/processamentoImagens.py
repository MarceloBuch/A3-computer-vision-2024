# Importando bibliotecas

import cv2
import os

# Arquivos processados pelo Google Drive para não prejudicar desempenho
path_image = '/content/drive/My Drive/A3-computer-vision-2024/imgs/orig/'
path_destino = '/content/drive/My Drive/A3-computer-vision-2024/imgs/proc/video.mp4'

images = []

# Verificando imagens que serão adicionadas no vídeo
for name_path in sorted(os.listdir(path_image)):  
    caminho_arquivo = os.path.join(path_image, name_path)
    if os.path.isfile(caminho_arquivo):
        images.append(caminho_arquivo)

if len(images) == 0:
    print("Nenhuma imagem encontrada para criar o vídeo.")
else:
    img_exemplo = cv2.imread(images[0])
    altura, largura, _ = img_exemplo.shape

    fps = 20  
    codec = cv2.VideoWriter_fourcc(*"mp4v")  
    video = cv2.VideoWriter(path_destino, codec, fps, (largura, altura))

    for imagem in images:
        img = cv2.imread(imagem)
        video.write(img)  

    video.release()
    print(f"Vídeo criado com sucesso em: {path_destino}")