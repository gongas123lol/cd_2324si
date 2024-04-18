import numpy as np
import cv2

def generate_key(image_shape):
    key = np.random.randint(0, 256, size=image_shape, dtype=np.uint8)
    return key

def encrypt(image, key, start_x=None, start_y=None, end_x=None, end_y=None):
    cropped_area = image[start_y:end_y, start_x:end_x]
    cropped_key = generate_key(cropped_area.shape)
    encrypted_area = np.zeros_like(cropped_area)
    for i in range(3):
        encrypted_area[:,:,i] = cv2.bitwise_xor(cropped_area[:,:,i], cropped_key[:,:,i])
    image[start_y:end_y, start_x:end_x] = encrypted_area
    return image

def decrypt(encrypted_image, key, start_x=None, start_y=None, end_x=None, end_y=None):
    encrypted_area = encrypted_image[start_y:end_y, start_x:end_x]
    cropped_key = generate_key(encrypted_area.shape)
    decrypted_area = np.zeros_like(encrypted_area)
    for i in range(3):
        decrypted_area[:,:,i] = cv2.bitwise_xor(encrypted_area[:,:,i], cropped_key[:,:,i])
    encrypted_image[start_y:end_y, start_x:end_x] = decrypted_area
    return encrypted_image

def main():
    image = cv2.imread(r'C:\Users\ferra\PycharmProjects\CD1\test\barries.jpg')
    key = generate_key(image.shape)
    encrypted_image = encrypt(image, key, start_x=10, start_y=10, end_x=110, end_y=60)
    decrypted_image = decrypt(encrypted_image, key, start_x=10, start_y=10, end_x=110, end_y=60)
    cv2.imshow('Original Image', image)
    cv2.imshow('Encrypted Image', encrypted_image)
    cv2.imshow('Decrypted Image', decrypted_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
