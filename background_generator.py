import cv2
import numpy as np

from config import background, resolution

red = background['red']
green = background['green']
blue = background['blue']
default_width = resolution['width']
default_height = resolution['height']


def create_blank_image(width=default_width, height=default_height, rgb_color=(red, green, blue)):
    image = np.zeros((height, width, 3), np.uint8)
    color = tuple(reversed(rgb_color))
    image[:] = color
    return image


def add_text_to_image(image, text: str):
    image_copy = np.copy(image)
    font = cv2.FONT_HERSHEY_SIMPLEX
    text_size = cv2.getTextSize(text, font, 5, 10)[0]
    text_x = (image_copy.shape[1] - text_size[0]) // 2
    text_y = (image_copy.shape[0] + text_size[1]) // 2
    cv2.putText(image_copy, text, (text_x, text_y), font, 5, (255, 255, 255), 10)
    return image_copy
