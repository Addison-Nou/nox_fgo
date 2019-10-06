import tensorflow as tf
import numpy as np
from tensorflow.keras import datasets, layers, models
from screenshotter import screenshot
from image_to_data import convert_image_to_data
from image_modifier import crop_and_resize, index_to_label

model = tf.keras.models.load_model('./models/dragalia_model.h5')
real_time_image_path = './screenshots/_real-time.png'


def check_if_exists(label, filename):
    # Crop & resize a section of the screenshot
    new_file_path = crop_and_resize(filename, label, (32, 32))

    # Convert cropped & resized image into data
    np_frame = convert_image_to_data(new_file_path)

    # Perform a prediction and act on it.
    prediction = model.predict(np_frame)
    val = np.argmax(prediction[0])
    print('AI RESULT:', val, 'a.k.a', index_to_label[val])


def auto_pic():
    index = 0
    while(True):
        label = input('\nWhat would you like to check for the existence of?\n')

        # TODO: Remove or comment out
        # import time
        # time.sleep(3)
        # label = 'tap'
        # real_time_image_path = './screenshots/_real-time-{}.png'.format(index)

        screenshot(real_time_image_path)
        # check_if_exists(label, '_real-time-{}'.format(index))
        check_if_exists(label, '_real-time')

        index += 1


if __name__ == "__main__":
    # Take a screenshot
    index = 1
    auto_pic()