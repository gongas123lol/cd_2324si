import numpy as np
import cv2

def generate_key(image_shape):
    # Gerar uma chave aleatória com o mesmo tamanho da imagem
    key = np.random.randint(0, 256, size=image_shape, dtype=np.uint8)
    return key

def encrypt(image, key, start_x=None, start_y=None, end_x=None, end_y=None):
    # Verificar se as coordenadas retangulares foram especificadas
    if start_x is not None and start_y is not None and end_x is not None and end_y is not None:
        # Cifrar apenas a área retangular especificada
        encrypted_area = cv2.bitwise_xor(image[start_y:end_y, start_x:end_x], key[start_y:end_y, start_x:end_x])
        image[start_y:end_y, start_x:end_x] = encrypted_area
    else:
        # Cifrar a imagem inteira
        image = cv2.bitwise_xor(image, key)
    return image

def decrypt(encrypted_image, key, start_x=None, start_y=None, end_x=None, end_y=None):
    # Verificar se as coordenadas retangulares foram especificadas
    if start_x is not None and start_y is not None and end_x is not None and end_y is not None:
        # Descriptografar apenas a área retangular especificada
        decrypted_area = cv2.bitwise_xor(encrypted_image[start_y:end_y, start_x:end_x], key[start_y:end_y, start_x:end_x])
        encrypted_image[start_y:end_y, start_x:end_x] = decrypted_area
    else:
        # Descriptografar a imagem inteira
        encrypted_image = cv2.bitwise_xor(encrypted_image, key)
    return encrypted_image

def main():
    # Carregar a imagem
    image = cv2.imread(r'C:\Users\ferra\PycharmProjects\CD1\test\barries.jpg', cv2.IMREAD_GRAYSCALE)

    # Gerar uma chave com o mesmo tamanho da imagem
    key = generate_key(image.shape)
    print(key)
    # Cifrar a imagem inteira
    encrypted_image = encrypt(image, key)

    # Decifrar a imagem inteira
    decrypted_image = decrypt(encrypted_image, key)

    # Cifrar apenas uma área retangular especificada (10 pixels a partir do topo e da esquerda, com largura de 100 pixels e altura de 50 pixels)
    encrypted_image_rect = encrypt(image, key, start_x=10, start_y=10, end_x=110, end_y=60)

    # Decifrar apenas uma área retangular especificada
    decrypted_image_rect = decrypt(encrypted_image_rect, key, start_x=10, start_y=10, end_x=110, end_y=60)

    # Exibir as imagens original, cifrada, decifrada e retangular
    cv2.imshow('Original Image', image)
    cv2.imshow('Encrypted Image', encrypted_image)
    cv2.imshow('Decrypted Image', decrypted_image)
    cv2.imshow('Encrypted Rectangular Image', encrypted_image_rect)
    cv2.imshow('Decrypted Rectangular Image', decrypted_image_rect)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
