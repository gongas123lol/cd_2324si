import cv2
import numpy as np


# generate Key
def generate_key(image_shape):
    key = np.random.randint(0, 256, image_shape)
    return key.astype(np.uint8)


# Encripts the image using the generated Key
def encrypt(image, key):
    encrypted_image = cv2.bitwise_xor(image, key)
    return encrypted_image


# Decrypts the image
def decrypt(encrypted_image, key):
    decrypted_image = cv2.bitwise_xor(encrypted_image, key)
    return decrypted_image


# Partially encrypts the image, given two points, start and end
def encrypt_portion(image, key, start_x, start_y, end_x, end_y):
    encrypted_image = image.copy()
    encrypted_image[start_y:end_y, start_x:end_x] = cv2.bitwise_xor(image[start_y:end_y, start_x:end_x],
                                                                    key[start_y:end_y, start_x:end_x])
    return encrypted_image


# Partially decrypts the image, given two points, start and end
def decrypt_portion(encrypted_image, key, start_x, start_y, end_x, end_y):
    decrypted_image = encrypted_image.copy()
    decrypted_image[start_y:end_y, start_x:end_x] = cv2.bitwise_xor(encrypted_image[start_y:end_y, start_x:end_x],
                                                                    key[start_y:end_y, start_x:end_x])
    return decrypted_image


def demo_grayscale():
    image = cv2.imread(r'C:\Users\ferra\PycharmProjects\CD1\teste_pb_2.jpg', cv2.IMREAD_GRAYSCALE)

    key = generate_key(image.shape)

    encrypted_image = encrypt(image, key)

    decrypted_image = decrypt(encrypted_image, key)

    cv2.imshow('Original Image Whole', image)
    cv2.imshow('Encrypted Image Whole', encrypted_image)
    cv2.imshow('Decrypted Image Whole', decrypted_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    start_x = 100
    start_y = 200
    end_x = 400
    end_y = 500

    encrypted_image_portion = encrypt_portion(image, key, start_x, start_y, end_x, end_y)

    decrypted_image_portion = decrypt_portion(encrypted_image_portion, key, start_x, start_y, end_x, end_y)

    cv2.imshow('Original Image portion', image)
    cv2.imshow('Encrypted Image portion', encrypted_image_portion)
    cv2.imshow('Decrypted Image portion', decrypted_image_portion)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def demo_colors():
    image = cv2.imread(r'C:\Users\ferra\PycharmProjects\CD1\teste_cores_2.jpg', cv2.IMREAD_COLOR)
    key = generate_key(image.shape)
    encrypted_image = encrypt(image, key)
    decrypted_image = decrypt(encrypted_image, key)

    cv2.imshow('Original Image Whole', image)
    cv2.imshow('Encrypted Image Whole', encrypted_image)
    cv2.imshow('Decrypted Image Whole', decrypted_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    start_x = 200
    start_y = 150
    end_x = 600
    end_y = 500

    encrypted_image_portion = encrypt_portion(image, key, start_x, start_y, end_x, end_y)

    decrypted_image_portion = decrypt_portion(encrypted_image_portion, key, start_x, start_y, end_x, end_y)

    cv2.imshow('Original Image portion', image)
    cv2.imshow('Encrypted Image portion', encrypted_image_portion)
    cv2.imshow('Decrypted Image portion', decrypted_image_portion)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#demo_colors()
demo_grayscale()

