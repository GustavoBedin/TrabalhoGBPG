import cv2
import numpy as np
from scipy.interpolate import UnivariateSpline
import random

def LookupTable(x, y):
  spline = UnivariateSpline(x, y)
  return spline(range(256))

def Winter(img):
    
    increaseLookupTable = LookupTable([0, 64, 128, 256], [0, 80, 160, 256])
    decreaseLookupTable = LookupTable([0, 64, 128, 256], [0, 50, 100, 256])
    blue_channel, green_channel,red_channel = cv2.split(img)
    red_channel = cv2.LUT(red_channel, decreaseLookupTable).astype(np.uint8)
    blue_channel = cv2.LUT(blue_channel, increaseLookupTable).astype(np.uint8)
    win= cv2.merge((blue_channel, green_channel, red_channel))
    
    return win

def Summer(img):
    increaseLookupTable = LookupTable([0, 64, 128, 256], [0, 80, 160, 256])
    decreaseLookupTable = LookupTable([0, 64, 128, 256], [0, 50, 100, 256])
    blue_channel, green_channel,red_channel  = cv2.split(img)
    red_channel = cv2.LUT(red_channel, increaseLookupTable).astype(np.uint8)
    blue_channel = cv2.LUT(blue_channel, decreaseLookupTable).astype(np.uint8)
    sum= cv2.merge((blue_channel, green_channel, red_channel ))
    return sum

def invert(img):
    inv = cv2.bitwise_not(img)
    return inv

def HDR(img):
    hdr = cv2.detailEnhance(img, sigma_s=12, sigma_r=0.15)
    return  hdr

def pencil_sketch_col(img):
    #inbuilt function to create sketch effect in colour and greyscale
    sk_gray, sk_color = cv2.pencilSketch(img, sigma_s=60, sigma_r=0.07, shade_factor=0.1) 
    return  sk_color

def pencil_sketch_grey(img):
    #inbuilt function to create sketch effect in colour and greyscale
    sk_gray, sk_color = cv2.pencilSketch(img, sigma_s=60, sigma_r=0.07, shade_factor=0.1) 
    return  sk_gray

def sepia(img):
    img_sepia = np.array(img, dtype=np.float64) # converting to float to prevent loss
    img_sepia = cv2.transform(img_sepia, np.matrix([[0.272, 0.534, 0.131],
                                    [0.349, 0.686, 0.168],
                                    [0.393, 0.769, 0.189]])) # multipying image with special sepia matrix
    img_sepia[np.where(img_sepia > 255)] = 255 # normalizing values greater than 255 to 255
    img_sepia = np.array(img_sepia, dtype=np.uint8)
    return img_sepia

def sharpen(img):
    kernel = np.array([[-1, -1, -1], [-1, 9.5, -1], [-1, -1, -1]])
    img_sharpen = cv2.filter2D(img, -1, kernel)
    return img_sharpen

def bright(img, beta_value ):
    img_bright = cv2.convertScaleAbs(img, beta=beta_value)
    return img_bright

def greyscale(img):
    greyscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return greyscale

def filters(imagem, pos):
    match pos:
        case 0:
            return imagem
        case 1:
            return greyscale(imagem)
        case 2:
            return bright(imagem, 60)
        case 3:
            return sharpen(imagem)
        case 4:
            return sepia(imagem)
        case 5:
            return pencil_sketch_grey(imagem)
        case 6:
            return pencil_sketch_col(imagem)
        case 7:
            return HDR(imagem)
        case 8:
            return invert(imagem)
        case 9:
            return Summer(imagem)
        case 10:
            return Winter(imagem)

def nomeAleatorio():
    return random.randint(1, 3000)

def nothing(x):
    pass

def overlay_transparent(background, overlay, x, y):


    background_width = background.shape[1]
    background_height = background.shape[0]

    if x >= background_width or y >= background_height:
        return background

    h, w = overlay.shape[0], overlay.shape[1]

    if x + w > background_width:
        w = background_width - x
        overlay = overlay[:, :w]

    if y + h > background_height:
        h = background_height - y
        overlay = overlay[:h]

    if overlay.shape[2] < 4:
        overlay = np.concatenate(
            [
                overlay,
                np.ones((overlay.shape[0], overlay.shape[1], 1), dtype = overlay.dtype) * 255
            ],
            axis = 2,
        )

    overlay_image = overlay[..., :3]
    mask = overlay[..., 3:] / 255.0

    background[y:y+h, x:x+w] = (1.0 - mask) * background[y:y+h, x:x+w] + mask * overlay_image

    return background

def sticker(event,x,y,flags,param):
    global img
    if event == cv2.EVENT_LBUTTONDBLCLK:
        
        match posSticker:
            case 1:
                img = overlay_transparent(img, fogo, x, y)
            case 2:
                img = overlay_transparent(img, estrela, x, y)
            case 3:
                img = overlay_transparent(img, bola, x, y)
            case 4:
                img = overlay_transparent(img, arco, x, y)
            case 5:
                img = overlay_transparent(img, feliz, x, y)   

    elif event == cv2.EVENT_RBUTTONDBLCLK:
        nome = nomeAleatorio()
        cv2.imwrite(str(nome)+".png", img)

def trackbarMouseCb():
    cv2.namedWindow('Controle')
    cv2.namedWindow("Imagem")
    cv2.createTrackbar('Efeitos','Controle',0,10,nothing)
    cv2.createTrackbar('Stickers', 'Controle', 1, 5, nothing)
    cv2.setMouseCallback('Imagem', sticker)

fogo = cv2.imread("Stickers/fogo.png" , cv2.IMREAD_UNCHANGED)
fogo = cv2.resize(fogo, (100, 54))
estrela = cv2.imread("Stickers/estrela.png" , cv2.IMREAD_UNCHANGED)
estrela = cv2.resize(estrela, (92, 51))
bola = cv2.imread("Stickers/bola.png" , cv2.IMREAD_UNCHANGED)
bola = cv2.resize(bola, (90, 52))
arco = cv2.imread("Stickers/arco-iris.png" , cv2.IMREAD_UNCHANGED)
arco = cv2.resize(arco, (84, 68))
feliz = cv2.imread("Stickers/feliz.png" , cv2.IMREAD_UNCHANGED)
feliz = cv2.resize(feliz, (92, 64))

OPCAO = input(("Selecione a opcao desejada: (1 = Webcam), (2 = Selecionar foto) "))
match (OPCAO):
    case "1":
        original = cv2.VideoCapture(0)
        if not original.isOpened():
            print("Cannot open camera")
            exit()
        trackbarMouseCb()
        while True:
            ret, frame = original.read()
            if not ret:
                print("Can't receive frame (stream end?). Exiting ...")
                break
            pos = cv2.getTrackbarPos('Efeitos', 'Controle')
            posSticker = cv2.getTrackbarPos('Stickers', 'Controle')
            img = filters(frame, pos)
            cv2.imshow('Imagem', img)
            if cv2.waitKey(10) == ord('q'):
                break
        cv2.destroyAllWindows()

    case "2":
        arquivo = input("Qual o caminho para o arquivo: ")
        original = cv2.imread(arquivo , 1)
        original = cv2.resize(original, (1131, 752))
        img = original
        trackbarMouseCb()
        while (True):
            posEffects = cv2.getTrackbarPos('Efeitos', 'Controle')
            posSticker = cv2.getTrackbarPos('Stickers', 'Controle')         
            img = filters(original, posEffects)
            cv2.imshow('Imagem', img)
            if cv2.waitKey(10) == ord('q'):
                break
        cv2.destroyAllWindows()