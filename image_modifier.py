from PIL import Image
import os

# Always crop() before calling resize()

box_locations = {
    'tap': (700, 800, 800, 900)
}

index_to_label = {
    0: 'invalid',
    1: 'tap'
}


def crop(filename, box):
    im = Image.open("./screenshots/" + filename + ".png")
    cropped_im = im.crop(box_locations[box])
    cropped_im.save("./screenshots/cropped/" +
                    filename + "-" + box + ".png", "PNG")
    # print('Cropped to size:', cropped_im.size)
    im.close()


def resize(filename, box, size):
    im = Image.open("./screenshots/cropped/" + filename + "-" + box + ".png")
    im_resized = im.resize(size, Image.ANTIALIAS)
    final_path = "./screenshots/resized/" + filename + "-" + box + ".png"
    im_resized.save(final_path, "PNG")
    im.close()
    return final_path


def crop_and_resize(filename, box, new_size):
    crop(filename, box)
    return resize(filename, box, new_size)


def run():
    screenshots_path = './screenshots/'
    onlyfiles = [f for f in os.listdir(screenshots_path) if os.path.isfile(
        os.path.join(screenshots_path, f))]

    for filename in onlyfiles:
        print('Cropping pieces from screenshot:', filename)
        filename = filename[:-4]
        for box in box_locations.keys():
            crop_and_resize(filename, box, (32, 32))


def test():
    filename = 'screencap-3'
    crop_and_resize(filename, 'tap', (32, 32))


if __name__ == "__main__":
    #test()
    run()