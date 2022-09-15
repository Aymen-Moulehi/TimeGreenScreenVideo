from datetime import time

import cv2

from background_generator import add_text_to_image
from time_incrumenteur import increment_time


def generate_counter_video(image, start: time, end: time):
    if end < start:
        raise Exception("start time must be less then end time")
    height, width, layers = image.shape
    size = (width, height)
    out = cv2.VideoWriter('output/output.avi', cv2.VideoWriter_fourcc(*'DIVX'), 1.0, size)
    while start < end:
        current_image = add_text_to_image(image, str(start))
        out.write(current_image)
        start = increment_time(start)
    out.release()
