import datetime
from background_generator import create_blank_image
from config import start_time, end_time
from video_generator import generate_counter_video

if __name__ == '__main__':
    image = create_blank_image()
    t1 = datetime.time(start_time['hour'], start_time['minute'], start_time['second'])
    t2 = datetime.time(end_time['hour'], end_time['minute'], end_time['second'])
    generate_counter_video(image, t1, t2)
